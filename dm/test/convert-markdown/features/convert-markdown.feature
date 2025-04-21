Feature: Test converting markdown

Scenario Outline: Converting markdown to HTML and PDF

    When converting the <INPUT FILE> to html
    Then the html output is equal to <HTML FILE>

    When converting the <INPUT FILE> to PDF
    Then the PDF output is equal to <PDF FILE>

Examples: Input files

    | INPUT FILE                   | HTML FILE                      | PDF FILE                      | 
                                                                    
    | 000_empty_file__i.md         | 000_empty_file__o.html         | 000_empty_file__o.pdf         |   
    | 001_line_of_text__i.md       | 001_line_of_text__o.html       | 001_line_of_text__o.pdf       |
    | 002_nested_headings__i.md    | 002_nested_headings__o.html    | 002_nested_headings__o.pdf    |
    | 003_title_author__i.md       | 003_title_author__o.html       | 003_title_author__o.pdf       |
    | 004_simple_list__i.md        | 004_simple_list__o.html        | 004_simple_list__o.pdf        |
    | 005_nested_list__i.md        | 005_nested_list__o.html        | 005_nested_list__o.pdf        |
    | 006_simple_enumeration__i.md | 006_simple_enumeration__o.html | 006_simple_enumeration__o.pdf |
    | 007_nested_enumeration__i.md | 007_nested_enumeration__o.html | 007_nested_enumeration__o.pdf |
    | 008_nested_mixed_lists__i.md | 008_nested_mixed_lists__o.html | 008_nested_mixed_lists__o.pdf |
    | 009_paragraphs__i.md         | 009_paragraphs__o.html         | 009_paragraphs__o.pdf         |
    | 010_blockquotes__i.md        | 010_blockquotes__o.html        | 010_blockquotes__o.pdf        |
    | 011_inline_styles__i.md      | 011_inline_styles__o.html      | 011_inline_styles__o.pdf      |
    | 012_inline_code__i.md        | 012_inline_code__o.html        | 012_inline_code__o.pdf        |
    | 013_code_section__i.md       | 013_code_section__o.html       | 013_code_section__o.pdf       |
    | 014_definition_list__i.md    | 014_definition_list__o.html    | 014_definition_list__o.pdf    |
    | 015_inline_link__i.md        | 015_inline_link__o.html        | 015_inline_link__o.pdf        |
    | 016_table_of_contents__i.md  | 016_table_of_contents__o.html  | 016_table_of_contents__o.pdf  |
    | 017_inline_quotes__i.md      | 017_inline_quotes__o.html      | 017_inline_quotes__o.pdf      |
    | 018_checklists__i.md         | 018_checklists__o.html         | 018_checklists__o.pdf         |
    | 019_comments__i.md           | 019_comments__o.html           | 019_comments__o.pdf           |
    | 020_note__i.md               | 020_note__o.html               | 020_note__o.pdf               |
    | 021_symbols__i.md            | 021_symbols__o.html            | 021_symbols__o.pdf            |
    | 022_highlighting__i.md       | 022_highlighting__o.html       | 022_highlighting__o.pdf       |
    | 023_parts__i.md              | 023_parts__o.html              | 023_parts__o.pdf              |
    | 024_preface__i.md            | 024_preface__o.html            | 024_preface__o.pdf            |
    | 025_frontmatter__i.md        | 025_frontmatter__o.html        | 025_frontmatter__o.pdf        |
    | 026_backmatter__i.md         | 026_backmatter__o.html         | 026_backmatter__o.pdf         |
    | 027_bibliography__i.md       | 027_bibliography__o.html       | 027_bibliography__o.pdf       |
    | 028_full_structure__i.md     | 028_full_structure__o.html     | 028_full_structure__o.pdf     |
    | 029_glossary__i.md           | 029_glossary__o.html           | 029_glossary__o.pdf           |
    | 030_sidebar__i.md            | 030_sidebar__o.html            | 030_sidebar__o.pdf            |
    | 031_inline_tags__i.md        | 031_inline_tags__o.html        | 031_inline_tags__o.pdf        |
    | 990_example_text__i.md       | 990_example_text__o.html       | 990_example_text__o.pdf       |
    | 999_showcase__i.md           | 999_showcase__o.html           | 999_showcase__o.pdf           |


Scenario Outline: Converting markdown to PDF

    When converting the <INPUT FILE> to PDF
    Then the PDF output is equal to <PDF FILE>

Examples: Input files

    | INPUT FILE         | PDF FILE            | 
                                                                    
    | 032_diagrams__i.md | 032_diagrams__o.pdf |
