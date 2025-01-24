import csv

def read_csv(path):
   total = 0
   with open(path, mode='r', encoding="utf-8") as csvfile:
      csv_reader = csv.reader(csvfile, delimiter=',')
      for row in csv_reader:
         total += int(row[1])
   return total

response = read_csv('./data.csv')
print(response)


def read_csv(path):
   with open(path, 'r') as csvfile:      
      total = sum(int(r[1]) for r in csv.reader(csvfile))
      return total

response = read_csv('./data.csv')
print(response)