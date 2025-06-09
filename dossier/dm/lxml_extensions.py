""" Module providing xpath extensions.
"""

import hashlib, lxml.etree, re


MULT_SPACES  = re.compile(r'\s+')
HREF_FULL_RE = re.compile(r'#(?P<glossary>[a-zA-Z0-9]+)__(?P<term>.*)')
HREF_PART_RE = re.compile(r'#(?P<term>.*)')


def string(str_or_list: str | list[str]) -> str:

    if isinstance(str_or_list, list):
        return str_or_list[0]
        
    return str(str_or_list)


def ext_term_g(context: object, terms: list[lxml.etree._Element]) -> str:

    for term in terms:
        return term.text.strip()


def ext_entry_link_g(context: object, entries: list[lxml.etree._Element]) -> str:

    for entry in entries:
        glossary = entry.getparent()
        glossary_id = glossary.get('id')
        term = entry.find('term')

        if term is not None:
            id_text = MULT_SPACES.sub('_', term.text.strip().lower())

            if glossary_id is not None:
                return f'{glossary_id}__{id_text}'
            else:
                return f'{id_text}'

    return ""


def ext_lookup_g(context: object, refs: list[lxml.etree._Element]) -> lxml.etree._Element:

    root = context.context_node.getroottree()

    if len(refs) != 1:
        return False    
    ref = refs[0]

    link = lxml.etree.Element('a')
    link.set('data-type', 'xref')
    link.set('data-xrefstyle', 'glossary')

    href = HREF_FULL_RE.match(ref.get('href'))
    if href:
        glossary = href.group("glossary")
        term = href.group("term")
        terms = root.xpath(f'//glossary[@id="{glossary}"]//term')
        for text in terms:
            if MULT_SPACES.sub('_', text.text.strip().lower()) == term:
                link.set('href', f'#{glossary}__{term}')
                link.text = ref.text
                link.set('data-match', 'full')
                return link

    href = HREF_PART_RE.match(ref.get('href'))
    if href:
        term = href.group("term")
        terms = root.xpath(f'//glossary//term')
        cnt = 0
        for text in terms:
            if MULT_SPACES.sub('_', text.text.strip().lower()) == term:
                cnt += 1
                glossary = text.getparent().getparent().get('id')
                if glossary is not None:                    
                    link.set('href', f'#{glossary}__{term}')
                else:    
                    link.set('href', f'#{term}')
                link.text = ref.text
        if 1 == cnt:
            link.set('data-match', 'unique')
            return link
        if cnt > 1:
            link.set('data-match', 'ambigiuous')
            return link

    return ref


def ext_defined_fully_g(context: object, refs: list[lxml.etree._Element]) -> bool:

    root = context.context_node.getroottree()

    href = HREF_FULL_RE.match(string(refs))
    if href:
        glossary = href.group("glossary")
        term = href.group("term")
        terms = root.xpath(f'//glossary[@id="{glossary}"]//term')
        for text in terms:
            if MULT_SPACES.sub('_', text.text.strip().lower()) == term:
                # print(f'MATCH {glossary}, {term}')
                return True

    return False


def ext_defined_uniquely_g(context: object, refs: list[lxml.etree._Element]) -> bool:

    root = context.context_node.getroottree()

    href = HREF_PART_RE.match(string(refs))
    if href:
        term = href.group("term")
        terms = root.xpath(f'//glossary//term')
        for text in terms:
            cnt = 0
            if MULT_SPACES.sub('_', text.text.strip().lower()) == term:
                cnt += 1
            
            if cnt>0:
                print(f'MATCH {term} {cnt} times')
                return True

    return False


def ext_match_g(context: object, text: str, used_text: str) -> bool:

    """ Compares two texts case-insensitive.
    
        Args:
            context:   the xpath context
            text:      first string
            used_text: second string

        Returns:
            true, if the strings are equal when compared case-insensitive, otherwise false
    """
    
    text = string(text).strip().lower()
    used_text = string(used_text).strip().lower()

    return text == used_text


