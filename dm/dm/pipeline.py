""" Module providing the pipeline functionality.
"""

import logging
from io import TextIOWrapper, BytesIO

from lxml import etree
from klartext import Parser

from dm.tasks.SequenceTask import SequenceTask
from dm.utilities import tryLocatingFile
from dm.context import Context
from dm.tasks import Task


class Pipeline:

    """ The pipeline.
    """

    def __init__(self, pipeline : TextIOWrapper) -> None:

        """ Initializer.
            
            Args:
                pipeline: The pipeline input file.
        """

        self.pipeline : TextIOWrapper = pipeline


    def tryParsingPipeline(self, context : Context) -> etree._Element:

        """ Tries to parse the pipeline file.

            Args:
                context: the context used to evaluate the pipeline

            Returns:
                The pipeline definition as an XML structure

            Raises:
                TaskException: when the pipeline input file can not be parsed.
        """

        parser = Parser()
        inp = parser.parse(self.pipeline, basedir=context.basedir(), lookup=tryLocatingFile)
        return etree.fromstring(inp)


    def run(self, input: BytesIO, input_encoding: str, output: BytesIO, output_encoding: str, context: Context) -> Task:
        
        """ Executes the pipeline tasks.

            Args:
                input:           the input stream for the pipeline
                input_encoding:  the encoding of the input
                output:          the output stream for the pipeline
                output_encoding: the encoding of the output
                context:         the execution context

            Returns:
                The task object used to execute the pipeline.

            Raises:
                TaskException: when the pipeline input file can not be parsed.
        """

        with context:
            if self.pipeline.name:
                context.set_filename(self.pipeline.name)

            pipeline_xml = self.tryParsingPipeline(context)
            task = SequenceTask(pipeline_xml, 'pipeline')

            if input is not None:
                task.content.data = BytesIO(input.read())
                task.content.encoding = input_encoding

            task.run(context)

            if output is not None:
                logging.info(f'Writing output file "{output.name}"')
                # TODO: convert to output encoding!
                output.write(task.content.data.getvalue())
        
            return task
