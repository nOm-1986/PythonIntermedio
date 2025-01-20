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

country = input('Ingresa un pais => ')

result = utils.pupulation_by_country(data, country)
print(result['Country'])
print(result['Population'])