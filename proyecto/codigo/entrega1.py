# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 22:58:17 2021

@author: Luisa Garcia
"""

import csv

name_archivo = ''

with open(name_archivo, newline='') as f:
    datos = csv.reader(f, delimiter = '\t')
    lista1 = list(datos)