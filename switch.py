import json
import shutil
from pathlib import Path
from datetime import datetime
import os
import sys

# 默认 settings.json 路径（Windows）
if sys.platform == "darwin":
    base = Path.home() / "Library" / "Application Support"
elif sys.platform.startswith("win"):
    base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
else:
    base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))

SETTINGS_PATH = base / "Code" / "User" / "settings.json"
KEY = "leetcode.defaultLanguage"

def backup(path: Path):
    if path.exists():
        bak = path.with_suffix(f".bak.{datetime.now():%Y%m%d%H%M%S}")
        shutil.copy2(path, bak)
        return bak
    return None

def load_json(path: Path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}

def save_json(path: Path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def toggle_language(path: Path):
    data = load_json(path)
    current = data.get(KEY, "python3")
    new = "java" if current == "python3" else "python3"
    backup(path)
    data[KEY] = new
    save_json(path, data)
    print(f"{KEY} 从 '{current}' 切换为 '{new}'（已备份原文件）")

if __name__ == "__main__":
    if not SETTINGS_PATH.exists():
        print(f"找不到 settings.json: {SETTINGS_PATH}")
    else:
        toggle_language(SETTINGS_PATH)