import requests
import argparse
import json
import pprint

argParser = argparse.ArgumentParser()
argParser.add_argument("-m", "--method", help="Service to be accessed")
argParser.add_argument("-k", "--apiKey", help="ApiKey of the Connection's DataNeed")
argParser.add_argument("-s", "--apiSecret", help="ApiSecret of the Connection's DataNeed")
argParser.add_argument("-c", "--connectionId", help="ConnectionId of the Connection you want to query data for")
argParser.add_argument("-lu", "--lastUpdateAfter", help="For connections, to get only connections where permissions have been changed after the UTC date")
argParser.add_argument("-fd", "--fromDate", help="Query TimeSeries entries from that iso datetime")
argParser.add_argument("-td", "--toDate", help="Query TimeSeries entries to that iso datetime")
argParser.add_argument("-o", "--output", help="Output file to write the data to")

args = argParser.parse_args()

headers = {
    "Accept": "application/json",
    "X-Api-Key": args.apiKey,
    "X-Api-Secret": args.apiSecret,
    "X-Connection-customerConnectionId": args.connectionId,
    "X-LastUpdateAfter": args.lastUpdateAfter,
    "X-FromDate": args.fromDate,
    "X-ToDate": args.toDate,
}

resp = requests.get('https://online.eddie.energy/api/' + args.method, headers=headers)

if resp.status_code == 200:
    respJson = json.loads(resp.content)
    json_data = json.dumps(respJson, indent=2)
    print(json_data)

    if args.output:
        with open(args.output, "w") as file:
            file.write(json_data)
        print(f"Data written to {args.output}")
else:
    print("ERROR: HTTP" + str(resp.status_code))
