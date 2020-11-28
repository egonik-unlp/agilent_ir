#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:48:09 2020

@author: gonik
"""

import pandas as pd 
import numpy as np
import csv

class spectrum():
    def __init__(self):
        self.name = 0
        self.wavenumber = 0
        self.transmittance = 0
        self.dict = 0 
    def load_files(self, file):
        self.name = file
        self.file = file
        self.dict = self.parse_files()
    def parse_file(self):
        with open(file, 'r') as f:
            conv = [int, float, float]
            reader = csv.reader(f)
            param = [con(next(reader)[0]) for con,i in zip(conv,range(3))]
            trash = [next(reader) for i in range(3)]
            self.wavenumber = np.linspace(param[1], param[2], int(param[0]))
            self.transmittance = [float(line[0]) for line in reader]
        return {'wavenumber': wavenumber, 'transmittance': transmittance } 