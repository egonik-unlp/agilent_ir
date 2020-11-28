#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:48:09 2020

@author: gonik
"""
import os
import pandas as pd 
import numpy as np
import csv

class spectrum():
    def __init__(self):
        self.name = 0
        self.wavenumber = []
        self.transmittance = 0
        self.dict = 0 
        self.file = 0
    def load_files(self, file):
        self.name = file
        self.file = file
        self.parse_files()

    def parse_file(self):
        with open(self.file, 'r') as f:
            conv = [int, float, float]
            reader = csv.reader(f)
            param = [con(next(reader)[0]) for con,i in zip(conv,range(3))]
            trash = [next(reader) for i in range(3)]
            self.wavenumber = np.linspace(param[1], param[2], int(param[0]))
            self.transmittance = [float(line[0]) for line in reader]

    def as_pandas(self):
        return pd.series(data = self.transmittance, index = self.wavenumber)
    def as_dict(self):
        return {'wavenumber': self.wavenumber, 'transmittance': self.transmittance}
    def as_array(self):
        return np.arrat(self.wavenumber. self.transmittance)


class spectra(spectrum):
    def __init__(self):
        super().__init__()
        self.wavenumber = {}
    def append_data(self):
    def load_spectra(self, imported_spectra):
        [self.load_files() for i in imported_spectra]

folder = os.getcwd()
files = [i for i in  os.listdir() if '.asp' in i[-4:]]
arch = spectrum()
arch.load_files(files[1])
