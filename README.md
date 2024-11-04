<h1 align="center"><img style="padding:0;vertical-align:bottom;" height="32" width="32" src="eventvwr.ico"/> evtx-python</h1>
<br/>

Quick evtx files parsing using: https://github.com/omerbenamram/evtx

## Setup environment:
```
python -m venv venv_evtx-python
source venv_evtx-python/bin/activate
pip install evtx
```

## Usage
```
python .\evtx-parser.py -h
usage: evtx-parser.py [-h] --eventids EVENTIDS [EVENTIDS ...] --file FILE [--show-all] [--search SEARCH]

Parse evtx files by EventID

options:
  -h, --help            show this help message and exit
  --eventids EVENTIDS [EVENTIDS ...], -ids EVENTIDS [EVENTIDS ...]
                        EventID to parse, can be a list of IDs separated by a space. Example: --eventids 1149
  --file FILE, -f FILE  Path for evtx file
  --show-all            Show all event data
  --search SEARCH       search for a specific string in the EventData
  ```