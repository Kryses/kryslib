import json
import subprocess
from datetime import datetime

from libqtile.widget import base


class TaskWidget(base.InLoopPollText, base.PaddingMixin, base.MarginMixin):
    orientations = base.ORIENTATION_HORIZONTAL

    def __init__(self, default_text="N/A", **config):
        super().__init__(default_text, **config)
        self.add_defaults(base.PaddingMixin.defaults)
        self.add_defaults(base.MarginMixin.defaults)

    def poll(self):
        text_format = "  {project} |   {task_name} | 󰦖  {task_time}"
        is_active = subprocess.run(
            ["timew", "get", "dom.active"], capture_output=True, text=True
        )
        if not int(is_active.stdout):
            return "No active task"

        task = subprocess.run(
            ["timew", "get", "dom.active.json"], capture_output=True, text=True
        )
        task_json = json.loads(task.stdout)
        task_text = task_json["tags"][-1]
        task_project = task_json["tags"][-2]
        task_start_time = subprocess.run(
            ["timew", "get", "dom.active.start"], capture_output=True, text=True
        ).stdout
        start_time = datetime.fromisoformat(task_start_time.strip())
        duration = datetime.now() - start_time
        hours = duration.seconds // 3600
        minutes = (duration.seconds // 60) % 60
        seconds = duration.seconds % 60
        formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

        return text_format.format(
            project=self.truncate_string(task_project, 20),
            task_name=self.truncate_string(task_text, 20),
            task_time=formatted_time,
        )

    def truncate_string(self, text, width):
        return text[:width] + "…" if len(text) > width else text
