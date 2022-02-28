import logging

from dm.tasks.Task import Task
from dm.tasks.TaskFactory import TaskFactory


# TODO: Move to a better place!
def evaluate(test, context):
    if test.startswith('!'):
        return test[1:] not in context.flags()
    else:
        return test in context.flags()


class IfTask(Task):

    """ The if task.

        This task executes all child tasks when a condition flag is set.
    """

    def __init__(self, element, tag_name):
        super().__init__(element, tag_name)
        self.test = self.getAttribute('test', default='')

    def run(self, context):
        if evaluate(self.test, context):
            logging.debug(f'{self.name} - condition "{self.test}" is True')
            for child in self.element.iterchildren():
                task = TaskFactory.createTask(child, child.tag)
                task.content = self.content
                task.run(context)
                self.content = task.content
        else:
            logging.debug(f'{self.name} - condition "{self.test}" is False')