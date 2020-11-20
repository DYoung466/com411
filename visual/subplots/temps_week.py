import csv

def read_data():
  with open("visual/subplots/temps_week.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"')
    header = next(csv_reader)
    for row in csv_reader:
        all_data = []
        all_data.append(row)
        print(all_data[0])
        


read_data()