import csv

values = []
with open('./csv/sample.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
        values.append({'Phone':row["Phone"],
                       "BussName":row['Name']})

        print("Phone:{0} Name:{1}".format(row['Phone'],row['Name']))
    print(values)