import csv

FILE_URL = "d:/Development/Python/PythonIntermedio/InterNico/FilesExcel/world_population.csv"
FILE_URL2 = "./world_population.csv"


def read_csv(path, searchingCountry):
    data = []
    with open(path, mode='r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            iterable = zip(header, row)
            country_dict = {k:v for k,v in iterable}
            data.append(country_dict)
    result = list(filter(lambda x: x['Country/Territory'] == searchingCountry, data))
    return result


if __name__ == '__main__':
    data1 = read_csv(FILE_URL, 'Colombia')
    print(data1)