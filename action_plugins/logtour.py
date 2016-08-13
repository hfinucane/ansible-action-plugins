from ansible.plugins.action import ActionBase

try:
    from __main__ import display
except ImportError:
    from ansible.utils.display import Display
    display = Display()


class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        display.v("a log")
        display.vv("Kind of verbose")
        display.vvv("Verbose")
        display.vvvv("Lookout!")
        display.verbose("Super custom verbosity", caplevel=6)
        return {'msg': 'done'}