def _refered_glossary(reference: lxml.etree._Element) -> str | None:
    href = HREF_FULL_RE.match(reference.get('href'))
    if href:
        return href.group('glossary')

    return None


def _term_used_g(context: object, term: str) -> bool:

    root = context.context_node.getroottree()

    term_text = string(term).strip().lower()
    term_id = context.eval_context['glossary'].get('id') if 'glossary' in context.eval_context else None

    references = root.xpath(f'//xhtml:a[@data-type="xref" and @data-xrefstyle="glossary" and not(ancestor::glossary)]', namespaces={'xhtml': 'http://www.w3.org/1999/xhtml'})
    for reference in references:
        ref_text = reference.text.strip().lower()
        ref_id = _refered_glossary(reference)

        if ext_match_g(context, term_text, ref_text) and ((term_id == ref_id) or (ref_id is None)):
            return True

    return False


def ext_entry_used_g(context: object, entries: list[lxml.etree._Element]) -> bool:
    
    root = context.context_node.getroottree()
    parent = context.context_node.getparent()

    term_id = None
    if parent is not None and 'glossary' == parent.tag:
        context.eval_context['glossary'] = parent
        term_id = parent.get('id')

    for entry in entries:
        for term in entry.findall('term'):
            term_text = term.text.strip().lower()

            # check if the term is directly used in a reference
            if _term_used_g(context, term_text):
                return True
    
            # check if the term is used in the definition of a used term
            for glossary_entry in root.xpath(f'//glossary/entry'):
                if glossary_entry != entry:
                    references = glossary_entry.xpath(f'definition//xhtml:a[@data-type="xref" and @data-xrefstyle="glossary"]', namespaces={'xhtml': 'http://www.w3.org/1999/xhtml'})
                    for reference in references:
                        ref_text = reference.text.strip().lower()
                        ref_id = _refered_glossary(reference)

                        if ext_match_g(context, term_text, ref_text) and ((term_id == ref_id) or (ref_id is None)):
                            if ext_entry_used_g(context, [glossary_entry]):
                                return True

    return False


def ext_id(context: object, text: str | list[str]) -> str:

    """ Generates a textual id.
    
        Args:
            context:   the xpath context
            text:      a text string

        Returns:
            the text, with whitespaces converted to '_', and prefixed by '_'
    """

    return '_' + MULT_SPACES.sub('_', string(text).strip())


def node_id(node) -> bytes:

    index = node.getparent().index(node) if node.getparent() is not None else 0
    return f'id-{node.tag}[{index}]-'.encode('ascii')


def ext_unique_id(context: object) -> str:

    """ Calculates a unique id for the current node.
    
        Args:
            context: the xpath context (containing the current node)

        Returns:
            an ID for the current node, unique within the XML document
    """

    md = hashlib.md5()

    node = context.context_node
    md.update(node_id(node))
    for node in context.context_node.iterancestors():
       md.update(node_id(node))

    return md.hexdigest()


def ext_lowercase(context: object, text: str | list[str]) -> str:

    """ Converts a text to lowercase.
    
        Args:
            context: the xpath context (containing the current node)
            text:    a text string

        Returns:
            the text converted to lowercase
    """

    return string(text).lower()


def ext_uppercase(context: object, text: str | list[str]) -> str:

    """ Converts a text to uppercase.
    
        Args:
            context: the xpath context (containing the current node)
            text:    a text string

        Returns:
            the text converted to uppercase
    """
    
    return string(text).upper()


def ext_sentencecase(context: object, text: str | list[str]) -> str:

    """ Capitalize a text.
    
        Args:
            context: the xpath context (containing the current node)
            text:    a text string

        Returns:
            the text with the first character uppercase, all other lowercase
    """
    
    text = string(text)
    if len(text) <= 1:
        return text.upper()
    return text[:1].upper() + text[1:].lower()


def ext_lstrip(context: object, text: str | list[str]) -> str:

    """ Removes leading whitespace.
    
        Args:
            context: the xpath context
            text:    a text string

        Returns:
            the text without leading whitespace
    """
    
    return string(text).lstrip()


