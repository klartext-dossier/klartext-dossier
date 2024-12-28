''' Module providing the checkbox extension for Markdown.
'''

import re

from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown import Markdown


class CheckboxPostprocessor(Postprocessor):

    list_pattern = re.compile(r'<ul([^>]*)>\s*<li class')
    pattern = re.compile(r'<li>\[([ Xx])\]')

    def run(self, text: str) -> str:

        text = re.sub(self.pattern, self.convert_checkbox, text)
        text = re.sub(self.list_pattern, self.convert_checklist, text)
        return text

    def convert_checklist(self, match: re.Match) -> str:

        return f'<ul{match.group(1)} class="checklist">\n<li class'

    def convert_checkbox(self, match: re.Match) -> str:

        if ' ' != match.group(1):
            cls = 'checked'
        else:
            cls = 'unchecked'

        return f'<li class="{cls}">'


class CheckboxExtension(Extension):

    """ Extension for Checkboxes.

        Convert markdown checkboxes to xhtml compliant xml.

        Examples:

            The input:

                - [ ] unchecked
                - [x] checked

            will be converted to:

                <ul class="checklist">
                    <li class="unchecked">unchecked</li>
                    <li class="checked">checked</li>
                </ul>        
    """

    def extendMarkdown(self, md: Markdown) -> None:

        md.postprocessors.register(CheckboxPostprocessor(md), 'Checkbox', 100)


def makeExtension(**kwargs):

    return CheckboxExtension(**kwargs)
