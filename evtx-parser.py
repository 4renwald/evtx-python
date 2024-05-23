from evtx import PyEvtxParser
from pathlib import Path
import argparse
import json

def safeget(dct, *keys):
    """
    Helper function to safely get values from a nested dictionary
    """
    for key in keys:
        try:
            dct = dct[key]
        except (KeyError, TypeError) as e:
            return None
    return dct

def parse_evtx(file, eventids, show_all=None, search=None):
    with open(file, 'rb') as a:
        parser = PyEvtxParser(a)
        data = None
        
        for record in parser.records_json():
            if search is not None:
                dict_string = json.dumps(record)
                if dict_string.find(search) != -1:
                    data = json.loads(record['data'])
                else:
                    continue

            data = json.loads(record['data'])
            
            if (safeget(data, 'Event', 'System', 'EventID', '#text') or safeget(data, 'Event', 'System', 'EventID')) in eventids:
                if show_all:
                    print(f'{json.dumps(data, indent=2)}')
                else:
                    event = {
                    "EventID": safeget(data, 'Event', 'System', 'EventID', '#text') or safeget(data, 'Event', 'System', 'EventID'),
                    "TimeCreated": safeget(data, 'Event', 'System', 'TimeCreated', '#attributes', 'SystemTime'),
                    "EventRecordID": safeget(data, 'Event', 'System', 'EventRecordID'),
                    "UserID": safeget(data, 'Event', 'System', 'Security', '#attributes', 'UserID'),
                    "Computer": safeget(data, 'Event', 'System', 'Computer'),
                    "User": safeget(data, 'Event', 'UserData', 'EventXML', 'Param1'),
                    "SourceIP": safeget(data, 'Event', 'UserData', 'EventXML', 'Param3'),
                    "ProductName": safeget(data, 'Event', 'EventData', 'Product Name'),
                    "CategoryName": safeget(data, 'Event', 'EventData', 'Category Name'),
                    "DetectionUser": safeget(data, 'Event', 'EventData', 'Detection User'),
                    "Severity": safeget(data, 'Event', 'EventData', 'Severity Name'),
                    "ThreatName": safeget(data, 'Event', 'EventData', 'Threat Name'),
                    "SystemUptime": safeget(data, 'Event', 'EventData', 'Data', '#text'),
                    "ScriptBlockText": safeget(data, 'Event', 'EventData', 'ScriptBlockText'),
                    }
                    
                    for key, value in event.items():
                        if key == "SystemUptime" and value is not None:
                            value = value[4]
                        if value is not None:
                            print(f'{key}: {value}')

                    print('------------------------------------------')

def main():
    p = argparse.ArgumentParser(description='Parse evtx files by EventID')
    p.add_argument('--eventids', '-ids', type=int, required=True, nargs='+', help='EventID to parse, can be a list of IDs separated by a space. Example: --eventids 1149 ')
    p.add_argument('--file', '-f', type=Path, required=True, nargs=1, help='Path for evtx file')
    p.add_argument('--show-all', action='store_true', help='Show all event data')
    p.add_argument('--search', type=str, help='search for a specific string in the EventData')
    args = p.parse_args()
    
    parse_evtx(args.file[0], args.eventids, args.show_all, args.search)

if __name__ == "__main__":
    main()
