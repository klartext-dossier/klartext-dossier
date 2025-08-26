import unittest

import io, os

from klartext import Parser, ParseError


def str_to_file(text):
    return io.TextIOWrapper(io.BytesIO(text.encode('utf8')), encoding='utf8')


class TestGetIndent(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_empty(self):
        self.assertEqual(0, self.parser._getIndent(''))

    def test_two(self):
        with self.assertRaises(ParseError):
            self.assertEqual(0, self.parser._getIndent('  a'))

    def test_four(self):
        self.assertEqual(1, self.parser._getIndent('    a'))

    def test_eight(self):
        self.assertEqual(2, self.parser._getIndent('        a'))


class TestRemoveSurroundingBlankLines(unittest.TestCase):

    def test_normal(self):
        T = """


1
2

3


4


"""
        R = """1
2

3


4"""
        self.assertEqual(R, Parser.removeSurroundingBlankLines(T, None))

    def test_empty(self):
        T = """


"""
        R = ""
        self.assertEqual(R, Parser.removeSurroundingBlankLines(T, None))


class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()
        self.basedir = os.path.dirname(__file__)
        
    def runParser(self, text):
        return self.parser.parse(str_to_file(text), basedir=self.basedir)
        
    def test_empty_text(self):
        KT = """
"""
        self.assertEqual(b'', self.runParser(KT))

    def test_simple_text(self):
        KT = """
foobar
"""
        self.assertEqual(b'foobar\n', self.runParser(KT))
        
    def test_simple_tag(self):
        KT = """
foobar:
"""
        self.assertEqual(b'<foobar>\n</foobar>\n', self.runParser(KT))

    def test_parse_error(self):
        KT = """
        foobar:
        """
        with self.assertRaises(ParseError):
            with self.assertLogs("ERROR"):
                self.runParser(KT)

    def test_dont_convert_text(self):
        KT = """
This is not *markdown*.
"""
        self.assertEqual(b'This is not *markdown*.\n', self.runParser(KT))

    def test_namespaces(self):
        KT = """
!import "www.hoelzer-kluepfel.de" as mhk

mhk::tag:
"""
        self.assertEqual(b'<mhk:tag xmlns:mhk="www.hoelzer-kluepfel.de">\n</mhk:tag>\n', self.runParser(KT))

    def test_namespaces_and_attributes(self):
        KT = """
!import "www.hoelzer-kluepfel.de" as mhk

mhk::tag: foo="bar"
"""
        self.assertEqual(b'<mhk:tag xmlns:mhk="www.hoelzer-kluepfel.de" foo="bar">\n</mhk:tag>\n', self.runParser(KT))

    def test_unknwnom_namespace(self):
        KT = """
mhk::tag: foo="bar"
"""
        with self.assertRaises(ParseError):
            self.runParser(KT)

    def test_include_fails(self):
        KT = """
!include "7idh87hnvd.kt"
"""
        with self.assertRaises(ParseError):
            self.runParser(KT)

    def test_include(self):
        KT = """
!include "included.kt"
This is text.
"""
        self.assertEqual(b'This is included text.\nThis is text.\n', self.runParser(KT))

    def test_include_indented(self):
        KT = """
tag:
!include "included.kt"
tag:
    !include "included.kt"
"""
        self.assertEqual(b'<tag>\n</tag>\nThis is included text.\n<tag>\nThis is included text.\n</tag>\n', self.runParser(KT))

    def test_markdown_simple(self):
        KT = """
This is *markdown*.
"""
        self.assertEqual(b'<p>This is <em>markdown</em>.</p>\n', self.parser.parse(str_to_file(KT), convert_text=Parser.convertMarkdown))

    def test_markdown_inline(self):
        KT = """
This is /em/markdown/.
"""
        self.assertEqual(b'<p>This is <em>markdown</em>.</p>\n', self.parser.parse(str_to_file(KT), convert_text=Parser.convertMarkdown))

    def test_markdown_glossary(self):
        KT = """
This is {markdown}.
"""
        self.assertEqual(b'<p>This is <a data-type="xref" data-xrefstyle="glossary" href="#markdown">markdown</a>.</p>\n', self.parser.parse(str_to_file(KT), convert_text=Parser.convertMarkdown))


if __name__ == '__main__':
    unittest.main()