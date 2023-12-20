import re

from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor


class CheckboxExtension(Extension):

    def extendMarkdown(self, md):
        md.postprocessors.register(CheckboxPostprocessor(md), 'Checkbox', 100)


class CheckboxPostprocessor(Postprocessor):

    list_pattern = re.compile(r'<ul([^>]*)>\s*<li class')
    pattern = re.compile(r'<li>\[([ Xx])\]')

    def run(self, html):
        html = re.sub(self.pattern, self.convert_checkbox, html)
        html = re.sub(self.list_pattern, self.convert_checklist, html)
        return html

    def convert_checklist(self, match):
        return f'<ul{match.group(1)} class="checklist">\n<li class'

    def convert_checkbox(self, match):
        if ' ' != match.group(1):
            cls = 'checked'
        else:
            cls = 'unchecked'

        return f'<li class="{cls}">'


def makeExtension(**kwargs):  # pragma: no cover
    return CheckboxExtension(**kwargs)
