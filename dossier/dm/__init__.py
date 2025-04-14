from .lxml_extensions import register_dossier_extensions, register_vcf_extensions
from .main import run_dm

register_dossier_extensions('http://klartext-dossier.org/dossier')
register_vcf_extensions('http://klartext-dossier.org/vcf')