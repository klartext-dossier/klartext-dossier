Feature: Tests running pipelines

# File task -------------------------------------

Scenario: Testing the 'file' task - 101 - Create a simple markdown content and pass it on to the next task.

    When running the pipeline 101_file.dm
    Then the file 101_file__o.test.md is equal to 101_file__o.md

Scenario: Testing the 'file' task - 103 - Create content with unicode characters and save it to a UTF-16 encoded file

    When running the pipeline 103_file.dm
    Then the file 103_file__o.test.md is equal to 103_file__o.md

Scenario: Testing the 'file' task - 104 - Create markdown content and directly save it to a file

    When running the pipeline 104_file.dm
    Then the file 104_file__o.test.md is equal to 104_file__o.md

Scenario: Testing the 'file' task - 105 - Create a file, but do not provide content => TaskException

    When running the pipeline 105_file.dm
    Then error code -2 is returned

Scenario: Testing the 'file' task - 106 - Provide two output files => TaskException

    When running the pipeline 106_file.dm
    Then error code -2 is returned

Scenario: Testing the 'file' task - 107 - Provide an input file => TaskException

    When running the pipeline 107_file.dm
    Then error code -2 is returned

Scenario: Testing the 'file' task - 108 - Provide incorrect child element => TaskException

    When running the pipeline 108_file.dm
    Then error code -2 is returned

Scenario: Testing the 'file' task - 109 - Provide incorrect child attribute => TaskException

    When running the pipeline 109_file.dm
    Then error code -2 is returned


# Markdown task ---------------------------------

Scenario: Testing the 'markdown-to-xhtml' task - 201 - Simple conversion from markdown to xhtml

    When running the pipeline 201_markdown.dm
    Then the file 201_markdown__o.test.xhtml is equal to 201_markdown__o.xhtml

Scenario: Testing the 'markdown-to-xhtml' task - 202 - Conversion from a markdown file to xhtml

    When running the pipeline 202_markdown.dm
    Then the file 202_markdown__o.test.xhtml is equal to 202_markdown__o.xhtml

Scenario: Testing the 'markdown-to-xhtml' task - 203 - Conversion from a markdown file to an xhtml file

    When running the pipeline 203_markdown.dm
    Then the file 203_markdown__o.test.xhtml is equal to 203_markdown__o.xhtml
    Then the file 203b_markdown__o.test.xhtml is equal to 203_markdown__o.xhtml

Scenario: Testing the 'markdown-to-xhtml' task - 204 - Conversion from a u16 encoded markdown file to an xhtml file

    When running the pipeline 204_markdown.dm
    Then the file 204_markdown__o.test.xhtml is equal to 204_markdown__o.xhtml

Scenario: Testing the 'markdown-to-xhtml' task - 205 - Conversion from a markdown file to an u16 encoded xhtml file

    When running the pipeline 205_markdown.dm
    Then the file 205_markdown__o.test.xhtml is equal to 205_markdown__o.xhtml


# Dump task -------------------------------------

Scenario: Testing the 'dump' taks - 301 - Dump simple content

    When running the pipeline 301_dump.dm
    Then it displays "This is a test."

Scenario: Testing the 'dump' taks - 302 - Dump unicode content

    When running the pipeline 302_dump.dm
    Then it displays "This is a file using unicode: ♥ ♠ ♣ ♦"

Scenario: Testing the 'dump' taks - 303 - Dump file content

    When running the pipeline 303_dump.dm
    Then it displays "This is a file using unicode: ♥ ♠ ♣ ♦"    


# Save task -------------------------------------

Scenario: Testing the 'save' task - 401 - Create a simple markdown content and save it

    When running the pipeline 401_save.dm
    Then the file 401_save__o.test.md is equal to 401_save__o.md

Scenario: Testing the 'save' task - 402 - Create a simple markdown content and save it with other encoding

    When running the pipeline 402_save.dm
    Then the file 402_save__o.test.md is equal to 402_save__o.md


# Load task -------------------------------------

Scenario: Testing the 'load' task - 501 - Load a file

    When running the pipeline 501_load.dm
    Then the file 501_load__o.test.md is equal to 501_load__o.md

# xhtml-to-pdf task -----------------------------

