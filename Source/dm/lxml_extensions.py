import hashlib, lxml.etree, re


MULT_SPACES = re.compile(r'\s+')


def string(str_or_list):

    if isinstance(str_or_list, list):
        if len(str_or_list) == 1:
            return str_or_list[0]
    return str_or_list


def ext_match_g(context, text, used_text):

    text = string(text).strip().lower()
    used_text = string(used_text).strip().lower()
    return text == used_text


def ext_id(context, text):

    return '_' + MULT_SPACES.sub('_', string(text).strip())


def node_id(node):

    index = node.getparent().index(node) if node.getparent() is not None else 0
    return f'id-{node.tag}[{index}]-'.encode('ascii')


def ext_unique_id(context):

    md = hashlib.md5()

    node = context.context_node
    md.update(node_id(node))
    for node in context.context_node.iterancestors():
       md.update(node_id(node))

    return md.hexdigest()


def ext_lowercase(context, text):

    return string(text).lower()


def ext_uppercase(context, text):

    return string(text).upper()


def ext_sentencecase(context, text):

    text = string(text)
    if len(text) <= 1:
        return text.upper()
    return text[:1].upper() + text[1:].lower()


def ext_lstrip(context, text):

    return string(text).lstrip()


def ext_rstrip(context, text):

    return string(text).rstrip()


def ext_strip(context, text):

    return string(text).strip()


def ext_simplify(context, text):

    return MULT_SPACES.sub(' ', string(text))


def register_dossier_extensions(namespace: str):

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


def ext_N(context, text):

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


def ext_ADR(context, text):

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


def register_vcf_extensions(namespace: str):

    ns = lxml.etree.FunctionNamespace(namespace)

    ns['N'] = ext_N
    ns['ADR'] = ext_ADR
