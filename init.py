import numpy as np
import csv
import os

def parse_file(file):
    with open(file, 'r') as f:
        conv = [int, float, float]
        reader = csv.reader(f)
        param = [con(next(reader)[0]) for con,i in zip(conv,range(3))]
        trash = [next(reader) for i in range(3)]
        wavenumber = np.linspace(param[1], param[2], int(param[0]))
        transmittance = [float(line[0]) for line in reader]
    return {'wavenumber': wavenumber, 'transmittance': transmittance } 

def parse_folder(path = '.', filter_asp = True, one_dict = True):
    if filter_asp:
        files = [i for i in os.listdir(path = path) if '.asp' in i[-4:]]
    else:
        files = [i for i in os.listdir(path = path)]
    if one_dict:
        return {'wavenumber': parse_file(files[0])['wavenumber'], file: trans for file, trans in zip(files,[])}
    

lista = os.listdir(path = '/home/gonik/Documents/agilent_ir/test_data/IR')
os.chdir('/home/gonik/Documents/agilent_ir/test_data/IR')
files = [i for i in lista if '.asp' in i[-4:]]

x = parse_file(files[1])
