import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs,sufixo):
        self.sufixo = sufixo
        self.inputs = inputs
    def outputs(self):
        C_lpsi_gamma_w = self.inputs['C_lpsi_gamma_w'];gamma_w = self.inputs['gamma_w']
        C_lpsits_w = self.inputs['C_lpsits_w'];C_Lavt = self.inputs['C_Lavt'];S_w = self.inputs['S_w']
        b_w = self.inputs['b_w'];S_vt = self.inputs['S_vt'];z_vt = self.inputs['z_vt']
        eta_vt = self.inputs['eta_vt']
        self.C_lpsiw = C_lpsi_gamma_w * gamma_w + C_lpsits_w
        self.C_lpsiwf = 0.0006
        self.C_lpsivt = C_Lavt * S_vt * z_vt * eta_vt / (S_w * b_w)
        self.C_lpsiwvt = 0.00016
        self.C_lpsi = self.C_lpsiw + self.C_lpsiwf + self.C_lpsivt + self.C_lpsiwvt
        with open('resultados/E.E.LAT-PERKINS' + self.sufixo + '.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE ESTÁTICA LATERAL                         |\n')
            saida.write('| METODOLOGIA: PERKINS                                  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  C lΨ / Γ w ..............................    ');saida.write(str('%5.4f'%C_lpsi_gamma_w));saida.write('  |\n')
            saida.write('|  Γ w .....................................    ');saida.write(str('%5.4f'%gamma_w));saida.write('  |\n')
            saida.write('|  ΔC lΨ ts,w ..............................    ');saida.write(str('%5.4f'%C_lpsits_w));saida.write('  |\n')
            saida.write('|  S w .....................................    ');saida.write(str('%5.4f'%S_w));saida.write('  |\n')
            saida.write('|  b w .....................................    ');saida.write(str('%5.4f'%b_w));saida.write('  |\n')
            saida.write('|  C Lα vt .................................    ');saida.write(str('%5.4f'%C_Lavt));saida.write('  |\n')
            saida.write('|  S vt ....................................    ');saida.write(str('%5.4f'%S_vt));saida.write('  |\n')
            saida.write('|  z vt ....................................    ');saida.write(str('%5.4f'%z_vt));saida.write('  |\n')
            saida.write('|  η vt ....................................    ');saida.write(str('%5.4f'%eta_vt));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  C lΨ w ..................................    ');saida.write(str('%5.4f'%self.C_lpsiw));saida.write('  |\n')
            saida.write('|  C lΨ wf .................................    ');saida.write(str('%5.4f'%self.C_lpsiwf));saida.write('  |\n')
            saida.write('|  C lΨ vt .................................    ');saida.write(str('%5.4f'%self.C_lpsivt));saida.write('  |\n')
            saida.write('|  C lΨ w vt ...............................    ');saida.write(str('%5.4f'%self.C_lpsiwvt));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|  C lΨ ....................................    ');saida.write(str('%5.4f'%self.C_lpsi));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
    def graphs(self):
        x = np.array(range(-15,15))
        my_dpi=100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(x,x*self.C_lpsi,'k-',color='black',label ='Clψ')
        plt.plot(x,x*self.C_lpsiw,'k-',color='red',label = 'Clψw')
        plt.plot(x,x*self.C_lpsiwf,'k-',color='green',label = 'Clψwf')
        plt.plot(x,x*self.C_lpsivt,'k-',color='yellow',label = 'Clψvt')
        plt.plot(x,x*self.C_lpsiwvt,'k-',color='blue',label = 'Clψwvt')
        plt.title("Estabilidade Estatica Lateral")
        plt.grid(True)
        plt.xlabel("ψ")
        plt.ylabel("Cl")
        plt.legend()
        plt.savefig('graficos/E.E.LAT-PERKINS' + self.sufixo + '.png', format='png')