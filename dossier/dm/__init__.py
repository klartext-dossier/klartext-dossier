from .lxml_extensions import register_dossier_extensions, register_glossary_extensions, register_vcf_extensions
from .main import run_dm

register_dossier_extensions('http://klartext-dossier.org/dossier')
register_glossary_extensions('http://klartext-dossier.org/glossary')
register_vcf_extensions('http://klartext-dossier.org/vcf')