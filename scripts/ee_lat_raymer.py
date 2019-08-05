import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs,sufixo):
        self.sufixo = sufixo
        self.inputs = inputs
    def outputs(self):
        C_Law = self.inputs['C_Law'];gamma_w = self.inputs['gamma_w']
        lambda2_w = self.inputs['lambda2_w'];AR_w = self.inputs['AR_w']
        b_w = self.inputs['b_w'];z_w = self.inputs['z_w'];h_medf = self.inputs['h_medf']
        w_medf = self.inputs['w_medf'];C_lBw_CL = self.inputs['C_lBw_CL']
        self.C_lBgamma = - (C_Law * gamma_w *2* (1+2*lambda2_w)) / ( 4*3*(1+lambda2_w))
        self.C_lBwf = -1.2 * np.sqrt(AR_w) * z_w * (h_medf + w_medf) / (b_w**2)
        self.C_lBlambda = C_lBw_CL * np.pi / 180 * C_Law
        self.C_lB = self.C_lBgamma + self.C_lBwf + self.C_lBlambda
        with open('resultados/E.E.LAT-RAYMER' + self.sufixo + '.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE ESTÁTICA LATERAL                         |\n')
            saida.write('| METODOLOGIA: RAYMER                                   |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  C Lα w ..................................    ');saida.write(str('%5.4f'%C_Law));saida.write('  |\n')
            saida.write('|  Γ w .....................................    ');saida.write(str('%5.4f'%gamma_w));saida.write('  |\n')
            saida.write('|  λ w .....................................    ');saida.write(str('%5.4f'%lambda2_w));saida.write('  |\n')
            saida.write('|  AR w ....................................    ');saida.write(str('%5.4f'%AR_w));saida.write('  |\n')
            saida.write('|  z w .....................................    ');saida.write(str('%5.4f'%z_w));saida.write('  |\n')
            saida.write('|  h med f .................................    ');saida.write(str('%5.4f'%h_medf));saida.write('  |\n')
            saida.write('|  w med f .................................    ');saida.write(str('%5.4f'%w_medf));saida.write('  |\n')
            saida.write('|  b w .....................................    ');saida.write(str('%5.4f'%b_w));saida.write('  |\n')
            saida.write('|  C lβ w / C L ............................   ');saida.write(str('%5.4f'%C_lBw_CL));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  C lβ Γ ..................................   ');saida.write(str('%5.4f'%self.C_lBgamma));saida.write('  |\n')
            saida.write('|  C lβ wf .................................   ');saida.write(str('%5.4f'%self.C_lBwf));saida.write('  |\n')
            saida.write('|  C lβ Λ ..................................   ');saida.write(str('%5.4f'%self.C_lBlambda));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|  C lβ ....................................   ');saida.write(str('%5.4f'%self.C_lB));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
    def graphs(self):
        x = np.array(range(-15,15))
        my_dpi=100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(x,x*self.C_lB,'k-',color='black',label ='Clβ')
        plt.plot(x,x*self.C_lBgamma,'k-',color='red',label = 'ClβΓ')
        plt.plot(x,x*self.C_lBwf,'k-',color='green',label = 'Clβwf')
        plt.plot(x,x*self.C_lBlambda,'k-',color='yellow',label = 'ClβΛ')
        plt.title("Estabilidade Estatica Lateral")
        plt.grid(True)
        plt.xlabel("β")
        plt.ylabel("Cl")
        plt.legend()
        plt.savefig('graficos/E.E.LAT-RAYMER' + self.sufixo + '.png', format='png')
    def valor(self):
        return self.C_lB