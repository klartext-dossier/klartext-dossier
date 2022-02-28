presentation: title="Dossier" subtitle="A new approach to technical documentation" author="Matthias Hölzer-Klüpfel"

    section: title="Motivation"

        slide: title="Unstructured Text" master="image"

            img: src="image-calligraphy.jpg"

        slide: title="Unstructured Text Examples" master="text"
            
            - Examples
                - Prose (novels, poems, ...)
            - Trends    
                - moves towards more structure (single-source publishing)

        slide: title="Structured Text" master="text"
        
            - Examples
                - Data collections (dictionaries, phone books, ...)
            - Trends
                - stored in databases

        slide: title="Semi-Structured Text" master="text"

            - Examples
                - Technical documents (standards, specifications, ...)
            - Trends
                - are a real challenge...


    section: title="Challenges - semi-structured text"

        slide: title="Challenges" master="text"

            consistency     
            :   do it the same way all the time

            flexibility
            :   allow for deviations from the norm

            maintainability
            :   ensure changes are safe and simple

            scalability
            :   make it work with large amounts of text

        slide: title="Content Management Systems" master="image"
            
            img: src="image-wordpress-cms.jpg"

        slide: title="Markup Languages" master="text"

            "A system for annotating a document in a way that is distinguishable from the content."

            Procedural Markup Languages - describe text processing

            - troff
            - TeX

            Descriptive Markup Languages - describe text content
            
            - SGML
            - XML?

            Hybrid Markup Languages - describe content and presentation

            - LaTeX
            - HTML
            - Markdown?

        slide: title="Wishlist" master="text"

            Ideally, a text processing system for semi-structured text would:

            - provide a structured way to express the structured parts
            - provide a simple notation for the unstructured parts
            - use an (extensible) schema to ensure correct syntax
            - be easy to write, read and process
            - separate content from the presentation
            - provide flexible output formats


    section: title="Klartext - markup language"

        slide: title="What is Pythonic?" master="text"

            **Pythonic** is an adjective that describes an approach to computer programming that agrees with the founding philosophy of the Python programming language. 

            Python philosophy of writing code:

            - **Beautiful** is better than ugly
            - **Explicit** is better than implicit
            - **Simple** is better than complex
            - **Complex** is better than complicated
            - **Flat** is better than nested
            - **Sparse** is better than dense
            - **Readability** counts

        slide: title="Traditional vs. Python" master="text"

            ---            
            ``` c++ 
            #include <iostream>

            int main (int argc, char **argv)
            {
                for (int i; i<argc; ++i)
                {
                    std::cout << argv[i] << std::endl;
                }
            }
            ```
            ``` python 
            import sys

            for arg in sys.argv:
                print(arg)
            ```

        slide: title="Traditional XML" master="text"

            ``` xml
            <task id="task-define-sdlc" name="Define Software Development Life Cycle" scope="project-start">
                <description>
                    <xhtml:p>
                        Define the <g ref="glossary-sdlc">Software Development Life Cycle</g> for 
                        the development project.
                    </xhtml:p>
                    <xhtml:p>
                        This includes:
                    </xhtml:p>
                    <xhtml:ul>
                        <xhtml:li>
                            referencing <g ref="glossary-SOP">standard operating procedures</g> 
                            relevant to the development project
                        </xhtml:li>
                        <xhtml:li>
                            defining <g ref="glossary-activity">activities</g> and <g ref="task">tasks</g> 
                            to be performed
                        </xhtml:li>
                        <xhtml:li>
                            documenting and justifying any deviations from the 
                            <g ref="glossary-SOP">standard operating procedures</g> (i.e. process tailoring)
                        </xhtml:li>
                    </xhtml:ul>
                </description>
                <responsible ref="project-manager"/>
                <output ref="software-development-plan"/>
            </task>
            ```

        slide: title="Pythonic XML" master="text"

            ``` klartext
            // This is a task definition

            task: #task-define-sdlc name="Define Software Development Life Cycle" scope="project-start"
                
                description:
                    Define the {software development life cycle} for the development project.

                    This includes:
                
                    - **referencing** {standard operating procedures} relevant to the development project
                    - **defining** {activities} and {tasks} to be performed
                    - **documenting** and justifying any deviations from the {standard operating procedures} 
                      (i.e. process tailoring)

                responsible> project-manager 
                output> software-development-plan
            ```

        slide: title="Structure" master="text"
        
            - content structure is expressed with simplified tags
            - nesting is replaced by indentation

            ``` klartext
            tag: #ID attribute="value"

                subtag: another-attribute="value"

                    level-three:

                subtag: another-attribute="value2"
            ```
            ``` xml
            <tag id="ID" attribute="value">

                <subtag another-attribute="value">
            
                    <level-three/>
            
                </subtag>
            
                <subtag another-atribute="value2"/>
            
            </tag>
            ```

        slide: title="Free Text" master="text"
        
            - text content is using the Markdown syntax
            
            ``` klartext
            tag:

                This is **normal** Markdown text:

                - list entry
            ```
            ``` xml
            <tag>
                
                <p>
                    This is <b>normal</b> Markdown text:

                    <ul>

                        <li>list entry</li>

                    </ul>

                </p>

            </tag>
            ```

        slide: title="Inline Tags" master="text"

            - inline tags have another simplified form

            ``` klartext
            This is /q/quoted/ text.
            ```
            ``` xml
            <p>
                This is <q>quoted</q> text.
            </p>
            ```
        
        slide: title="Glossary Entries" master="text"

            - glossary entries are enclosed in curly braces:

            ``` klartext
            This is a {glossary entry}.
            ```
            ``` xml
            <p>
                This is a <g>glossary entry</g>.
            </p>
            ```
        
        slide: title="Links" master="text"

            - references to other elements have a shortcut syntax:

            ``` klartext
            tag: #ID1
                link> ID2

            tag: #ID2
                link: ref="#ID2"
            ```
            ``` xml
            <tag id="ID1">

                <link ref="ID2"/>

            </tag>

            <tag id="ID2">

                <link ref="ID2"/>

            </tag>
            ```

        slide: title="Directives" master="text"

            - directives can be used for including files:

            ``` klartext
            #include "file.kt"
            ```

            - or for using namespaces:

            ``` klartext
            #import "http://hoelzer-kluepfel.de/dossier" as dm

            dm::tag: 
            ```
            ``` xml
            <tag xmlns="http://hoelzer-kluepfel.de/dossier"/>
            ```
        

    section: title="Med-Core - content framework"
        
        slide: title="Content Framework" master="text"

            Typical aspects that need to be covered in all text processing projects:

            - maintaining a glossary of defined terms
            - refering to literature like standards and norms
            - transforming structured content into human-readable documents
            - styling the documents to be visually appealing

            One approach is to set up a content framework: MedCore

        slide: title="Glossary" master="text"

            Structure for defining glossary entries:

            ``` klartext
            entry:
                term: "Activity"
                term: "Activities"
            
                definition:
                    A set of one or more interrelated or interacting {tasks}.
                    
                    origin> reference-iec-62304 section="3.1"
            ```

        slide: title="References" master="text"
        
            Structure for defining literature:
            
            ``` klartext
            reference: #reference-iec-62304 name="IEC 62304"

                title:   "Medical device software - Software life cycle processes"
                version: "2006+AMD1:2015"
                edition: "1.1"

                description:
                    Defines the life cycle requirements for medical device software. 
                    The set of processes, activities, and tasks described in this standard 
                    establishes a common framework for medical device software life cycle 
                    processes. Applies to the development and maintenance of medical device 
                    software when software is itself a medical device or when software is an
                    embedded or integral part of the final medical device. This standard does 
                    not cover validation and final release of the medical device, even when 
                    the medical device consists entirely of software.
            ```

        slide: title="Content" master="text"

            Content can follow any schema, using the defined elements:

            ``` klartext
            task: #task-define-sdlc name="Define Software Development Life Cycle" scope="project-start"

                description:
                    Define the {software development life cycle} for the development project.

                    This includes:
                
                    - referencing {standard operating procedures} relevant to the development project
                    - defining {activities} and {tasks} to be performed
                    - documenting and justifying any deviations from the {standard operating procedures} 
                      (i.e. process tailoring)

                responsible> project-manager 
                output> software-development-plan
            ```

        slide: title="Transformation" master="text"

            Transforming the content into a document is a multi-stage process:

            img: src="image-xml-processing.png"

        slide: title="Conversion Pipeline" master="text"

            The transformation can be defined via a pipeline:

            ``` klartext
            pipeline:

                include:
                    input: "Content.kt"
                    input: "med-core/glossary_en.kt"
                    input: "med-core/bibliography_en.kt"
                    
                xml-transform:
                    stylesheet: "transform.xslt"
                    stylesheet: "med-core/glossary.xslt"
                    stylesheet: "med-core/bibliography.xslt"
                    stylesheet: "unique-ids.xslt"
                    stylesheet: "table-of-contents.xslt"
                                    
                xhtml-to-pdf:
                    stylesheet: "htmlbook.css"
                    output: "Document.pdf"            
            ```


    section: title="Dossier Management - processing tool"

        slide: title="Features" master="text"

            "dm" is a tool to convert documents. Some of its features:

            - multiple input formats (klartext, HTML, XML, Markdown)
            - multiple output formats (PDF, HTML, XML, docx)
            - extensible structure
            - flexible text encodings
        
        slide: title="Commands" master="text"

            ```
            $ dm --help

            usage: dm [-h] [--log {debug,info,warn,error}] {convert,init,pretty,compare,check,run} ...

            Dossier Management tool.

            positional arguments: {convert,init,pretty,compare,check,run}

                convert                     Convert files to another format.
                init                        Initialize folders and documents.
                pretty                      Pretty print the input file.
                compare                     Compare the content of documents.
                check                       Check the input file for correctness.
                run                         Execute conversion pipelines.

            optional arguments:
            -h, --help                      show this help message and exit
            --log {debug,info,warn,error}   Log level.
            ```
        
        slide: title="Pipelines" master="text"

            Pipelines can be used to configure custom-made conversion scenarios:

            ``` klartext
            pipeline:

                include:
                    input: "Content.kt"
                    input: "med-core/glossary_en.kt"
                    input: "med-core/bibliography_en.kt"
                    
                xml-transform:
                    stylesheet: "transform.xslt"
                    stylesheet: "med-core/glossary.xslt"
                    stylesheet: "med-core/bibliography.xslt"
                    stylesheet: "unique-ids.xslt"
                    stylesheet: "table-of-contents.xslt"
                                    
                xhtml-to-pdf:
                    stylesheet: "htmlbook.css"
                    output: "Document.pdf"            
            ```

        slide: title="Tasks" master="text"

            |                   |                                           |
            | ----------------- | ----------------------------------------- |
            | code-highlight    | Adds syntax highlighting to code sections |
            | copy              | Copies a file, incl. encoding conversion  |
            | dump              | Displays the content of a document        |
            | file              | Creates a document in place               |
            | include           | Includes several files into a document    |
            | klartext-to-xml   | Converts klartext to XML                  |
            | load              | Creates a document by loading a file      |
            | markdown-include  | Processes include directives in .md files |
            | markdown-to-xhtml | Converts a markdown document to XHTML     |
            | save              | Saves a document to a file                |
            | xhtml-to-docx     | Converts an XHTML file to docx            |
            | xhtml-to-pdf      | converts XHTML to PDF with CSS stylesheet |
            | xml-tidy          | Pretty-prints an XML file                 |
            | xml-transform     | Transforms XML with XSLT transformations  |
            | xml-validate      | Validates XML against XSD schema files    |

    
    // section: title="Examples - Process Descriptions"

    //     slide: title="Process Descriptions" master="text"

    section: title="Examples - Medical SPICE"

        slide: title="Medical SPICE Blatt 1 - Source" master="text"

            ``` klartext
            process: #SD5 tag="SD.5" name="Software Detailed Design"

                purpose:
                    The objective of the /r.q/SD5/ {process} is to refine the {software items} and interfaces defined in 
                    the software architecture to create {software units} and their interfaces.

                    Detailed design specifies algorithms, data representations, interfaces among different 
                    {software units}, and interfaces between {software units} and data structures.
                    
                    It is necessary to document the design of each {software unit} and its interface so that the 
                    {software unit} can be implemented correctly.

                outcomes:
                    outcome: #SD5_OC1 The software architecture is refined until it is represented by {software units} 
                             that can be implemented and tested separately.
                    outcome: #SD5_OC2 Each {software unit} is designed.
                    outcome: #SD5_OC4 The interfaces between {software units} and external components as well as in 
                             between {software units} are defined.            
                    outcome: #SD5_OC5 The software detailed design is verified.

                base-practices:

                    base-practice: #SD5_BP1 tag="SD.5_BP.1" name="Subdivide Software into Software Units"

                        description:
                            Subdivide the software until it is represented by {software units}.

                            !!! note "Note"
                                Although {software units} are often thought of as being a single function or module, this 
                                view is not always appropriate. A {software unit} is defined to be a {software item} that 
                                is not subdivided into smaller items and can be tested separately.

                        outcome> SD5_OC1
                        reference> reference-iec-62304 section="5.4.1" class="B,C"
                        reference> reference-iec-60601-1 section="14.8"            
            ```

        slide: title="Medical SPICE Blatt 1 - Result" master="image"

            img: src="image-medical-spice.png"


    section: title="Examples - This Presentation"

        slide: title="This Presentation - Source" master="text"

            ``` klartext
            presentation: title="Dossier" subtitle="A new approach to technical documentation"

                section: title="Examples - This Presentation"

                    slide: title="This Presentation - Result" master="text"

                        You are looking at it!
            ```
    
        slide: title="This Presentation - Result" master="text"

            You are looking at it!

    section: title="Outlook - Documentation as Code"

        slide: title="Workflow" master="image"

            img: src="image-workflow.png"

        slide: title="Pull Requests" master="image"

            img: src="image-pull-request.png"

        slide: title="Dev Ops Pipeline" master="image"

            img: src="image-dev-ops-pipeline.png"

        slide: title="Contact Data" master="contact"

            Matthias Hölzer-Klüpfel
            Landsteinerstraße 4
            97074 Würzburg
            Germany

            +49 176 6085 7994

            [matthias@hoelzer-kluepfel.de](mailto:matthias@hoelzer-kluepfel.de)
            [https://www.hoelzer-kluepfel.de](https://www.hoelzer-kluepfel.de)