Scenario: Testing the 'xhtml' task - 601 - Test generating PDF

    When running the pipeline 601_xhtml-to-pdf.dm
    Then the file 601_xhtml-to-pdf__o.test.pdf is equal to 601_xhtml-to-pdf__o.pdf

Scenario: Testing the 'xhtml' task - 602 - Test converting an XHTML file directly to PDF

    When running the pipeline 602_xhtml-to-pdf.dm
    Then the file 602_xhtml-to-pdf__o.test.pdf is equal to 602_xhtml-to-pdf__o.pdf

Scenario: Testing the 'xhtml' task - 603 - Test converting an incorrect XHTML file to PDF => no exception, as parser is tolerant...

    When running the pipeline 603_xhtml-to-pdf.dm
    Then no exception is thrown
    Then the file 603_xhtml-to-pdf__o.test.pdf is equal to 603_xhtml-to-pdf__o.pdf

Scenario: Testing the 'xhtml' task - 604 - Test generating PDF with a non-existent stylesheet => TaskException

    When running the pipeline 604_xhtml-to-pdf.dm
    Then error code -2 is returned

Scenario: Testing the 'xhtml' task - 605 - Test generating PDF with an implicit stylesheet

    When running the pipeline 605_xhtml-to-pdf.dm
    Then the file 605_xhtml-to-pdf__o.test.pdf is equal to 605_xhtml-to-pdf__o.pdf


# xml-validate task -----------------------------

Scenario: Testing the 'xml-validate' task - 701 - Test validating correct XML against schema file

    When running the pipeline 701_validate.dm
    Then no exception is thrown

Scenario: Testing the 'xml-validate' task - 701 - Test validating incorrect XML against schema file

    When running the pipeline 702_validate.dm
    Then error code -2 is returned

Scenario: Testing the 'xml-validate' task - 703 - Test validating XML against an non-existant schema file

    When running the pipeline 703_validate.dm
    Then error code -2 is returned

Scenario: Testing the 'xml-validate' task - 704 - Test validating XML against an incorrect schema file

    When running the pipeline 704_validate.dm
    Then error code -2 is returned

Scenario: Testing the 'xml-validate' task - 705 - Test validating an incorrect XML file

    When running the pipeline 705_validate.dm
    Then error code -2 is returned


# copy task -------------------------------------

Scenario: Testing the 'copy' task - 801 - Copy a file to another

    When running the pipeline 801_copy.dm
    Then the file 801_copy__o.test.md is equal to 801_copy__o.md
    Then the file 801b_copy__o.test.md is equal to 801_copy__o.md

Scenario: Testing the 'copy' task - 802 - Copy a file to another, changing the encoding

    When running the pipeline 802_copy.dm
    Then the file 802_copy__o.test.md is equal to 802_copy__o.md
    Then the file 802b_copy__o.test.md is equal to 802b_copy__o.md


# markdown-include task -------------------------

Scenario: Testing the 'markdown-include' task - 901 - Include Markdown Files

    When running the pipeline 901_include.dm
    Then the file 901_include__o.test.md is equal to 901_include__o.md


# klartext-to-xml task --------------------------

Scenario: Testing the 'klartext-to-xml' task - C01 - Simple conversion from klartext to xml

    When running the pipeline C01_klartext.dm
    Then the file C01_klartext__o.test.xml is equal to C01_klartext__o.xml


# include task ----------------------------------

Scenario: Testing the 'include' task - E01 - Include multiple klartext files

    When running the pipeline E01_include.dm
    Then the file E01_include__o.test.xml is equal to E01_include__o.xml

Scenario: Testing the 'include' task - E02 - Include nested klartext files

    When running the pipeline E02_include.dm
    Then the file E02_include__o.test.xml is equal to E02_include__o.xml

# pdf-to-png task ----------------------------------

Scenario: Testing the 'pdf-to-png' task - G01

    When running the pipeline G01_pdf-to-png.dm
    # Then the file G01_pdf-to-png__o.test.zip is equal to G01_pdf-to-png__o.zip

# less stylesheet ----------------------------------

Scenario: Testing .less styesheets - H01

    When running the pipeline H01_less_stylesheet.dm
    Then the file H01_less_stylesheet__o.test.pdf is equal to H01_less_stylesheet__o.pdf
