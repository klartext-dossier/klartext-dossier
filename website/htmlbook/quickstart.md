# Quickstart

## Using the css stylesheet

To use the css version of the `htmlbook-css` stylesheet, simply link to it in a html file:

``` html
<html xmlns="http://www.w3.org/1999/xhtml">

    <head>
        <link rel="stylesheet" type="text/css" href="htmlbook.css"/>
    </head>

    <body data-type="book">

        [ ... ]
    
    </body>

</html>
```

## Using the less stylesheet

To use the less version of the `htmlbook-css` stylesheet, there a different options:

1. Convert the less version to css

    Simply run

    ``` bash
    lessc htmlbook.less htmlbook.css
    ```

    to convert the less stylestheet to css. Than use it as described above.

2. Use it with the less javascript library

    ``` html
    <html xmlns="http://www.w3.org/1999/xhtml">

        <head>
            <link rel="stylesheet/less" type="text/css" href="htmlbook.less"/>
            <script src="https://cdn.jsdelivr.net/npm/less"/>        
        </head>

        <body data-type="book">

            [ ... ]
        
        </body>

    </html>
    ```

3. Directly include it in a [dm](../dm/index.md) pipeline:

    ``` klartext
    pipeline:

        include:
            input: "document.xhtml"

        xhtml-to-pdf:
            stylesheet: "htmlbook.less"
            output: "document.pdf"    
    ```
