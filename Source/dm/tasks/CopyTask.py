from dm.tasks.Task import Task


class CopyTask(Task):

    """ The copy task.

        This task allows copying the content of a file, potentially performing
        an encoding conversion.
    """

    def run(self, context):
        self.load()
        self.save()
