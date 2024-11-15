pipeline:

    xml-transform:
        input: "002_vcf__i.xml"
        stylesheet: "002_vcf__i.xslt"

    save:
        output: "002_vcf__o.test.txt"
