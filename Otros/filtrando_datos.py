"""Ejercicio filtrando datos con python.
    Utiliza de ejemplo funciones de orden superiro - alto nivel ( Son funciones que reciben como parametro a otra función y hacen algo con ella.) 
"""

from concurrent.futures.thread import _worker


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    #All python developers - names
    all_python_devs = [worker["name"] for worker in DATA if worker['language'] == 'python']
    
    #All workers from platzi
    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi' ]
    
    #All adults with filters
    adults = list(filter(lambda worker: worker['age'] > 18 , DATA))
    #adults = [worker for worker in DATA if worker['age'] > 18]
    #Como lo anterior me trae todo el diccionario ahora solo saco los nombres utilizando map
    adulst = list(map(lambda worker: worker['name'], adults))
    
    old_people = list(map(lambda worker: worker | {"old": worker['age'] > 70}, DATA))
    old_true = list(filter(lambda worker: worker['old'] == False, old_people))
    old_true = list(map(lambda worker: worker['name'], old_true))
    print(old_true)


if __name__ == '__main__':
    run()