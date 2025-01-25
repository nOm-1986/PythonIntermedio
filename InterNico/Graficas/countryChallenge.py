import csv
import charts
FILE_URL = "d:/Development/Python/PythonIntermedio/InterNico/FilesExcel/world_population.csv"


def read_csv(path, searchedCountry):
    data = []
    with open(path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            iterable = zip(header, row)
            country_dict = {k:v for k,v in iterable}
            data.append(country_dict)
    return list(filter(lambda x: x['Country/Territory'] == searchedCountry, data))


def get_population(country_dict):
    population_dict = {
        '2022' : float(country_dict['2022 Population']),
        '2020' : float(country_dict['2020 Population']),
        '2015' : float(country_dict['2015 Population']),
        '2010' : float(country_dict['2010 Population']),
        '2000' : float(country_dict['2000 Population']),
        '1990' : float(country_dict['1990 Population']),
        '1980' : float(country_dict['1980 Population']),
        '1970' : float(country_dict['1970 Population']),
    }
    labels = population_dict.keys() 
    values = population_dict.values()
    return labels, values

def run():
    country = input("Ingresa el pais: ")
    result_search = read_csv(FILE_URL, country)
    labels, values = get_population(result_search[0])
    charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
    run()
            