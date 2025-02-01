import logging, os, subprocess, tempfile

from weasyprint import HTML, CSS, default_url_fetcher
from weasyprint.text.fonts import FontConfiguration

from dm.exceptions import TaskException
from dm.utilities import tryLocatingToolsFile
from dm.tasks.Task import Task
from dm.tasks.IfTask import evaluate


class PDFTask(Task):

    """ The xhtml-to-pdf task.

        This task converts an XHTML file to PDF with a CSS stylesheet transformation.
    """   

    def url_fetcher(self, url):
        if url.startswith('file:') and url.endswith('.css'):
            if len(self.stylesheets) > 0:
                logging.debug(f'{self.name} - ignoring "{url}", as external stylesheets are used')
                # fetch an empty dummy stylesheet, as url_fetcher needs to return something
                url = 'none.css'
            else:
                # only log in the 'else' clause, as we want to hide the dummy stylesheet
                logging.info(f'{self.name} - looking up "{url}"')
            try:
                css_file = tryLocatingToolsFile(os.path.basename(url), 'css', self.toolsdir)
                return dict(filename=css_file, file_obj=open(css_file, 'rb'), mime_type='text/css', encoding='UTF-8')
            except:
                pass
        return default_url_fetcher(url)

    def tryConvertingLessFile(self, context, stylesheet, attributes):
        tmpfile = tempfile.NamedTemporaryFile(suffix='.css')
        context.add_tempfile(tmpfile.name, tmpfile)
        logging.info(f'{self.name} - converting "{stylesheet}" to "{tmpfile.name}"')
        cmd = ["lessc", f"--include-path=.:{context.toolsdir()}/less:{context.toolsdir()}/css:"]
        if attributes:
            for key, value in list(attributes.items()):
                if 'test' != key:
                    cmd.append(f"--modify-var={key}={value}")
        cmd.append(stylesheet)
        cmd.append(tmpfile.name)
        logging.debug(f"command: {cmd}")
        subprocess.run(cmd)
        return tmpfile.name
    
    def locateStylesheet(self, context, stylesheet, attributes):
        if stylesheet.endswith('.css'):
            return tryLocatingToolsFile(stylesheet, 'css', context.toolsdir())
        elif stylesheet.endswith('.less'):
            less = tryLocatingToolsFile(stylesheet, 'less', context.toolsdir())
            return self.tryConvertingLessFile(context, less, attributes)
        raise TaskException(f'{self.name} - cannot locate stylesheet {stylesheet}')

    def tryLoadingStylesheets(self, context):
        csss = []
        font_config = FontConfiguration()
        for entry in self.stylesheets:
            stylesheet, attributes = entry
            test = attributes['test'] if 'test' in attributes else None
            filename = self.locateStylesheet(context, stylesheet, attributes)
            if test:
                if evaluate(test, context):
                    logging.info(f'{self.name} - applying stylesheet "{filename}" as {test} is True')
                    csss.append(CSS(filename=filename, font_config=font_config))
                else:
                    logging.info(f'{self.name} - skipping stylesheet "{filename}" as {test} is False')
            else:
                logging.info(f'{self.name} - applying stylesheet "{filename}"')
                csss.append(CSS(filename=filename, font_config=font_config))

        return (csss, font_config)

    def tryParsingXHTML(self):
        try:
            return HTML(file_obj=self.content.data, encoding=self.content.encoding, base_url=self.base_url, url_fetcher=self.url_fetcher)
        except Exception as e:
            raise TaskException(f'{self.name} - cannot parse XHTML content', e)

    def tryWritingPDF(self, html, csss, font_config):
        try:
            return html.write_pdf(stylesheets=csss, font_config=font_config, presentational_hints=self.presentational_hints)
        except Exception as e:
            raise TaskException(f'{self.name} - cannot write PDF', e)

    def getStylesheetInfo(self):
        self.checkNumberOfElements('stylesheet', required=False, multiple=True)
        info = []
        for child in self.element.findall('stylesheet'):
            info.append((child.text.strip(), child.attrib))
        return info
    
    def run(self, context):
        self.toolsdir = None
        self.presentational_hints = 'true' == self.getAttribute('presentational-hints', default='true').lower()
        self.stylesheets = self.getStylesheetInfo()
        self.base_url = self.getAttribute('base-url', default='.')

        self.load()
        self.toolsdir = context.toolsdir() # to pass to the url_fetcher
        (csss, font_config) = self.tryLoadingStylesheets(context)
        html = self.tryParsingXHTML()
        self.content.setData(self.tryWritingPDF(html, csss, font_config))
        self.save()
