# `code-highlight` task

The `code-highlight` task adds syntex highlighting to `<code>` tags.

!!! note
    The highlighting is done using the [Pygments](https://pygments.org) syntax highlighter.

## Task attributes

| Attribute name | Default value | Description                            |
| -------------- | ------------- | -------------------------------------- |
| name           | file          | The name of the task used for logging. |

## Task elements

| Element name | Multiplicity | Description                            |
| ------------ | ------------ | -------------------------------------- |
| input        | [1..n]       | The name of the input file.            |
| output       | [0..1]       | The name of the output file. Optional. |

Each `input` element can have the following attributes:

| Attribute name | Default value | Description                     |
| -------------- | ------------- | ------------------------------- |
| encoding       | utf-8         | The encoding of the input file. |

Each `output` element can have the following attributes:

| Attribute name | Default value | Description                      |
| -------------- | ------------- | -------------------------------- |
| encoding       | utf-8         | The encoding of the output file. |

## Task behaviour

The tasks looks for `<code>` tags in the input, which needs to be xhtml, and applies the pygments syntax highlighting on the code, if available.

If an `output` element is given, the result will be saved to a file with the given name.

## Example

=== "Pipeline"
    ``` klartext
    pipeline:

        load: 
            input: "code.html"

        code-highlight:
            output: "code-highlighted.html"    
    ```

=== "code.html"
    ``` html
    <html xmlns="http://www.w3.org/1999/xhtml" lang="en">

        <body>    
        <code class="language-cpp">
    #include &lt;iostream&gt;

    int main (int argc, char **argv)
    {
        for (int i; i&lt;argc; ++i)
        {
            std::cout &lt;&lt; argv[i] &lt;&lt; std::endl;
        }
    }
            </code>
        </body>

    </html>
    ```

will be converted to

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
