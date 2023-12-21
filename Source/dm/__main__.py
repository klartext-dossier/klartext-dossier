import argparse, logging, os.path, sys

import dm.context, dm.run_command


RETVAL_POSITIVE : int =  0  # The tool worked without error, the result is positive
RETVAL_NEGATIVE : int = -1  # The tool worked without error, the result is negative
RETVAL_ERROR    : int = -2  # The tool encountered an error.


def configure_app_logging(log_level: str):

    level = getattr(logging, log_level.upper(), None)
    if not isinstance(level, int):
        level = logging.ERROR

    logging.basicConfig(format='{asctime} | {levelname:1.1} | {message}', level=level, style='{')


def configure_library_logging(log_level: int):
    for key in logging.Logger.manager.loggerDict:
        logging.getLogger(key).setLevel(log_level)


def create_cmd_parser():
    parser = argparse.ArgumentParser(prog='dm', description='Dossier Management tool.')
    parser.add_argument('--log', choices=['debug', 'info', 'warn', 'error'], help='Log level.')
    parser.add_argument('--tools', default=os.path.abspath(os.path.join(os.path.dirname(sys.argv[0]), 'Tools')), help='Path to the tools directory.')

    subparsers = parser.add_subparsers()
    dm.run_command.add_subparser(subparsers)
    
    return parser


if __name__ == '__main__':

    parser = create_cmd_parser()
    args = parser.parse_args()

    if not 'func' in args:
        parser.print_help()
        exit(RETVAL_NEGATIVE)

    configure_app_logging(args.log)
    configure_library_logging(logging.CRITICAL)

    initial_context = dm.context.Context(tools_dir=args.tools)

    try:
        retval = args.func(args, initial_context)
        exit(RETVAL_POSITIVE)
    except Exception as e:
        logging.error(f'Execution of command "{args.command_name}" failed')
        logging.debug(e, exc_info=e)
        exit(RETVAL_ERROR)

