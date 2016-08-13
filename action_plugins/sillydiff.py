from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        # If there's no change, Ansible assumes there can be no diff
        return {'changed': True, 'diff': { 'before': 'foo\nbar', 'after': 'bar' } }
