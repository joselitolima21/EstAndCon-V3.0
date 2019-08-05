import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs,sufixo):
        self.sufixo = sufixo
        self.inputs = inputs
    def outputs(self):
        K_B = self.inputs['K_B'];h14f = self.inputs['h14f'];S_fs = self.inputs['S_fs']
        l_fs = self.inputs['l_fs'];h34f = self.inputs['h34f'];b_w = self.inputs['b_w']
        w34f = self.inputs['w34f'];S_w = self.inputs['S_w'];S_vt = self.inputs['S_vt']
        lambda_w = self.inputs['lambda_w'];w14f = self.inputs['w14f'];eta_vt = self.inputs['eta_vt']
        x_vt = self.inputs['x_vt'];C_Lavt = self.inputs['C_Lavt'];D_p = self.inputs['D_p']
        x_p = self.inputs['x_p'];N_p = self.inputs['N_p'];dCyp_dpsi = self.inputs['dCyp_dpsi']
        self.C_npsiw = -0.00006*np.sqrt(lambda_w)
        self.C_npsif = (0.96*K_B*S_fs*l_fs) / (57.3*S_w*b_w) * (h14f/h34f)**(0.5) * (w34f/w14f)**(0.33333333)
        self.C_npsiwf = -0.0002
        self.C_npsip = 1.5 * (np.pi * D_p**2 * x_p * N_p * dCyp_dpsi) / (4*S_w*b_w)
        self.C_npsivt = - (C_Lavt * S_vt * x_vt * eta_vt) / (S_w * b_w)
        self.C_npsi = self.C_npsiw + self.C_npsif + self.C_npsiwf + self.C_npsip + self.C_npsivt
        with open('resultados/E.E.DIR-PERKINS' + self.sufixo + '.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE ESTÁTICA DIRECIONAL                      |\n')
            saida.write('| METODOLOGIA: PERKINS                                  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  Λ w .....................................    ');saida.write(str('%5.4f'%lambda_w));saida.write('  |\n')
            saida.write('|  K β .....................................    ');saida.write(str('%5.4f'%K_B));saida.write('  |\n')
            saida.write('|  S fs ....................................    ');saida.write(str('%5.4f'%S_fs));saida.write('  |\n')
            saida.write('|  l fs ....................................    ');saida.write(str('%5.4f'%l_fs));saida.write('  |\n')
            saida.write('|  S w .....................................    ');saida.write(str('%5.4f'%S_w));saida.write('  |\n')
            saida.write('|  b w .....................................    ');saida.write(str('%5.4f'%b_w));saida.write('  |\n')
            saida.write('|  h 1/4f ..................................    ');saida.write(str('%5.4f'%h14f));saida.write('  |\n')
            saida.write('|  h 3/4f ..................................    ');saida.write(str('%5.4f'%h34f));saida.write('  |\n')
            saida.write('|  w 1/4f ..................................    ');saida.write(str('%5.4f'%w14f));saida.write('  |\n')
            saida.write('|  w 3/4f ..................................    ');saida.write(str('%5.4f'%w34f));saida.write('  |\n')
            saida.write('|  D_p .....................................    ');saida.write(str('%5.4f'%D_p));saida.write('  |\n')
            saida.write('|  x_p .....................................    ');saida.write(str('%5.4f'%x_p));saida.write('  |\n')
            saida.write('|  N_p .....................................    ');saida.write(str('%5.4f'%N_p));saida.write('  |\n')
            saida.write('|  dCyp / dψ ...............................    ');saida.write(str('%5.4f'%dCyp_dpsi));saida.write('  |\n')
            saida.write('|  C Lα vt .................................    ');saida.write(str('%5.4f'%C_Lavt));saida.write('  |\n')
            saida.write('|  S vt ....................................    ');saida.write(str('%5.4f'%S_vt));saida.write('  |\n')
            saida.write('|  x vt ....................................    ');saida.write(str('%5.4f'%x_vt));saida.write('  |\n')
            saida.write('|  η vt ....................................    ');saida.write(str('%5.4f'%eta_vt));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  C nΨ w ..................................   ');saida.write(str('%5.4f'%self.C_npsiw));saida.write('  |\n')
            saida.write('|  C nΨ f ..................................    ');saida.write(str('%5.4f'%self.C_npsif));saida.write('  |\n')
            saida.write('|  C nΨ wf .................................   ');saida.write(str('%5.4f'%self.C_npsiwf));saida.write('  |\n')
            saida.write('|  C nΨ p ..................................    ');saida.write(str('%5.4f'%self.C_npsip));saida.write('  |\n')
            saida.write('|  C nΨ vt .................................   ');saida.write(str('%5.4f'%self.C_npsivt));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|  C nΨ ....................................   ');saida.write(str('%5.4f'%self.C_npsi));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
    def graphs(self):
        x = np.array(range(-15,15))
        my_dpi=100
        # Definir tamanho da imagem em pixeis
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(x,x*self.C_npsi,'k-',color='black',label ='Cnψ')
        plt.plot(x,x*self.C_npsiw,'k-',color='red',label = 'Cnψw')
        plt.plot(x,x*self.C_npsiwf,'k-',color='green',label = 'Cnψwf')
        plt.plot(x,x*self.C_npsif,'k-',color='magenta',label = 'Cnψf')
        plt.plot(x,x*self.C_npsivt,'k-',color='yellow',label = 'Cnψvt')
        plt.plot(x,x*self.C_npsip,'k-',color='blue',label = 'Cnψp')
        plt.title("Estabilidade Estatica Direcional")
        plt.grid(True)
        plt.xlabel("ψ")
        plt.ylabel("Cn")
        plt.legend()
        plt.savefig('graficos/E.E.DIR-PERKINS' + self.sufixo + '.png', format='png')