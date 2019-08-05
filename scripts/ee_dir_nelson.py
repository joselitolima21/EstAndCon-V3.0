import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs,sufixo):
        self.sufixo = sufixo
        self.inputs = inputs
    def outputs(self):
        k_n = self.inputs['k_n'];k_Rl = self.inputs['k_Rl'];S_fs = self.inputs['S_fs']
        l_fs = self.inputs['l_fs'];AR_w = self.inputs['AR_w'];b_w = self.inputs['b_w']
        z_w = self.inputs['z_w'];S_w = self.inputs['S_w'];S_vt = self.inputs['S_vt']
        lambda_w = self.inputs['lambda_w'];w_maxf = self.inputs['w_maxf'];eta_vt = self.inputs['eta_vt']
        x_vt = self.inputs['x_vt'];C_Lavt = self.inputs['C_Lavt']
        self.C_nBwf = - k_n * k_Rl * (S_fs * l_fs) / (S_w * b_w)
        do_dB = (0.724+3.06*(S_vt/S_w)/(1+np.cos(lambda_w)) + 0.4*z_w/w_maxf+0.009*AR_w)/eta_vt - 1
        V_vt = (x_vt * S_vt) / (b_w * S_w)
        self.C_nBvt = V_vt * C_Lavt * eta_vt * (1 + do_dB)
        self.C_nB = self.C_nBwf + self.C_nBvt
        with open('resultados/E.E.DIR-NELSON' + self.sufixo + '.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE ESTÁTICA DIRECIONAL                      |\n')
            saida.write('| METODOLOGIA: NELSON                                   |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  k n .....................................    ');saida.write(str('%5.4f'%k_n));saida.write('  |\n')
            saida.write('|  k Rl ....................................    ');saida.write(str('%5.4f'%k_Rl));saida.write('  |\n')
            saida.write('|  S fs ....................................    ');saida.write(str('%5.4f'%S_fs));saida.write('  |\n')
            saida.write('|  l fs ....................................    ');saida.write(str('%5.4f'%l_fs));saida.write('  |\n')
            saida.write('|  S w .....................................    ');saida.write(str('%5.4f'%S_w));saida.write('  |\n')
            saida.write('|  b w .....................................    ');saida.write(str('%5.4f'%b_w));saida.write('  |\n')
            saida.write('|  C Lα vt .................................    ');saida.write(str('%5.4f'%C_Lavt));saida.write('  |\n')
            saida.write('|  x vt ....................................    ');saida.write(str('%5.4f'%x_vt));saida.write('  |\n')
            saida.write('|  S vt ....................................    ');saida.write(str('%5.4f'%S_vt));saida.write('  |\n')
            saida.write('|  η vt ....................................    ');saida.write(str('%5.4f'%eta_vt));saida.write('  |\n')
            saida.write('|  Λ w .....................................    ');saida.write(str('%5.4f'%lambda_w));saida.write('  |\n')
            saida.write('|  z w .....................................    ');saida.write(str('%5.4f'%z_w));saida.write('  |\n')
            saida.write('|  w max f .................................    ');saida.write(str('%5.4f'%w_maxf));saida.write('  |\n')
            saida.write('|  AR w ....................................    ');saida.write(str('%5.4f'%AR_w));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  V vt ....................................    ');saida.write(str('%5.4f'%V_vt));saida.write('  |\n')
            saida.write('|  dσ / dβ .................................    ');saida.write(str('%5.4f'%do_dB));saida.write('  |\n')
            saida.write('|  C nβ wf .................................   ');saida.write(str('%5.4f'%self.C_nBwf));saida.write('  |\n')
            saida.write('|  C nβ vt .................................    ');saida.write(str('%5.4f'%self.C_nBvt));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|  C nβ ....................................    ');saida.write(str('%5.4f'%self.C_nB));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
    def graphs(self):
        x = np.array(range(-15,15))
        my_dpi=100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(x,x*self.C_nB,'k-',color='black',label ='Cnβ')
        plt.plot(x,x*self.C_nBwf,'k-',color='red',label = 'Cnβwf')
        plt.plot(x,x*self.C_nBvt,'k-',color='green',label = 'Cnβvt')
        plt.title("Estabilidade Estatica Direcional")
        plt.grid(True)
        plt.xlabel("β")
        plt.ylabel("Cn")
        plt.legend()
        plt.savefig('graficos/E.E.DIR-NELSON' + self.sufixo + '.png', format='png')
    def valor(self):
        return self.C_nB