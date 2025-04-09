import csv
import json

FILE_URL="D:\FENOGE\5 - Act - April\Masivo\Financiero y Contable"

def read_csv(path):
    data = []
    with open(path, mode="r", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=",")
        headers = next(csv_reader)
        for row in csv_reader:
            iterable = zip(headers, row)
            result_dict = {k:v for k,v in iterable}
            data.append(result_dict)
    
    with open('json_financiero_contable.js', mode='w') as resultfile:
        json.dump(data, resultfile, indent=4)
        
def run():
    read_csv(FILE_URL)

