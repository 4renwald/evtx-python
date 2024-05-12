from evtx import PyEvtxParser
from pathlib import Path
import argparse
import json

def parse_evtx(file, eventids):
    with open(file, 'rb') as a:
        parser = PyEvtxParser(a)
        
        for record in parser.records_json():
            
            data = json.loads(record['data'])
            
            if data['Event']['System']['EventID'] in eventids:
                try: 
                    print(f'TimeCreated: {data['Event']['System']['TimeCreated']['#attributes']['SystemTime']}')
                    print(f'EventRecordID: {data['Event']['System']['EventRecordID']}')
                    print(f'EventID: {data['Event']['System']['EventID']}')
                    print(f'Computer: {data['Event']['System']['Computer']}')
                    print(f'User: {data['Event']['UserData']['EventXML']['Param1']}')
                    print(f'Source IP address: {data['Event']['UserData']['EventXML']['Param3']}')
                except KeyError:
                    pass

                finally:
                    print(f'------------------------------------------')

def main():
    p = argparse.ArgumentParser(description='Parse evtx files by EventID')
    
    p.add_argument('--eventids', '-ids', 
                    type=int, 
                    required=True,
                    nargs='+',
                    help='EventID to parse')
    
    p.add_argument('--file', '-f', 
                    type=Path, 
                    required=True, 
                    nargs=1, 
                    help='Path for evtx file')
    
    args = p.parse_args()
    
    ids = args.eventids
    file = args.file[0]
    
    parse_evtx(file, ids)

if __name__ == "__main__":
    main()