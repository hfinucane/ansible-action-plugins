from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        # Get the current context
        all_variables = self._templar.template('{{vars}}')
        # Set an arbitrary value- just to show that we can
        all_variables['foo'] = 'bar'
        return all_variables
