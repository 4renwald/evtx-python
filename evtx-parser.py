from evtx import PyEvtxParser
from pathlib import Path
import argparse
import json

def safeget(dct, *keys):
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
                    EventID = safeget(data, 'Event', 'System', 'EventID', '#text') or safeget(data, 'Event', 'System', 'EventID')
                    TimeCreated = safeget(data, 'Event', 'System', 'TimeCreated', '#attributes', 'SystemTime')
                    EventRecordID = safeget(data, 'Event', 'System', 'EventRecordID')
                    UserID = safeget(data, 'Event', 'System', 'Security', '#attributes', 'UserID')
                    Computer = safeget(data, 'Event', 'System', 'Computer')
                    User = safeget(data, 'Event', 'UserData', 'EventXML', 'Param1')
                    SourceIP = safeget(data, 'Event', 'UserData', 'EventXML', 'Param3')
                    ProductName = safeget(data, 'Event', 'EventData', 'Product Name')
                    CategoryName = safeget(data, 'Event', 'EventData', 'Category Name')
                    DetectionUser = safeget(data, 'Event', 'EventData', 'Detection User')
                    Severity = safeget(data, 'Event', 'EventData', 'Severity Name')
                    ThreatName = safeget(data, 'Event', 'EventData', 'Threat Name')
                    SystemUptime = safeget(data, 'Event', 'EventData', 'Data', '#text')
                    ScriptBlockText = safeget(data, 'Event', 'EventData', 'ScriptBlockText')
                    
                    if TimeCreated is not None:
                        print(f'TimeCreated: {TimeCreated}')
                        
                    if EventRecordID is not None:
                        print(f'EventRecordID: {EventRecordID}')

                    if EventID is not None:
                        print(f'EventID: {EventID}')

                    if UserID is not None:
                        print(f'UserID: {UserID}')
                    
                    if Computer is not None:
                        print(f'Computer: {Computer}')
                        
                    if User is not None:    
                        print(f'User: {User}')
                    
                    if SourceIP is not None:
                        print(f'Source IP address: {SourceIP}')

                    if ProductName is not None:
                        print(f'Product Name: {ProductName}')
                    
                    if CategoryName is not None:
                        print(f'Category Name: {CategoryName}')
                    
                    if DetectionUser is not None:
                        print(f'Detection User: {DetectionUser}')
                    
                    if Severity is not None: 
                        print(f'Severity: {Severity}')
                    
                    if ThreatName is not None:
                        print(f'Threat Name: {ThreatName}')
                    
                    if SystemUptime is not None:
                        print(f'System Uptime: {SystemUptime[4]}')

                    if ScriptBlockText is not None:
                        print(f'Script  Block Text: {ScriptBlockText}')

                    print(f'------------------------------------------')

def main():
    p = argparse.ArgumentParser(description='Parse evtx files by EventID')
    p.add_argument('--eventids', '-ids', type=int, required=True, nargs='+', help='EventID to parse')
    p.add_argument('--file', '-f', type=Path, required=True, nargs=1, help='Path for evtx file')
    p.add_argument('--show-all', action='store_true', help='Show all event data')
    p.add_argument('--search', type=str, help='search for a specific string in the EventData')
    args = p.parse_args()
    
    parse_evtx(args.file[0], args.eventids, args.show_all, args.search)

if __name__ == "__main__":
    main()
