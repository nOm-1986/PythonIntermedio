items = [
    {
        'product' : 'camisa',
        'price': 100,
    },
    {
        'product' : 'pantalones',
        'price': 160,
    },
    {
        'product' : 'zapatos',
        'price': 300,
    },
    {
        'product' : 'bufanda',
        'price': 30,
    }
]

prices = list(map(lambda x: x['price'], items))
print(prices)

def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

print(items)
items_with_taxes = list(map(add_taxes, items))
print(items_with_taxes)