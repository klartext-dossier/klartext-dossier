from .lxml_extensions import register_dossier_extensions, register_vcf_extensions
from .main import run_dm

register_dossier_extensions('http://www.hoelzer-kluepfel.de/dossier')
register_vcf_extensions('http://www.hoelzer-kluepfel.de/vcf')