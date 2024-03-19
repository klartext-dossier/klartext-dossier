import logging, zipfile, tempfile

import pypdfium2 as pdfium

from dm.exceptions import TaskException
from dm.tasks.Task import Task


class PDFiumTask(Task):

    """ The pdf-to-png task.

        This task converts a PDF file to a set of images.
    """   

    def tryConvertingToPNG(self):
        try:
            tmp = tempfile.NamedTemporaryFile('w+b', suffix='.zip')

            with zipfile.ZipFile(tmp, 'w') as zipf:

                logging.info(f'{self.name} - Converting PDF to PNG')

                pdf = pdfium.PdfDocument(self.content.data)
             
                page_nr = 0
                for page in pdf:
                    filename = self.pattern % str(page_nr+1)

                    image = page.render(scale = self.dpi/72).to_pil()

                    if self.single:
                        logging.info(f'{self.name} - Saving PDF page {page_nr} to "{filename}"')                   
                        with open(filename, 'w+b') as outfile:
                            image.save(outfile, 'PNG')
                            zipf.write(filename, filename)
                    else:
                        with tempfile.NamedTemporaryFile('w+b', suffix='.png') as outfile:
                            image.save(outfile, 'PNG')
                            zipf.write(outfile.name, filename)

                    page_nr += 1
                    image.close()

            tmp.seek(0)
            return tmp.read()

        except Exception as e:
            raise TaskException(f'{self.name} - cannot write PNG', e)

    def run(self, context):
        self.load()

        self.pattern = self.getAttribute('pattern', default='page-%s.png')
        self.dpi = int(self.getAttribute('dpi', default='300'))
        self.single = 'true' == self.getAttribute('single', default='false').lower()

        zip = self.tryConvertingToPNG()   
        self.content.setData(zip)

        self.save()
