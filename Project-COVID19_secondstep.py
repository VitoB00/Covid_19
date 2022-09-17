# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:35:58 2022

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
    minimo = 847
    massimo = 1000
    count = 0

    for line in lista:
        if str(line[3]) == regione:
            count += 1
            if minimo < count < massimo:
                date.append(line[0])
                tot_positivi.append(line[10])

    return date, tot_positivi


def main():
    date, tot_positivi = get_data_reg("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni.csv", "Friuli Venezia Giulia")

    x = np.arange(0, len(date))
    y = np.array(tot_positivi)
    # disegniamo il grafico
    plt.plot(x, y)
    plt.show()


main()