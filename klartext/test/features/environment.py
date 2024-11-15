import tempfile
import logging


def before_scenario(context, feature):
    logging.disable(logging.INFO)
    context.xml = None
    

def after_scenario(context, feature):
    context.xml = None
