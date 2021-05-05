# -*- coding: utf-8 -*-
#!/usr/bin/env python3
from __future__ import print_function
import platform, subprocess, socket, sys, os, time, json
from datetime import datetime
# import mercury
import _thread
import threading
import queue

tempoMinimo = 30.0
queueAux = queue.Queue(maxsize=1000)
queueClassRace = queue.Queue(maxsize=1000)
largada = datetime.timestamp(datetime.now())

class Carro:
    def __init__(self, tag, timeStampAtual):
        self.tag = tag
        self.timeStampAnterior = 0.0
        self.timeStampAtual = timeStampAtual
        self.contadorVoltasCarro = 0

    def setTag(self, tag):
        self.tag = tag

    def setTimeStampAnterior(self, timeStampAnterior):
        self.timeStampAnterior = timeStampAnterior

    def setTimeStampAtual(self, timeStampAtual):
        self.timeStampAtual = timeStampAtual

    def setContadorVoltasCarro(self):
        self.contadorVoltasCarro += 1

    def getTag(self):
        return self.tag

    def getTimeStampAnterior(self):
        return self.timestampAnterior

    def getTimeStampAtual(self):
        return self.timeStampAtual

    def getContadorVoltasCarro(self):
        return self.contadorVoltasCarro

    def testeTempoMinimo(self, tempoMinimo):
        # if self.contadorVoltasCarro == 0:
            # largada = datetime.timestamp(datetime.now())
        if (self.timeStampAtual - self.timeStampAnterior) > tempoMinimo:
            return True
        else:
            return False
        
    def toString(self):        
        return "" + self.tag + " " + str(self.timeStampAnterior) + " " + str(self.timeStampAtual) + " " + str(self.contadorVoltasCarro)
        # return "" + self.tag + " " + str(self.timeStampAtual) + " " + str(self.contadorVoltasCarro)
    
    def testelargada(self):
        print(largada)

def retornaCarro(tag):
    for i in range(len(listaDeCarro)):
        aux = listaDeCarro[i].getTag()
        if aux == tag:
            # print("achou")
            return listaDeCarro[i]

def callBackRead(epc, timestamp):
    global largada    
    global tempoMinimo
    # tag = epc.decode("utf-8")
    carroAux = retornaCarro(epc)
    #if carroAux não existir vai retornar erro
    if carroAux.testeTempoMinimo(tempoMinimo):
        carroAux.setContadorVoltasCarro()
        carroAux.setTimeStampAnterior(carroAux.getTimeStampAtual())
        carroAux.setTimeStampAtual(timestamp)
        print(carroAux.toString())
        queueClassRace.put(carroAux)
carro1 = Carro ("E20000172211012518905484", 0.04639387130737305)
carro2 = Carro ("E20000172211011718905474", 0.051393985748291016)
carro3 = Carro ("E2000017221101321890548C", 0.07022285461425781)
carro4 = Carro ("E2000017221101241890547C", 35.05587601661682129)
carro5 = Carro ("E20000172211013118905493", 40.06587600708007812)

# carro4 = Carro ("E2000017221101241890547C", 0.06587600708007812)
# carro5 = Carro ("E20000172211013118905493", 60.0)
# carro4 = Carro ("E2000017221101241890547C", 60.0)

listaDeCarro = [carro1, carro2, carro3, carro4, carro5]

# callBackRead("E2000017221101241890547C", 35.05587601661682129)
# callBackRead("E20000172211013118905493", 40.06587600708007812)
# # carro4 = Carro ("E2000017221101241890547C", 66.05587601661682129)
# callBackRead("E2000017221101241890547C", 70.05587601661682129)


# "E20000172211012518905484": 0.04639387130737305,
# "E20000172211011718905474": 0.051393985748291016,
# "E2000017221101321890548C": 0.07022285461425781,
# "E2000017221101241890547C": 0.05587601661682129,
# "E20000172211013118905493": 0.06587600708007812


# largada = datetime.timestamp(datetime.now())




        
