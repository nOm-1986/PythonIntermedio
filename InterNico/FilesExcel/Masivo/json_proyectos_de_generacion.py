import csv
import json

FILE_URL = "d:/Development/Python/PythonIntermedio/InterNico/FilesExcel/Masivo/Lista_registro_proyectos.csv"

def read_csv(path):
    data = []
    with open(path, mode='r', encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            iterable = zip(header, row)
            country_dict = {k:v for k,v in iterable}
            data.append(country_dict)

    with open('result_json.js', mode="w") as resutlfile:
        json.dump(data, resutlfile, indent=4)

def run():
    read_csv(FILE_URL)
    
    


if __name__ == "__main__":
    run()