def ext_rstrip(context: object, text: str | list[str]) -> str:

    """ Removes trailing whitespace.
    
        Args:
            context: the xpath context
            text:    a text string

        Returns:
            the text without trailing whitespace
    """
    
    return string(text).rstrip()


def ext_strip(context: object, text: str | list[str]) -> str:

    """ Removes leading and trailing whitespace.
    
        Args:
            context: the xpath context
            text:    a text string

        Returns:
            the text without leading and trailing whitespace
    """
    
    return string(text).strip()


def ext_simplify(context: object, text: str | list[str]) -> str:

    """ Simplifies whitespace.
    
        Args:
            context: the xpath context (containing the current node)
            text:    a text string

        Returns:
            the text with multiple consecutive whitespace converted to a single space
    """

    return MULT_SPACES.sub(' ', string(text))


def register_dossier_extensions(namespace: str) -> None:

    """ Registers the lxml extensions.

        Registers the extensions

        - id
        - lower-case
        - lstrip
        - match-g
        - rstrip
        - sentence-case
        - simplify
        - strip
        - unique-id
        - upper-case

        Args:
            namespace: the namespace to register the extentions under.
    """

    ns = lxml.etree.FunctionNamespace(namespace)

    ns['entry-used-g'] = ext_entry_used_g
    ns['lookup-g'] = ext_lookup_g
    ns['defined-fully-g'] = ext_defined_fully_g
    ns['defined-uniquely-g'] = ext_defined_uniquely_g
    ns['entry-link-g'] = ext_entry_link_g
    ns['match-g'] = ext_match_g
    ns['term-g'] = ext_term_g
    ns['id'] = ext_id
    ns['unique-id'] = ext_unique_id
    ns['lower-case'] = ext_lowercase
    ns['upper-case'] = ext_uppercase
    ns['sentence-case'] = ext_sentencecase
    ns['lstrip'] = ext_lstrip
    ns['rstrip'] = ext_rstrip
    ns['strip'] = ext_strip
    ns['simplify'] = ext_simplify


def ext_N(context: object, text: str | list[str]) -> str:

    name = string(text).strip()

    prefix = ''
    for p in ['Prof. Dr.', 'Prof.', 'Dr.']:
        if name.startswith(p):
            prefix = p
            name = name.replace(p, '', 1).strip()

    suffix = ''
    for p in ['MD', 'MSc']:
        if name.endswith(', ' + p):
            suffix = p
            name = name.replace(', ' + p, '', 1).strip()

    first = ''
    middle = ''
    last = ''

    parts = name.split()
    if (1 == len(parts)):
        last = parts[0]
    elif (2 == len(parts)):
        first = parts[0]
        last = parts[1]
    elif (2 < len(parts)):
        first = parts[0]
        middle = parts[1]
        for i in range(2, len(parts)-1):
            middle += ' ' + parts[i]
        last = parts[len(parts)-1]

    return last + ';' + first + ';' + middle + ';' + prefix + ';' + suffix


def ext_ADR(context: object, text: str | list[str]) -> str:

    adr = string(text).strip()

    street = ''
    city = ''
    region = ''
    code = ''
    country = ''

    parts = adr.split(',')
    if (1 == len(parts)):        
        city = parts[0].strip()
    elif (2 == len(parts)):
        street = parts[0].strip()
        city = parts[1].strip()
    elif (3 == len(parts)):
        street = parts[0].strip()
        city = parts[1].strip()
        country = parts[2].strip()
    elif (4 == len(parts)):
        street = parts[0].strip()
        city = parts[1].strip()
        region = parts[2].strip()
        country = parts[3].strip()

    parts = city.split(maxsplit=1)
    if (2 == len(parts)):
        code = parts[0].strip()
        city = parts[1].strip()
    parts = region.split(maxsplit=1)
    if (2 == len(parts) and 'USA' == country):
        region = parts[0].strip()
        code = parts[1].strip()

    return ";;" + street + ";" + city + ";" + region + ";" + code + ";" + country


def register_vcf_extensions(namespace: str) -> None:

    ns = lxml.etree.FunctionNamespace(namespace)

    ns['N'] = ext_N
    ns['ADR'] = ext_ADR
