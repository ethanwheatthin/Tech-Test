#Ethan Collins 
#LA Angeles Technical Test Submission

import json
import csv


def json_to_csv():
    with open('Question 1/Angels_SWE_Question_1.json', newline="") as json_file:
        data = json.load(json_file)
        league_data = data['leagues']

        # Get all the present keys in the json payload and get a union of all the objects
        common_keys = set(k for r in league_data for k in r)

        with open('json_to_csv_output.csv', 'w', newline="") as f:
            cw = csv.DictWriter(f, fieldnames=common_keys, restval="", delimiter="\t")
            cw.writeheader()
            cw.writerows(league_data)
            f.close()
        print(data)

if __name__ == "__main__":
    json_to_csv()