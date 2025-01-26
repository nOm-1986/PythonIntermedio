import csv
import matplotlib.pyplot as plt

FILE_URL = "d:/Development/Python/PythonIntermedio/InterNico/FilesExcel/world_population.csv"

def read_csv(path):
    data = []
    with open(path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        header = next(csv_reader)
        for row in csv_reader:
            iterable = zip(header, row)
            country_dict = {k:v for k,v in iterable}
            data.append(country_dict)
    return data

def generate_chart(l, p):
    fig, ax = plt.subplots()
    ax.pie(p, labels=l)
    ax.axis('equal')
    plt.show()

def run():
    data = read_csv(FILE_URL)

    selected = input('Ingrese un continente: ')
    filtro = list(filter(lambda item: item['Continent'] == selected, data))
    labels2 = list(map(lambda x: x['Country/Territory'], filtro))
    percentages2 = list(map(lambda x: x['World Population Percentage'], filtro))
    generate_chart(labels2, percentages2)

if __name__ == "__main__":
    run()