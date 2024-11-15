Feature: Test converting klartext

Scenario Outline: Converting klartext

    When converting the <INPUT FILE> to XML
    Then the XML output is equal to <XML FILE>

Examples: Input files

    | INPUT FILE                   | XML FILE                       | 
                                                                      
    | 000_empty_file__i.kt         | 000_empty_file__o.xml          | 
    | 001_simple_text__i.kt        | 001_simple_text__o.xml         | 
    | 002_simple_tag__i.kt         | 002_simple_tag__o.xml          | 
    | 003_nested_tags__i.kt        | 003_nested_tags__o.xml         | 
    | 004_attributes__i.kt         | 004_attributes__o.xml          |
    | 005_links__i.kt              | 005_links__o.xml               |
    | 006_inline_content__i.kt     | 006_inline_content__o.xml      |
    | 007_empty_tag__i.kt          | 007_empty_tag__o.xml           |
    | 009_verbatim__i.kt           | 009_verbatim__o.xml            |
    | 010_nested_links__i.kt       | 010_nested_links__o.xml        |
    | 011_include__i.kt            | 011_include__o.xml             |
    | 013_import__i.kt             | 013_import__o.xml              |
    
