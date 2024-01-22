import tempfile, subprocess

from dm.utilities import tryLocatingToolsFile, guessToolsDir


def mermaid_generator(ctx, width='auto', scale=5, background='transparent'):

    """ Mermaid generator.

        Renders a mermaid diagram into a PNG and includes the image.

        TODO: Cleanup the temporary files!
    """

    png = tempfile.NamedTemporaryFile(suffix='.png', mode="w+t", delete=False)

    mm = tempfile.NamedTemporaryFile(suffix='.mm', mode="w+t", delete=False)
    mm.write(ctx.content)
    mm.seek(0)

    config = tryLocatingToolsFile('puppeteer-config.json', 'json', guessToolsDir())

    subprocess.run(["mmdc", "-q", "-p", config, "-i", mm.name, "-o", png.name, '-s', str(scale), '-b', background])

    return f'<img style="width:{width}" src="{png.name}"/>'