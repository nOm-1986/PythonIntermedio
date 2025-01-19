def filter_by_length(words):
   return list(filter(lambda x: len(x) >= 4, words))

words = ['amor', 'sol', 'piedra', 'día']
response = filter_by_length(words)
print(response)