def calculate_total(products):
    total = 0
    for product in products:
        total += product['price']
    return total

def test_calculate_total_with_empty_list():
    assert calculate_total([]) == 0
    #print('Hola mundo')

def test_calculate_total_with_sigle_product():
    products = [
        {
            "name": "Laptop ASUS",
            "price": 5,
        }
    ]
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_products():
    products = [
        {'name':'1', 'price': 10},
        {'name':'2', 'price': 20},
        {'name':'3', 'price': 30},
    ]
    assert calculate_total(products) == 60


def run():
    test_calculate_total_with_empty_list()
    test_calculate_total_with_sigle_product()
    test_calculate_total_with_multiple_products()

if __name__ == "__main__":
    run()