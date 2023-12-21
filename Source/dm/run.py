import argparse, logging

from dm.utilities import tryLocatingToolsFile
import dm.pipeline


def add_subparser(parsers):

    parser = parsers.add_parser('run', help='Execute conversion pipelines.')
    parser.add_argument('-p', '--pipeline', help='The pipeline file to run.', required=True)
    parser.add_argument('-i', '--input', help='Input file provided to the pipeline. Use - for <stdin>.', required=False, type=argparse.FileType('rb'))
    parser.add_argument('--input-encoding', default='utf-8', help='The encoding of the input file.')
    parser.add_argument('-o', '--output', help='Output file generated by the pipeline. Use - for <stdout>.', required=False, type=argparse.FileType('wb'))
    parser.add_argument('--output-encoding', default=None, help='The encoding of the output file.')
    parser.add_argument('--set', help='Flags to be set (e.g., validate or dump)', required=False)

    parser.set_defaults(command_name='run', func=cmd_run)


def cmd_run(args, context):

    if args.set:
        flags = []
        for flag in args.set.split(','):
            flags.append(flag.strip())
        context.set_flags(flags)
    
    try:        
        pipeline_file = tryLocatingToolsFile(args.pipeline, 'pipeline', context.tools_dir())
        logging.info(f'Execute conversion pipeline "{pipeline_file}"')
        with open(pipeline_file, 'r', encoding="utf-8") as pipe:
            pipeline = dm.pipeline.Pipeline(pipe)
            pipeline.run(args.input, args.input_encoding, args.output, args.output_encoding, context)
        return 0
    except Exception as e:
        for arg in e.args:
            logging.error(arg)
        logging.error(f'Could not run pipeline "{args.pipeline}"')
        raise

