import csv


def write_csv():
    with open('csvtest.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow([1, 2, 3])
        writer.writerow(["가", "나", "다"])
        writer.writerow(["a", "b", "c"])


# write_csv()

def writerows_csv():
    csvrows = [
        ["가", "나", "다"],
        [11, 22, 33],
        ['aa', 'bb', 'cc'],
    ]

    with open("csvtest2.csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerows(csvrows)


# writerows_csv()

def read_csv():
    reader = csv.reader(open('csvtest.csv'))
    for row in reader:
        print(row)

    print("======================")

    reader2 = csv.reader(open('csvtest2.csv'))

    for row in reader2:
        print(row)


read_csv()
