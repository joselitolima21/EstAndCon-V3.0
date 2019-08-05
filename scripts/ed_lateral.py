import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,M_LatDir,sufixo):
        self.sufixo = sufixo
        self.M_LatDir = M_LatDir 
    def graphs(self):
        autovalsLAT, autovecsLAT = np.linalg.eig(self.M_LatDir) 
        #Determinado os MODODS periodos LATERAIS
        dutchtroll = autovalsLAT[0]
        DdeltaB = autovecsLAT[0,0]
        Ddeltap = autovecsLAT[1,0]
        Ddeltar = autovecsLAT[2,0]
        Ddelta0 = autovecsLAT[3,0]
        Cl = autovalsLAT[2]
        Dl = autovalsLAT[3]
        if abs(Cl.real) > abs(Dl.real):
            roll = autovalsLAT[2]
            spiral = autovalsLAT[3]
            RdeltaB = autovecsLAT[0,2]
            Rdeltap = autovecsLAT[1,2]
            Rdeltar = autovecsLAT[2,2]
            Rdelta0 = autovecsLAT[3,2]
            SdeltaB = autovecsLAT[0,3]
            Sdeltap = autovecsLAT[1,3]
            Sdeltar = autovecsLAT[2,3]
            Sdelta0 = autovecsLAT[3,3]
        else:
            roll = autovalsLAT[3]
            spiral = autovalsLAT[2]
            RdeltaB = autovecsLAT[0,3]
            Rdeltap = autovecsLAT[1,3]
            Rdeltar = autovecsLAT[2,3]
            Rdelta0 = autovecsLAT[3,3]
            SdeltaB = autovecsLAT[0,2]
            Sdeltap = autovecsLAT[1,2]
            Sdeltar = autovecsLAT[2,2]
            Sdelta0 = autovecsLAT[3,2]
        Dn = dutchtroll.real
        Dw = dutchtroll.imag
        Rn = roll.real
        Rw = roll.imag
        Sn = spiral.real
        Sw = spiral.imag

        #=========================Grafico para o DUTCHROLL
        Dux = np.arange(0,30,0.01)
        DyB = 1*abs(DdeltaB.real)*np.exp(Dn*Dux)*np.cos(Dw*Dux+np.angle(DdeltaB))
        Dyp = 1*abs(Ddeltap.real)*np.exp(Dn*Dux)*np.cos(Dw*Dux+np.angle(Ddeltap))
        Dyr = 1*abs(Ddeltar.real)*np.exp(Dn*Dux)*np.cos(Dw*Dux+np.angle(Ddeltar))
        Dy0 = 1*abs(Ddelta0.real)*np.exp(Dn*Dux)*np.cos(Dw*Dux+np.angle(Ddelta0))
        my_dpi = 100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(Dux,DyB,'k-',color='green',label ='B') 
        plt.plot(Dux,Dyp,'k-',color='black',label ='p') 
        plt.plot(Dux,Dyr,'k-',color='blue',label ='r') 
        plt.plot(Dux,Dy0,'k-',color='yellow',label ='0') 
        plt.title("Estabilidade Dinamica - DUTCHROLL")
        plt.grid(True)
        plt.xlabel("t")
        plt.ylabel("Variaçao")
        plt.legend()
        plt.savefig('graficos/E.D.LAT.-DUTCHOLL-NELSON' + self.sufixo + '.png', format='png')
        #=========================Grafico para o SPIRAL
        Sux = np.arange(0,16,0.01)
        SyB = 1*abs(SdeltaB.real)*np.exp(Sn*Sux)*np.cos(Sw*Sux+np.angle(SdeltaB))
        Syp = 1*abs(Sdeltap.real)*np.exp(Sn*Sux)*np.cos(Sw*Sux+np.angle(Sdeltap))
        Syr = 1*abs(Sdeltar.real)*np.exp(Sn*Sux)*np.cos(Sw*Sux+np.angle(Sdeltar))
        Sy0 = 1*abs(Sdelta0.real)*np.exp(Sn*Sux)*np.cos(Sw*Sux+np.angle(Sdelta0))
        my_dpi = 100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(Sux,SyB,'k-',color='green',label ='B') 
        plt.plot(Sux,Syp,'k-',color='black',label ='p') 
        plt.plot(Sux,Syr,'k-',color='blue',label ='r') 
        plt.plot(Sux,Sy0,'k-',color='yellow',label ='0') 
        plt.title("Estabilidade Dinamica - SPIRAL")
        plt.grid(True)
        plt.xlabel("t")
        plt.ylabel("Variaçao")
        plt.legend()
        plt.savefig('graficos/E.D.LAT.-SPIRAL-NELSON' + self.sufixo + '.png', format='png')
        #=========================Grafico para o ROLL
        Rux = np.arange(0,6,0.01)
        RyB = 1*abs(RdeltaB.real)*np.exp(Rn*Rux)*np.cos(Rw*Rux+np.angle(RdeltaB))
        Ryp = 1*abs(Rdeltap.real)*np.exp(Rn*Rux)*np.cos(Rw*Rux+np.angle(Rdeltap))
        Ryr = 1*abs(Rdeltar.real)*np.exp(Rn*Rux)*np.cos(Rw*Rux+np.angle(Rdeltar))
        Ry0 = 1*abs(Rdelta0.real)*np.exp(Rn*Rux)*np.cos(Rw*Rux+np.angle(Rdelta0))
        my_dpi = 100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(Rux,RyB,'k-',color='green',label ='B') 
        plt.plot(Rux,Ryp,'k-',color='black',label ='p') 
        plt.plot(Rux,Ryr,'k-',color='blue',label ='r') 
        plt.plot(Rux,Ry0,'k-',color='yellow',label ='0') 
        plt.title("Estabilidade Dinamica - ROLL")
        plt.grid(True)
        plt.xlabel("t")
        plt.ylabel("Variaçao")
        plt.legend()
        plt.savefig('graficos/E.D.LAT.-ROLL-NELSON' + self.sufixo + '.png', format='png')