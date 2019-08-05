import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,M_Long,sufixo):
        self.sufixo = sufixo
        self.M_Long = M_Long 
    def graphs(self):
        #Calcualando os autovalores e autovetores
        autovalsLON, autovecsLON = np.linalg.eig(self.M_Long)
        #Determinado os MODODS periodos LOONGITUDINAIS       
        A = autovalsLON[0]
        B = autovalsLON[2]  
        if A.imag > B.imag:
            short = A
            phugoid = B
            SdeltaU = autovecsLON[0,0]
            SdeltaW = autovecsLON[1,0]
            Sdeltaq = autovecsLON[2,0]
            Sdelta0 = autovecsLON[3,0]
            PdeltaU = autovecsLON[0,2]
            PdeltaW = autovecsLON[1,2]
            Pdeltaq = autovecsLON[2,2]
            Pdelta0 = autovecsLON[3,2]
        else:
            short = B
            phugoid = A
            SdeltaU = autovecsLON[0,2]
            SdeltaW = autovecsLON[1,2]
            Sdeltaq = autovecsLON[2,2]
            Sdelta0 = autovecsLON[3,2]
            PdeltaU = autovecsLON[0,0]
            PdeltaW = autovecsLON[1,0]
            Pdeltaq = autovecsLON[2,0]
            Pdelta0 = autovecsLON[3,0]
       
        pn = phugoid.real
        pw = phugoid.imag
        sn = short.real
        sw = short.imag

        #=========================Grafico para o PHUGOID
        pux = np.arange(0,100,0.01)
        pyu = 1*abs(PdeltaU.real)*np.exp(pn*pux)*np.cos(pw*pux+np.angle(PdeltaU))
        pyw = 1*abs(PdeltaW.real)*np.exp(pn*pux)*np.cos(pw*pux+np.angle(PdeltaW))
        pyq = 1*abs(Pdeltaq.real)*np.exp(pn*pux)*np.cos(pw*pux+np.angle(Pdeltaq))
        py0 = 1*abs(Pdelta0.real)*np.exp(pn*pux)*np.cos(pw*pux+np.angle(Pdelta0))
        my_dpi = 100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(pux,pyu,'k-',color='green',label ='U') 
        plt.plot(pux,pyw,'k-',color='black',label ='W') 
        plt.plot(pux,pyq,'k-',color='blue',label ='q') 
        plt.plot(pux,py0,'k-',color='yellow',label ='0') 
        plt.title("Estabilidade Dinamica - PHUGOID")
        plt.grid(True)
        plt.xlabel("t")
        plt.ylabel("Variaçao")
        plt.legend()
        plt.savefig('graficos/E.D.LON.-PHUGOID-NELSON' + self.sufixo + '.png', format='png')
        #=========================Grafico para o SHORT
        sux = np.arange(0,4,0.01)
        syu = 1*abs(SdeltaU.real)*np.exp(sn*sux)*np.cos(sw*sux+np.angle(SdeltaU))
        syw = 1*abs(SdeltaW.real)*np.exp(sn*sux)*np.cos(sw*sux+np.angle(SdeltaW))
        syq = 1*abs(Sdeltaq.real)*np.exp(sn*sux)*np.cos(sw*sux+np.angle(Sdeltaq))
        sy0 = 1*abs(Sdelta0.real)*np.exp(sn*sux)*np.cos(sw*sux+np.angle(Sdelta0))
        my_dpi = 100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(sux,syu,'k-',color='green',label ='U') 
        plt.plot(sux,syw,'k-',color='black',label ='W') 
        plt.plot(sux,syq,'k-',color='blue',label ='q') 
        plt.plot(sux,sy0,'k-',color='yellow',label ='0') 
        plt.title("Estabilidade Dinamica - SHORT")
        plt.grid(True)
        plt.xlabel("t")
        plt.ylabel("Variaçao")
        plt.legend()
        plt.savefig('graficos/E.D.LON.-SHORT-NELSON' + self.sufixo + '.png', format='png')