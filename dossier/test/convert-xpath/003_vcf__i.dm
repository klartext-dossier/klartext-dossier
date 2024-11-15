pipeline:

    xml-transform:
        input: "003_vcf__i.xml"
        stylesheet: "003_vcf__i.xslt"

    save:
        output: "003_vcf__o.test.txt"
