from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        self._play_context.ssh_args = ''
        result = self._execute_module('ping', task_vars=task_vars)
        return result
