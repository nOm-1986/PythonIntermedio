def message_creator(text):
    products = { 
                'computadora' : 'Con mi computadora puedo programar usando Python',
                'celular': 'En mi celular puedo aprender usando la app de Platzi',
                'cable' : '¡Hay un cable en mi bota!'}
    if text in products.keys():
        return products[text]
    else:
        return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)