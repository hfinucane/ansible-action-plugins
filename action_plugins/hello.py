from ansible.plugins.action import ActionBase

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        return dict(msg="Hello World", _ansible_verbose_always=True)
