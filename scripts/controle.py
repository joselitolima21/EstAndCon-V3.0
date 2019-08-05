import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs,sufixo,Cm,C_nB,C_lB):
        self.sufixo = sufixo
        self.inputs = inputs
        self.C_m0 = Cm[0]
        self.C_ma = Cm[1]
        self.C_nB = C_nB
        self.C_lB = C_lB
    def outputs(self):
        S_a = self.inputs['S_a'];S_e = self.inputs['S_e'];S_r = self.inputs['S_r']
        S_w = self.inputs['S_w'];S_ht = self.inputs['S_ht'];S_vt = self.inputs['S_vt']
        C_Law = self.inputs['C_Law'];c_a = self.inputs['c_a'];b_w = self.inputs['b_w']
        b_e_a = self.inputs['b_e_a'];b_i_a = self.inputs['b_i_a'];x_ht = self.inputs['x_ht']
        eta_ht = self.inputs['eta_ht'];C_Laht = self.inputs['C_Laht'];x_vt = self.inputs['x_vt']
        eta_vt = self.inputs['eta_vt'];C_Lavt = self.inputs['C_Lavt'];MAC_w = self.inputs['MAC_w']
        self.da = self.inputs['deflexao_a']
        self.de_mais = self.inputs['deflexao_e_+']
        self.de_menos = self.inputs['deflexao_e_-']
        self.dr = self.inputs['deflexao_r']
        V_ht = (x_ht * S_ht) / (MAC_w * S_w)
        V_vt = (x_vt * S_vt) / (b_w * S_w)
        tau_a = -4.8915*(S_a/S_w)**4 + 9.1273*(S_a/S_w)**3 -6.7373*(S_a/S_w)**2 + 3.0532*(S_a/S_w) + 0.0074
        tau_e = -4.8915*(S_e/S_ht)**4 + 9.1273*(S_e/S_ht)**3 -6.7373*(S_e/S_ht)**2 + 3.0532*(S_e/S_ht) + 0.0074
        tau_r = -4.8915*(S_r/S_vt)**4 + 9.1273*(S_r/S_vt)**3 -6.7373*(S_r/S_vt)**2 + 3.0532*(S_r/S_vt) + 0.0074

        self.C_lda = C_Law*tau_a*c_a/(S_w*b_w)*(b_e_a**2 - b_i_a**2)
        self.C_mde = -V_ht*eta_ht*C_Laht*tau_e
        self.C_ndr = -V_vt*eta_vt*C_Lavt*tau_r
        with open('resultados/CONTROLE'+ self.sufixo +'.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| COEFICIENTES DAS SUPERFÍCIE DE CONTROLE:              |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| AILERON (NELSON):                                     |\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('C Lα w ..................................       ');saida.write(str('%5.4f'%C_Law));saida.write('  |\n')
            saida.write('S w .....................................       ');saida.write(str('%5.4f'%S_w));saida.write('  |\n')
            saida.write('b w .....................................       ');saida.write(str('%5.4f'%b_w));saida.write('  |\n')
            saida.write('c a .....................................       ');saida.write(str('%5.4f'%c_a));saida.write('  |\n')
            saida.write('b ia ....................................       ');saida.write(str('%5.4f'%b_i_a));saida.write('  |\n')
            saida.write('b ea ....................................       ');saida.write(str('%5.4f'%b_e_a));saida.write('  |\n')
            saida.write('τ a .....................................       ');saida.write(str('%5.4f'%tau_a));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('C lδa ....................................       ');saida.write(str('%5.4f'%self.C_lda));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('| PROFUNDOR (NELSON):                                   |\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('V ht ....................................       ');saida.write(str('%5.4f'%V_ht));saida.write('  |\n')
            saida.write('η ht ....................................       ');saida.write(str('%5.4f'%eta_ht));saida.write('  |\n')
            saida.write('C Lα ht .................................       ');saida.write(str('%5.4f'%C_Laht));saida.write('  |\n')
            saida.write('τ e .....................................       ');saida.write(str('%5.4f'%tau_e));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('C mδe ....................................       ');saida.write(str('%5.4f'%self.C_mde));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('| LEME (NELSON):                                        |\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('V vt ....................................       ');saida.write(str('%5.4f'%V_vt));saida.write('  |\n')
            saida.write('η vt ....................................       ');saida.write(str('%5.4f'%eta_vt));saida.write('  |\n')
            saida.write('C Lα vt .................................       ');saida.write(str('%5.4f'%C_Lavt));saida.write('  |\n')
            saida.write('τ r .....................................       ');saida.write(str('%5.4f'%tau_r));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('C nδr ....................................       ');saida.write(str('%5.4f'%self.C_ndr));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
    def graphs(self):
        x = np.array(range(-15,15))
        my_dpi=100
        # Definir tamanho da imagem em pixeis
        # Aileron
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)

        plt.plot(x,x*self.C_lB+self.C_lda*self.da,'k-',color='blue',label ='Clβ | +δa')
        plt.plot(x,x*self.C_lB,'k-',color='red',label ='Clβ')
        plt.plot(x,x*self.C_lB+self.C_lda*-self.da,'k-',color='green',label ='Clβ | -δa')

        plt.title("Deflexao dos ailerons")
        plt.grid(True)
        plt.xlabel("β")
        plt.ylabel("Cl")
        plt.legend()
        plt.savefig('graficos/AILERONS' + self.sufixo + '.png', format='png')
        # Profundor
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)

        plt.plot(x,x*self.C_ma+self.C_m0 + self.C_mde*self.de_mais,'k-',color='blue',label ='Cmα | +δe')
        plt.plot(x,x*self.C_ma+self.C_m0,'k-',color='red',label ='Cmα')
        plt.plot(x,x*self.C_ma+self.C_m0 + self.C_mde*self.de_menos,'k-',color='green',label ='Cmα | -δe')

        plt.title("Deflexao do profundor")
        plt.grid(True)
        plt.xlabel("α")
        plt.ylabel("Cm")
        plt.legend()
        plt.savefig('graficos/PROFUNDOR' + self.sufixo + '.png', format='png')
        # Leme
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)

        plt.plot(x,x*self.C_nB+ self.C_ndr*self.dr,'k-',color='blue',label ='Cnβ | +δr')
        plt.plot(x,x*self.C_nB,'k-',color='red',label ='Cnβ')
        plt.plot(x,x*self.C_nB+self.C_ndr*-self.dr,'k-',color='green',label ='Cnβ | -δr')

        plt.title("Deflexao do leme")
        plt.grid(True)
        plt.xlabel("β")
        plt.ylabel("Cn")
        plt.legend()
        plt.savefig('graficos/LEME' + self.sufixo + '.png', format='png')
