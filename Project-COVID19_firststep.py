# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:39:14 2022

@author: vitob
"""
import numpy as np
import pandas
from matplotlib import pyplot as plt


def get_data_reg(url_reg, regione):
    date = []
    tot_positivi = []
    source = pandas.read_csv(url_reg)
    lista = source.values

    for line in lista:
        if str(line[3]) == regione:
            date.append(line[0])
            tot_positivi.append(line[10])

    return date, tot_positivi


def main():
    date, tot_positivi = get_data_reg("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv", "Sicilia")
  
    x = np.arange(0,len(date))
    y = np.array(tot_positivi)
    # disegniamo il grafico
    plt.plot(x,y)
    plt.show()


main()

