import os
from datetime import datetime
from Paths import io_paths

class Log:
    def __init__(self):
        self.log_dir = io_paths.LOG_DIR
        self.ensure_log_dir()

    def ensure_log_dir(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def get_log_file_path(self):
        today = datetime.now().strftime("%Y-%m-%d")
        path = os.path.join(self.log_dir, f"kras_{today}.txt")
        return path

    def write_log(self, message):
        log_file_path = self.get_log_file_path()
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{now}] {message}\n"

        with open(log_file_path, "a", encoding="utf-8") as f:
            f.write(log_line)
