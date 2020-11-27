import numpy as np
import csv
import os
def parse_file(file):
    with open(file, 'r') as f:
        reader = csv.reader(f)
        param = [int(next(reader)[0]) for i in range(3)]
    return np.linspace(param[1], param[2], param[0])


lista = os.listdir(path = '/home/gonik/Documents/agilent_ir/test_data/IR')

files = [i for i in lista if '.asp' in i[-4:]]

x = parse_file(files[1])
