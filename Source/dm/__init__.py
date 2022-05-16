from distutils.command.build_scripts import first_line_re
import hashlib, lxml.etree, re, logging


# register LXML extensions - dossier

ns = lxml.etree.FunctionNamespace('http://www.hoelzer-kluepfel.de/dossier')


def string(str_or_list):
    if isinstance(str_or_list, list):
        if len(str_or_list) == 1:
            return str_or_list[0]
    return str_or_list

MULT_SPACES = re.compile(r'\s+')


def ext_match_g(context, text, used_text):
    text = string(text).strip().lower()
    used_text = string(used_text).strip().lower()
    # logging.debug(f'match_g: "{text}" == "{used_text}"')
    return text == used_text

ns['match-g'] = ext_match_g


def ext_id(context, text):
    return '_' + MULT_SPACES.sub('_', string(text).strip())

ns['id'] = ext_id


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
ns['unique-id'] = ext_unique_id


def ext_lowercase(context, text):
    return string(text).lower()
ns['lower-case'] = ext_lowercase


def ext_uppercase(context, text):
    return string(text).upper()
ns['upper-case'] = ext_uppercase


def ext_sentencecase(context, text):
    text = string(text)
    if len(text) <= 1:
        return text.upper()
    return text[:1].upper() + text[1:].lower()
ns['sentence-case'] = ext_sentencecase


def ext_lstrip(context, text):
    return string(text).lstrip()
ns['lstrip'] = ext_lstrip


def ext_rstrip(context, text):
    return string(text).rstrip()
ns['rstrip'] = ext_rstrip


def ext_strip(context, text):
    return string(text).strip()
ns['strip'] = ext_strip


def ext_simplify(context, text):
    return MULT_SPACES.sub(' ', string(text))
ns['simplify'] = ext_simplify


# register LXML extensions - VCF

ns = lxml.etree.FunctionNamespace('http://www.hoelzer-kluepfel.de/vcf')

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


ns['N'] = ext_N
