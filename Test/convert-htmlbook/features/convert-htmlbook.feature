Feature: Test converting htmlbook

Scenario Outline: Converting htmlbook

    When converting the <INPUT FILE> to PDF
    Then the PDF output is equal to <PDF FILE>

Examples: Input files

    | INPUT FILE                     | PDF FILE                    |
                                     
    | 000_empty_file__o.html         | 000_empty_file__o.pdf       |
    | 310_book__o.html               | 310_book__o.pdf             |
    | 311_book__o.html               | 311_book__o.pdf             |
    | 320_chapter__o.html            | 320_chapter__o.pdf          |
    | 321_chapter__o.html            | 321_chapter__o.pdf          |
    | 330_appendix__o.html           | 330_appendix__o.pdf         |
    | 340_bibliography__o.html       | 340_bibliography__o.pdf     |
    | 350_glossary__o.html           | 350_glossary__o.pdf         |
    | 360_preface__o.html            | 360_preface__o.pdf          |
    | 370_frontmatter__o.html        | 370_frontmatter__o.pdf      |
    | 380_backmatter__o.html         | 380_backmatter__o.pdf       |
    | 390_part__o.html               | 390_part__o.pdf             |
    | 3A0_nav__o.html                | 3A0_nav__o.pdf              |
    | 3B0_index__o.html              | 3B0_index__o.pdf            |
    | 3C0_section__o.html            | 3C0_section__o.pdf          |
    | 410_paragraph__o.html          | 410_paragraph__o.pdf        |
    | 420_sidebar__o.html            | 420_sidebar__o.pdf          |
    | 430_admonition__o.html         | 430_admonition__o.pdf       |
    | 440_table__o.html              | 440_table__o.pdf            |
    | 450_figures__o.html            | 450_figures__o.pdf          |
    | 460_examples__o.html           | 460_examples__o.pdf         |
    | 470_code_listings__o.html      | 470_code_listings__o.pdf    |
    | 480_ordered_lists__o.html      | 480_ordered_lists__o.pdf    |
    | 490_itemized_lists__o.html     | 490_itemized_lists__o.pdf   |
    | 4A0_definition_lists__o.html   | 4A0_definition_lists__o.pdf |
    | 4B0_blockquotes__o.html        | 4B0_blockquotes__o.pdf      |
    | 4C0_equations__o.html          | 4C0_equations__o.pdf        |
    | 500_styling__o.html            | 500_styling__o.pdf          |
    | 510_code_highlight__o.html     | 510_code_highlight__o.pdf   |
    | 991_alice__o.html              | 991_alice__o.pdf            |
    # | 992_complete__o.html           | 992_complete__o.pdf         |
