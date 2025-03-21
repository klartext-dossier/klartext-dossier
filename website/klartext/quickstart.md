# Quickstart

## A simple klartext document

Klartext documents are plain text files. The following example shows a very simple klartext document:

``` klartext linenums="1" title="Simple klartext document"
process: #SD.2 name="Software Development Planning"

    purpose:
        The _objective_ of the "Software Development Planning" process is to plan the software development tasks, communicate procedures and goals to members of the development team.

        Systematic software development planning ensures that risks caused by software are reduced and quality characteristics for the medical device software are met.
```

!!! note
    It is recommended to use the UTF-8 encoding for klartext files.

Semantically, this klartext file is equivalent to the following XML structure:

``` xml linenums="1" title="Equivalent XML file"
<process name="Software Development Planning" id="SD.2">

    <purpose>
        <p xmlns="http://www.w3.org/1999/xhtml">The <em>objective</em> of the &quot;Software Development Planning&quot; process is to plan the software development tasks, communicate procedures and goals to members of the development team.</p>        

        <p xmlns="http://www.w3.org/1999/xhtml">Systematic software development planning ensures that risks caused by software are reduced and quality characteristics for the medical device software are met.</p>
    </purpose>

</process>
```
