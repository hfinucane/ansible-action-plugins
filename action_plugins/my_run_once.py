from ansible.plugins.action import ActionBase


class ActionModule(ActionBase):
    BYPASS_HOST_LOOP = True

    def run(self, tmp=None, task_vars=None):
        return { "msg": "YOLO" }
