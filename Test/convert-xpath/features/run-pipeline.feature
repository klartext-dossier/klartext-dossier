Feature: Tests for custom xpath extensions

Scenario: Testing the upper-case, lower-case and sentence-case functions

    When running the pipeline 001_case__i.dm
    Then the file 001_case__o.test.xml is equal to 001_case__o.xml
