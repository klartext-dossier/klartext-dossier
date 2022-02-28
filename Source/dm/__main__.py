import argparse, logging, os, sys

import dm.context, dm.run


""" USER MESSAGES

    The log levels are used for messages of the following kind:

    Error       Conditions that stop the tool from generating its required output.
    Warn        Conditions that might cause the generated output to be insufficient.
    Info        Confirmations of the expected execution of the tool.
    Debug       Information useful for debugging the tool. Not intended for the end user.

    The return codes have the following meaning:

    0           The tool worked without error, the result is positive.
    -1          The tool worked without error, the result is negative
    -2          The tool encountered an error.
"""


def configure_logging(log_level):

    """ Setup the logging mechanism with the specified log level.    
    """

    numeric_level = logging.ERROR
    if log_level:
        numeric_level = getattr(logging, log_level.upper(), None)
        if not isinstance(numeric_level, int):
            numeric_level = logging.ERROR

    logging.basicConfig(format='{asctime} | {levelname:1.1} | {message}', level=numeric_level, style='{')

    # discourage libraries to log
    for key in logging.Logger.manager.loggerDict:
        logging.getLogger(key).setLevel(logging.CRITICAL)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(prog='dm', description='Dossier Management tool.')
    parser.add_argument('--log', choices=['debug', 'info', 'warn', 'error'], help='Log level.')
    parser.add_argument('--tools', default=os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'Tools')), help='Path to the tools directory.')

    subparsers = parser.add_subparsers()
    dm.run.add_subparser(subparsers)
    
    args = parser.parse_args()

    configure_logging(args.log)

    initial_context = dm.context.Context(tools_dir=args.tools)

    if 'func' in args:
        try:
            retval = args.func(args, initial_context)
            exit(retval)
        except Exception as e:
            logging.error(f'Execution of command "{args.command_name}" failed')
            logging.debug(e, exc_info=e)
            exit(-2)
    else:
        parser.print_help()
        exit(-1)
