#!/user/bin/python3.6

import csv


def read_csv(csv_file, delimiter=';'):
    entry_list = []
    with open(csv_file, 'r') as csvfile:
        for row in csv.reader(csvfile, delimiter=delimiter):
            for column in range(0, len(row)):
                entry_list.append(row[column])
    return entry_list
