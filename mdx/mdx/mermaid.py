''' Module providing the mermaid generator for the customblocks extension for Markdown.
'''

import tempfile, subprocess
from importlib.resources import files


def mermaid_generator(ctx, width: str='auto', scale: int=5, background: str='transparent') -> str:

    """ Mermaid generator.

        Renders a mermaid diagram into a PNG and includes the image.
    """

    # TODO: Make sure the file gets deleted!
    png = tempfile.NamedTemporaryFile(suffix='.png', mode="w+t", delete=False) 

    mm = tempfile.NamedTemporaryFile(suffix='.mm', mode="w+t")
    mm.write(ctx.content)
    mm.seek(0)

    config = files('mdx').joinpath('puppeteer-config.json')

    subprocess.run(["mmdc", "-q", "-p", config, "-i", mm.name, "-o", png.name, '-s', str(scale), '-b', background]) # type: ignore[list-item]

    return f'<img style="width:{width}" src="{png.name}"/>'