from ansible.plugins.action import ActionBase
from ansible.plugins.action.synchronize import ActionModule as Sync

class ActionModule(ActionBase):
    def run(self, tmp=None, task_vars=None):
        sync = Sync(self._task,
                    self._connection,
                    self._play_context,
                    self._loader,
                    self._templar,
                    self._shared_loader_obj)
        sync_result = sync.run(tmp=tmp, task_vars=task_vars)
        return dict(results=sync_result)
