import csv


def read_csv(path):
   with open(path, "r") as csvfile:
      reader = csv.reader(csvfile, delimiter=",")
      data = {key:value for key,value in reader}
      total = [(int(i)) for i in data.values()]
   return sum(total)


response = read_csv('./datas.csv')
print(response)