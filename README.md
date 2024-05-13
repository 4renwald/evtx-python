# evtx-python
Quick evtx files parsing using https://github.com/omerbenamram/evtx

## Setup env:
```
python -m venv venv_evtx-python
source venv_evtx-python/bin/activate
pip install evtx
```

## Usage
```
python .\evtx-parser.py -h
usage: evtx-parser.py [-h] --eventids EVENTIDS [EVENTIDS ...] --file FILE [--show-all]

Parse evtx files by EventID

options:
  -h, --help            show this help message and exit
  --eventids EVENTIDS [EVENTIDS ...], -ids EVENTIDS [EVENTIDS ...]
                        EventID to parse
  --file FILE, -f FILE  Path for evtx file
  --show-all            Show all event data
  ```