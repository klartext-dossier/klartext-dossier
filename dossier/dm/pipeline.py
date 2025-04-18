import logging, io

from lxml import etree
from klartext import Parser

from dm.tasks.SequenceTask import SequenceTask
from dm.utilities import tryLocatingFile

class Pipeline:

    def __init__(self, pipeline):

        self.pipeline = pipeline


    def tryParsingPipeline(self, context):

        parser = Parser()
        inp = parser.parse(self.pipeline, basedir=context.basedir(), lookup=tryLocatingFile)
        return etree.fromstring(inp)


    def run(self, input, input_encoding, output, output_encoding, context):
        
        with context:
            if self.pipeline.name:
                context.set_filename(self.pipeline.name)

            pipeline_xml = self.tryParsingPipeline(context)
            task = SequenceTask(pipeline_xml, 'pipeline')

            if input is not None:
                task.content.data = io.BytesIO(input.read())
                task.content.encoding = input_encoding

            task.run(context)

            if output is not None:
                logging.info(f'Writing output file "{output.name}"')
                # TODO: convert to output encoding!
                output.write(task.content.data.getvalue())
        
            return task
