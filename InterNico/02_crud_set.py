set_countries = {'col', 'mex', 'bol'}
size = len(set_countries)
print(size)

print("=" * 30)

print('col' in set_countries)
print('pe' in set_countries)

#add
print("=" * 30)
set_countries.add('pe')
print(f'Added pe to my set: {set_countries}' )
print("=" * 30)

#update
print("=" * 30)
set_countries.update({'ar', 'ch', 'ecu', 'bol', 'pe'})
print(f'Updating my set using' + '{ "arg", "ch", "ecu" ...}' + f'{set_countries}' )

# Remove
print("=" * 30)
set_countries.remove('pe')
print(f"Removing 'pe' from my set using remove() .... {set_countries} " )
print("=" * 30)

# Remove item if doesnt exits without explote
print("=" * 30)
set_countries.discard('son')
print(set_countries)

# Deleting the data
set_countries.clear()
print(set_countries)
