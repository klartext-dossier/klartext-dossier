""" Module providing xpath extensions.
"""

import hashlib, lxml.etree, re


MULT_SPACES = re.compile(r'\s+')


def string(str_or_list: str | list[str]) -> str:

    if isinstance(str_or_list, list):
        return str_or_list[0]
        
    return str(str_or_list)


def ext_match_g(context: lxml.extensions._BaseContext, text: str, used_text: str) -> bool:

    """ Compares two texts case-insensitive.
    
        Args:
            context:   the xpath context
            text:      first string
            used_text: seconde string

        Returns:
            true, if the strings are equal when compared case-insensitive, otherwise false
    """

    text = string(text).strip().lower()
    used_text = string(used_text).strip().lower()
    return text == used_text


def ext_id(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

    """ Generates a textual id.
    
        Args:
            context:   the xpath context
            text:      a text string

        Returns:
            the text, with whitespaces converted to '_', and prefixed by '_'
    """

    return '_' + MULT_SPACES.sub('_', string(text).strip())


def node_id(node) -> str:

    index = node.getparent().index(node) if node.getparent() is not None else 0
    return f'id-{node.tag}[{index}]-'.encode('ascii')


def ext_unique_id(context: lxml.extensions._BaseContext) -> str:

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


def ext_lowercase(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

    """ Converts a text to lowercase.
    
        Args:
            context: the xpath context (containing the current node)
            text:    a text string

        Returns:
            the text converted to lowercase
    """

    return string(text).lower()


def ext_uppercase(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

    """ Converts a text to uppercase.
    
        Args:
            context: the xpath context (containing the current node)
            text:    a text string

        Returns:
            the text converted to uppercase
    """
    
    return string(text).upper()


def ext_sentencecase(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

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


def ext_lstrip(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

    """ Removes leading whitespace.
    
        Args:
            context: the xpath context
            text:    a text string

        Returns:
            the text without leading whitespace
    """
    
    return string(text).lstrip()


def ext_rstrip(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

    """ Removes trailing whitespace.
    
        Args:
            context: the xpath context
            text:    a text string

        Returns:
            the text without trailing whitespace
    """
    
    return string(text).rstrip()


def ext_strip(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

    """ Removes leading and trailing whitespace.
    
        Args:
            context: the xpath context
            text:    a text string

        Returns:
            the text without leading and trailing whitespace
    """
    
    return string(text).strip()


def ext_simplify(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

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

    ns['match-g'] = ext_match_g
    ns['id'] = ext_id
    ns['unique-id'] = ext_unique_id
    ns['lower-case'] = ext_lowercase
    ns['upper-case'] = ext_uppercase
    ns['sentence-case'] = ext_sentencecase
    ns['lstrip'] = ext_lstrip
    ns['rstrip'] = ext_rstrip
    ns['strip'] = ext_strip
    ns['simplify'] = ext_simplify


def ext_N(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

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


def ext_ADR(context: lxml.extensions._BaseContext, text: str | list[str]) -> str:

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
