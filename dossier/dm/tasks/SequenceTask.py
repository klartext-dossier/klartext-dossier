from dm.tasks.Task import Task
from dm.tasks.TaskFactory import TaskFactory


class SequenceTask(Task):

    """ The sequence task.

        This task executes all child tasks in sequence.

        This task is also used to execute a pipeline as a whole.
    """

    def __init__(self, element, tag_name):
        super().__init__(element, tag_name)
        self.checkAllowedAttributes(element, ['name'])
        self.checkAllowedElements(element, TaskFactory.TASKS.keys())

    def run(self, context):
        for child in self.element.iterchildren():
            task = TaskFactory.createTask(child, child.tag)
            task.content = self.content
            task.run(context)
            self.content = task.content

        return 0