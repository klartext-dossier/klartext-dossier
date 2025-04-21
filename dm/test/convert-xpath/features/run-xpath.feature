Feature: Tests for custom xpath extensions

Scenario: Testing the upper-case, lower-case and sentence-case functions

    When running the pipeline 001_case__i.dm
    Then the file 001_case__o.test.xml is equal to 001_case__o.xml

Scenario: Testing the vcf functions

    When running the pipeline 002_vcf__i.dm
    Then the file 002_vcf__o.test.txt is equal to 002_vcf__o.txt

    When running the pipeline 002_vcf__i.dm
    Then the file 003_vcf__o.test.txt is equal to 003_vcf__o.txt
