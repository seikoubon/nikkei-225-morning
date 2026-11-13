"""Copy the published forecast snapshot; no credentials or model calculation."""
import json
import shutil
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ORIGIN = 'https://nikkei-225-morning.seikou453202.chatgpt.site'


def build(destination):
    shutil.copytree(Path(__file__).resolve().parents[1] / 'public', destination, dirs_exist_ok=True)
    values = {}
    for name in ('dashboard.json', 'history.json'):
        request = urllib.request.Request(ORIGIN + '/' + name, headers={'User-Agent': 'nikkei-225-morning-public-mirror/1.0'})
        with urllib.request.urlopen(request, timeout=30) as response:
            values[name] = json.load(response)
    data = values['dashboard.json']
    if data.get('version') != 1 or not isinstance(data.get('rows'), list):
        raise ValueError('Invalid dashboard')
    datetime.fromisoformat(data['updated'])
    if not isinstance(values['history.json'], list):
        raise ValueError('Invalid history')
    for name, value in values.items():
        (destination / name).write_text(json.dumps(value, ensure_ascii=False, allow_nan=False, separators=(',', ':')) + '\n')
    print('Published source received:', data['updated'], 'records:', len(data['rows']))


if __name__ == '__main__':
    build(Path(sys.argv[1] if len(sys.argv) > 1 else '_site'))
