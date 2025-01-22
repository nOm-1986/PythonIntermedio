import utils

data = [
    {
        'Country': 'Colombia',
        'Population': 2000
    },{
        'Country': 'Ecuador',
        'Population': 3000
    }
]

def run():
    country2 = input('Ingresa un pais => ')
    result = utils.pupulation_by_country(data, country2)
    print(result[0]['Country'])
    print(result[0]['Population'])

#Dualidad para ejecutar desde la terminar directamente, o haciendo el import desde otro archivo.
if __name__ == "__main__":
    run()