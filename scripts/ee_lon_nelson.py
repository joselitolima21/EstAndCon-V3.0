import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs,sufixo):
        self.sufixo = sufixo
        self.inputs = inputs
    def outputs(self):
        C_macw = self.inputs['C_macw'];C_L0w = self.inputs['C_L0w'];x_CG = self.inputs['x_CG'] 
        x_AC = self.inputs['x_AC'];MAC_w = self.inputs['MAC_w'];C_Law = self.inputs['C_Law']
        AR_w = self.inputs['AR_w'];x_ht = self.inputs['x_ht'];S_ht = self.inputs['S_ht']
        S_w = self.inputs['S_w'];C_macht = self.inputs['C_macht'];eta_ht = self.inputs['eta_ht']
        C_L0ht = self.inputs['C_L0ht'];C_Laht = self.inputs['C_Laht'];i_ht = self.inputs['i_ht']
        i_w = self.inputs['i_w']

        x_CG_CFCA = 0.352356*MAC_w
        x_CG_BD = 0.357961*MAC_w
        x_CG_CF = 0.375885*MAC_w 

        #Asa
        #   30%
        self.C_m0w_31 = C_macw + C_L0w * (x_CG - x_AC) / MAC_w
        self.C_maw_31 = C_Law * (x_CG - x_AC) / MAC_w
        #   BD%
        self.C_m0w_bd = C_macw + C_L0w * ( x_CG_BD - x_AC) / MAC_w
        self.C_maw_bd = C_Law * (x_CG_BD - x_AC) / MAC_w
        #   CF%
        self.C_m0w_cf = C_macw + C_L0w * (x_CG_CF - x_AC) / MAC_w
        self.C_maw_cf = C_Law * (x_CG_CF - x_AC) / MAC_w
        #   CF-CA%
        self.C_m0w_cfca = C_macw + C_L0w * (x_CG_CFCA - x_AC) / MAC_w
        self.C_maw_cfca = C_Law * (x_CG_CFCA - x_AC) / MAC_w
        #Estabilizador horizontal
        e0 = (2*C_L0w*180) / (np.pi**2 * AR_w)
        de_da = (2*C_Law*180) / (np.pi**2 * AR_w)
        V_ht = (x_ht * S_ht) / (MAC_w * S_w)
        self.C_m0ht = C_macht * eta_ht * S_ht/S_w - ( C_L0ht + C_Laht*(i_ht - i_w - e0) ) * eta_ht * V_ht
        self.C_maht = - eta_ht * V_ht * C_Laht * (1-de_da)
        #Fuselagem
        self.C_m0f = -0.016
        self.C_maf = 0.0009
        #Aviao Completo
        #   31%
        self.C_m0_31 = self.C_m0w_31 + self.C_m0ht + self.C_m0f
        self.C_ma_31 = self.C_maw_31 + self.C_maht + self.C_maf
        alfatrim_31 = -self.C_m0_31/self.C_ma_31
        #   BD%
        self.C_m0_bd = self.C_m0w_bd + self.C_m0ht + self.C_m0f
        self.C_ma_bd = self.C_maw_bd + self.C_maht + self.C_maf
        alfatrim_bd = -self.C_m0_bd/self.C_ma_bd
        #   CF%
        self.C_m0_cf = self.C_m0w_cf + self.C_m0ht + self.C_m0f
        self.C_ma_cf = self.C_maw_cf + self.C_maht + self.C_maf
        alfatrim_cf = -self.C_m0_cf/self.C_ma_cf
        #   CF-CA%
        self.C_m0_cfca = self.C_m0w_cfca + self.C_m0ht + self.C_m0f
        self.C_ma_cfca = self.C_maw_cfca + self.C_maht + self.C_maf
        alfatrim_cfca = -self.C_m0_cfca/self.C_ma_cfca
        with open('resultados/E.E.LON-NELSON'+ self.sufixo +'.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE ESTÁTICA LONGITUDINAL                    |\n')
            saida.write('| METODOLOGIA: NELSON                                   |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  C Lα w ..................................    ');saida.write(str('%5.4f'%C_Law));saida.write('  |\n')
            saida.write('|  C L0 w ..................................    ');saida.write(str('%5.4f'%C_L0w));saida.write('  |\n')
            saida.write('|  C mac w .................................   ');saida.write(str('%5.4f'%C_macw));saida.write('  |\n')
            saida.write('|  c w .....................................    ');saida.write(str('%5.4f'%MAC_w));saida.write('  |\n')
            saida.write('|  x CG 31% ................................    ');saida.write(str('%5.4f'%x_CG));saida.write('  |\n')
            saida.write('|  x AC ....................................    ');saida.write(str('%5.4f'%x_AC));saida.write('  |\n')
            saida.write('|  C Lα ht .................................    ');saida.write(str('%5.4f'%C_Laht));saida.write('  |\n')
            saida.write('|  C L0 ht .................................    ');saida.write(str('%5.4f'%C_L0ht));saida.write('  |\n')
            saida.write('|  C mac ht ................................    ');saida.write(str('%5.4f'%C_macht));saida.write('  |\n')
            saida.write('|  η ht ....................................    ');saida.write(str('%5.4f'%eta_ht));saida.write('  |\n')
            saida.write('|  S ht ....................................    ');saida.write(str('%5.4f'%S_ht));saida.write('  |\n')
            saida.write('|  S w .....................................    ');saida.write(str('%5.4f'%S_w));saida.write('  |\n')
            saida.write('|  i w .....................................    ');saida.write(str('%5.4f'%i_w));saida.write('  |\n')
            saida.write('|  i ht ....................................    ');saida.write(str('%5.4f'%i_ht));saida.write('  |\n')
            saida.write('|  x ht ....................................    ');saida.write(str('%5.4f'%x_ht));saida.write('  |\n')
            saida.write('|  AR w ....................................    ');saida.write(str('%5.4f'%AR_w));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('|  ε 0 .....................................    ');saida.write(str('%5.4f'%e0));saida.write('  |\n')
            saida.write('|  dε/dα ...................................    ');saida.write(str('%5.4f'%de_da));saida.write('  |\n')
            saida.write('|  V ht ....................................    ');saida.write(str('%5.4f'%V_ht));saida.write('  |\n')
            saida.write('|  C mα w cfca% ..............................    ');saida.write(str('%5.4f'%self.C_maw_cfca));saida.write('  |\n')
            saida.write('|  C m0 w cfca% ..............................    ');saida.write(str('%5.4f'%self.C_m0w_cfca));saida.write('  |\n')
            saida.write('|  C mα w bd% ..............................    ');saida.write(str('%5.4f'%self.C_maw_bd));saida.write('  |\n')
            saida.write('|  C m0 w bd% ..............................    ');saida.write(str('%5.4f'%self.C_m0w_bd));saida.write('  |\n')
            saida.write('|  C mα w cf% ..............................    ');saida.write(str('%5.4f'%self.C_maw_cf));saida.write('  |\n')
            saida.write('|  C m0 w cf% ..............................    ');saida.write(str('%5.4f'%self.C_m0w_cf));saida.write('  |\n')
            saida.write('|  C mα ht .................................    ');saida.write(str('%5.4f'%self.C_maht));saida.write('  |\n')
            saida.write('|  C m0 ht .................................    ');saida.write(str('%5.4f'%self.C_m0ht));saida.write('  |\n')
            saida.write('|  C mα f ..................................    ');saida.write(str('%5.4f'%self.C_maf));saida.write('  |\n')
            saida.write('|  C m0 f ..................................    ');saida.write(str('%5.4f'%self.C_m0f));saida.write('  |\n')
            saida.write('|  α trim cfca% ..............................    ');saida.write(str('%5.4f'%alfatrim_cfca));saida.write('  |\n')
            saida.write('|  α trim bd% ..............................    ');saida.write(str('%5.4f'%alfatrim_bd));saida.write('  |\n')
            saida.write('|  α trim cf% ..............................    ');saida.write(str('%5.4f'%alfatrim_cf));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('|  C mα cfca% ................................    ');saida.write(str('%5.4f'%self.C_ma_cfca,));saida.write('  |\n')
            saida.write('|  C m0 cfca% ................................    ');saida.write(str('%5.4f'%self.C_m0_cfca,));saida.write('  |\n')
            saida.write('|  C mα bd% ................................    ');saida.write(str('%5.4f'%self.C_ma_bd,));saida.write('  |\n')
            saida.write('|  C m0 bd% ................................    ');saida.write(str('%5.4f'%self.C_m0_bd,));saida.write('  |\n')
            saida.write('|  C mα cf% ................................    ');saida.write(str('%5.4f'%self.C_ma_cf,));saida.write('  |\n')
            saida.write('|  C m0 cf% ................................    ');saida.write(str('%5.4f'%self.C_m0_cf,));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+')
    def graphs(self):
        x = np.array(range(-15,15))
        my_dpi=100
        # Definir tamanho da imagem em pixeis
        # Detalhado
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)

        #plt.plot(x,x*self.C_maw_31+self.C_m0w_31,'k-',color='green',label ='Cmαw 31%')
        #plt.plot(x,x*self.C_maht+self.C_m0ht,'k-',color='red',label = 'Cmαht')
        #plt.plot(x,x*self.C_maf+self.C_m0f,'k-',color='blue',label = 'Cmαf')
        #plt.plot(x,x*self.C_ma_31+self.C_m0_31,'k-',color='yellow',label = 'Cmα 31%')

        plt.plot(x,x*self.C_maw_31+self.C_m0w_31,'k-',color='green',label ='Cmαw')
        plt.plot(x,x*self.C_maht+self.C_m0ht,'k-',color='red',label = 'Cmαht')
        plt.plot(x,x*self.C_maf+self.C_m0f,'k-',color='blue',label = 'Cmαf')
        plt.plot(x,x*self.C_ma_31+self.C_m0_31,'k-',color='black',label = 'Cmα')   

        #plt.plot(x,x*self.C_maw_40+self.C_m0w_40,'k-',color='green',label ='Cmαw 40%')
        #plt.plot(x,x*self.C_maht+self.C_m0ht,'k-',color='red',label = 'Cmαht')
        #plt.plot(x,x*self.C_maf+self.C_m0f,'k-',color='blue',label = 'Cmαf')
        #plt.plot(x,x*self.C_ma_40+self.C_m0_40,'k-',color='yellow',label = 'Cmα 40%')   

        plt.title("Estabilidade Estatica Longitudinal")
        plt.grid(True)
        plt.xlabel("α")
        plt.ylabel("Cm")
        plt.legend()
        plt.savefig('graficos/E.E.LON-NELSON-DETALHADO' + self.sufixo + '.png', format='png')
        # Geral
        plt.figure(figsize=(800/my_dpi, 600/my_dpi), dpi=my_dpi)
        plt.plot(x,x*self.C_ma_cfca+self.C_m0_cfca,'k-',color='blue',label = 'Cmα 35.23% - C.F-C.A.')
        plt.plot(x,x*self.C_ma_bd+self.C_m0_bd,'k-',color='red',label = 'Cmα 35.79% - B.D')   
        plt.plot(x,x*self.C_ma_cf+self.C_m0_cf,'k-',color='green',label = 'Cmα 37.58% - C.F.')     

        plt.title("Estabilidade Estatica Longitudinal")
        plt.grid(True)
        plt.xlabel("α")
        plt.ylabel("Cm")
        plt.legend()
        plt.savefig('graficos/E.E.LON-NELSON-GERAL' + self.sufixo + '.png', format='png')
    def valor(self):
        return self.C_m0_31,self.C_ma_31