import numpy as np
import matplotlib.pyplot as plt
class Aviao():
    def __init__(self,inputs):
        self.inputs = inputs
    def outputs(self):
        C_L0w = self.inputs['C_L0w'];MAC_w = self.inputs['MAC_w'];C_Law = self.inputs['C_Law'];x_ht = self.inputs['x_ht']
        u_0 = self.inputs['u_0'];S_w = self.inputs['S_w'];eta_ht = self.inputs['eta_ht'];C_Laht = self.inputs['C_Laht']
        rho = self.inputs['rho'];C_D0 = self.inputs['C_D0'];S_vt = self.inputs['S_vt']
        AR_w = self.inputs['AR_w'];b_w = self.inputs['b_w'];S_w = self.inputs['S_w'];S_vt = self.inputs['S_vt']
        lambda_w = self.inputs['lambda_w'];eta_vt = self.inputs['eta_vt'];Ix = self.inputs['Ix']
        Iy = self.inputs['Iy'];Iz = self.inputs['Iz'];m = self.inputs['m'];C_Lavt = self.inputs['C_Lavt']
        lambda2_w = self.inputs['lambda2_w'];x_vt = self.inputs['x_vt'];z_vt = self.inputs['z_vt']
        S_ht = self.inputs['S_ht'];z_w = self.inputs['z_w'];w_maxf = self.inputs['w_maxf']
        teta_0 = self.inputs['teta_0'];g = 9.8;k_n = self.inputs['k_n'];k_Rl = self.inputs['k_Rl']
        S_fs = self.inputs['S_fs'];l_fs = self.inputs['l_fs'];x_CG = self.inputs['x_CG'];x_AC = self.inputs['x_AC']
        gamma_w = self.inputs['gamma_w'];h_medf = self.inputs['h_medf'];w_medf = self.inputs['w_medf'];C_lBw_CL = self.inputs['C_lBw_CL']
       
        self.C_nBwf = - k_n * k_Rl * (S_fs * l_fs) / (S_w * b_w)
        do_dB = (0.724+3.06*(S_vt/S_w)/(1+np.cos(lambda_w)) + 0.4*z_w/w_maxf+0.009*AR_w)/eta_vt - 1
        V_vt = (x_vt * S_vt) / (b_w * S_w)
        self.C_nBvt = V_vt * C_Lavt * eta_vt * (1 + do_dB)
        self.C_nB = self.C_nBwf + self.C_nBvt
        #Asa
        self.C_maw = C_Law * (x_CG - x_AC) / MAC_w
        #Estabilizador horizontal
        de_da = (2*C_Law*180) / (np.pi**2 * AR_w)
        V_ht = (x_ht * S_ht) / (MAC_w * S_w)
        self.C_maht = - eta_ht * V_ht * C_Laht * (1-de_da)
        #Fuselagem
        self.C_maf = 0.0009
        #Aviao Completo
        self.C_ma = self.C_maw + self.C_maht + self.C_maf

        self.C_lBgamma = - (C_Law * gamma_w *2* (1+2*lambda2_w)) / ( 4*3*(1+lambda2_w))
        self.C_lBwf = -1.2 * np.sqrt(AR_w) * z_w * (h_medf + w_medf) / (b_w**2)
        self.C_lBlambda = C_lBw_CL * np.pi / 180 * C_Law
        self.C_lB = self.C_lBgamma + self.C_lBwf + self.C_lBlambda
        
        #Valores necessarios
        Q = 0.5*rho*u_0**2
        Mach = u_0/348
        e = 0.9581
        V_ht = (x_ht * S_ht) / (MAC_w * S_w)
        V_vt = (x_vt * S_vt) / (b_w * S_w)
        de_da = (2*C_Law*180) / (np.pi**2 * AR_w)
        do_dB = (0.724+3.06*(S_vt/S_w)/(1+np.cos(lambda_w)) + 0.4*z_w/w_maxf+0.009*AR_w)/eta_vt - 1
        #COEFICIENTES ADIMENSIONAIS
        C_Xu = -3*C_D0 ; C_Zu = -C_L0w*(Mach**2/(1-Mach**2) + 2) ; C_Mu = 0
        C_Xa = C_L0w*(1 - (2*C_Law)/(np.pi*e*AR_w)) ; C_Za = -(C_Law + C_D0) #C_ma
        C_Xap = 0 ; C_Zap = -2*C_Laht*eta_ht*V_ht*de_da*1.1 ; C_Map = C_Zap * x_ht/MAC_w
        C_Xq = 0 ; C_Zq = -2*C_Laht*eta_ht*V_ht*1.1 ; C_Mq = C_Zq*x_ht/MAC_w
        C_YB = S_vt/S_w * C_Lavt*(-eta_vt*(1+do_dB)) ; #C_nB ; #C_lB
        C_Yp = C_L0w*((AR_w+np.cos(lambda_w)) / (AR_w+4*np.cos(lambda_w)))*np.tan(lambda_w) ; C_Np = -C_L0w/8 ; C_lp = -C_Law/12*(1+3*lambda2_w)/(1+lambda2_w)
        C_Yr = -2*C_YB*x_vt/b_w ; C_Nr = -2*eta_vt*V_vt*x_vt/b_w*C_Lavt ; C_lr = C_L0w/4 - 2*x_vt/b_w*z_vt/b_w*C_YB
        #COEFICIENTES DIMENSIONAIS
        Xu = C_Xu * (Q*S_w)/(u_0*m) ; Zu = C_Zu * (Q*S_w)/(u_0*m) ; Mu = C_Mu * (Q*S_w*MAC_w)/(u_0*Iy)
        Xw = C_Xa * (Q*S_w)/(u_0*m) ; Zw = C_Za * (Q*S_w)/(u_0*m) ; Mw = self.C_ma * (Q*S_w*MAC_w)/(u_0*Iy)
        Xwp = 0 ; Zwp = C_Zap * (Q*S_w*MAC_w)/(2*u_0**2*m) ; Mwp = C_Map * (Q*S_w*MAC_w**2)/(2*u_0**2*Iy)
        Xa = 0  #Xw * (u_0)
        Za = Zw * (u_0) ; Ma = Mw * (u_0)
        Xap = 0 ; Zap = Zwp * (u_0) ; Map = Mwp * (u_0)
        Xq = 0 ; Zq = C_Zq * (Q*S_w*MAC_w)/(2*u_0*m) ; Mq = C_Mq * (Q*S_w*MAC_w**2)/(2*u_0*Iy)
        YB = C_YB * (Q*S_w)/(m) ; NB = self.C_nB * (Q*S_w*b_w)/(Iz) ; LB = self.C_lB * (Q*S_w*b_w)/(Ix)
        Yp = C_Yp * (Q*S_w*b_w)/(2*u_0*m) ; Np = C_Np * (Q*S_w*b_w**2)/(2*u_0*Iz) ; Lp = C_lp * (Q*S_w*b_w**2)/(2*u_0*Ix)
        Yr = C_Yr * (Q*S_w*b_w)/(2*u_0*m) ; Nr = C_Nr * (Q*S_w*b_w**2)/(2*u_0*Iz) ; Lr = C_lr * (Q*S_w*b_w**2)/(2*u_0*Ix)
        #Matriz Longitudinal
        M_Long = np.zeros([4,4])
        M_Long[0,0] = Xu         ; M_Long[0,1] = Xw 
        M_Long[0,2] = 0          ; M_Long[0,3] = -g
        M_Long[1,0] = Zu         ; M_Long[1,1] = Zw
        M_Long[1,2] = u_0        ; M_Long[1,3] = 0
        M_Long[2,0] = Mu+Mwp*Zu  ; M_Long[2,1] = Mw+Mwp*Zw
        M_Long[2,2] = Mq+Mwp*u_0 ; M_Long[2,3] = 0
        M_Long[3,0] = 0          ; M_Long[3,1] = 0
        M_Long[3,2] = 1          ; M_Long[3,3] = 0
        #Matriz Latero-Direcional
        M_LatDir = np.zeros([4,4])
        M_LatDir[0,0] = YB/u_0      ; M_LatDir[0,1] = Yp/u_0
        M_LatDir[0,2] = -(1-Yr/u_0) ; M_LatDir[0,3] = g*np.cos(teta_0)/u_0
        M_LatDir[1,0] = LB          ; M_LatDir[1,1] = Lp
        M_LatDir[1,2] = Lr          ; M_LatDir[1,3] = 0
        M_LatDir[2,0] = NB          ; M_LatDir[2,1] = Np
        M_LatDir[2,2] = Nr          ; M_LatDir[2,3] = 0
        M_LatDir[3,0] = 0           ; M_LatDir[3,1] = 1
        M_LatDir[3,2] = 0           ; M_LatDir[3,3] = 0


        with open('resultados/E.D.COEFICIENTES LONGITUDINAL.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE DINÂMICA LONGITUDINAL                    |\n')
            saida.write('| METODOLOGIA: NELSON                                   |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('| ρ .......................................     ');saida.write(str('%5.4f'%rho));saida.write('  |\n')
            saida.write('| u 0 .....................................     ');saida.write(str('%5.3f'%u_0));saida.write('  |\n')
            saida.write('| m .......................................     ');saida.write(str('%5.4f'%m));saida.write('  |\n')
            saida.write('| θ 0 .....................................     ');saida.write(str('%5.4f'%teta_0));saida.write('  |\n')
            saida.write('| Ix ......................................     ');saida.write(str('%5.4f'%Ix));saida.write('  |\n')
            saida.write('| Iy ......................................     ');saida.write(str('%5.4f'%Iy));saida.write('  |\n')
            saida.write('| Iz ......................................     ');saida.write(str('%5.4f'%Iz));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('| Q .......................................     ');saida.write(str('%5.2f'%Q));saida.write('  |\n')
            saida.write('| Mach ....................................     ');saida.write(str('%5.4f'%Mach));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('| COEFICIENTES ADIMENSIONAIS:                           |\n')
            saida.write('|                                                       |\n')
            saida.write('|           |      X      |      Z      |      M        |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| u            ');saida.write(str('%5.4f'%C_Xu));saida.write('        '+str('%5.4f'%C_Zu));saida.write('        '+str('%5.4f'%C_Mu));saida.write('     |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| α            ');saida.write(str('%5.4f'%C_Xa));saida.write('        '+str('%5.4f'%C_Za));saida.write('        '+str('%5.4f'%self.C_ma));saida.write('     |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| α p          ');saida.write(str('%5.4f'%C_Xap));saida.write('        '+str('%5.4f'%C_Zap));saida.write('        '+str('%5.4f'%C_Map));saida.write('     |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| q            ');saida.write(str('%5.4f'%C_Xq));saida.write('        '+str('%5.4f'%C_Zq));saida.write('        '+str('%5.4f'%C_Mq));saida.write('     |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
        #   saida.write('| COEFICIENTES DIMENSIONAIS:                            |\n')
        #   saida.write('|                                                       |\n')
        #   saida.write('|           |      X      |      Z      |      M        |\n')
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #saida.write('u  ', Xu , Zu , Mu
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #saida.write('w  ', Xw , Zw , Mw
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #saida.write('w p', Xwp , Zwp , Mwp
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #saida.write('α  ', Xa , Za , Ma
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #saida.write('α p', Xap, Zap, Map
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #saida.write('q  ', Xq , Zq , Mq
        #   saida.write('| ---------  ------------- ------------- -------------  |\n')
        #   saida.write('|                                                       |\n')
        

        with open('resultados/E.D.COEFICIENTES LATERO-DIRECIONAIS.txt','w',encoding="utf-8") as saida:
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                                                       |\n')
            saida.write('| ESTABILIDADE DINÂMICA LONGITUDINAL                    |\n')
            saida.write('| METODOLOGIA: NELSON                                   |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                         INPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('| ρ .......................................     ');saida.write(str('%5.4f'%rho));saida.write('  |\n')
            saida.write('| u 0 .....................................     ');saida.write(str('%5.3f'%u_0));saida.write('  |\n')
            saida.write('| m .......................................     ');saida.write(str('%5.4f'%m));saida.write('  |\n')
            saida.write('| θ 0 .....................................     ');saida.write(str('%5.4f'%teta_0));saida.write('  |\n')
            saida.write('| Ix ......................................     ');saida.write(str('%5.4f'%Ix));saida.write('  |\n')
            saida.write('| Iy ......................................     ');saida.write(str('%5.4f'%Iy));saida.write('  |\n')
            saida.write('| Iz ......................................     ');saida.write(str('%5.4f'%Iz));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
            saida.write('|                        OUTPUTs                        |\n')
            saida.write('|                                                       |\n')
            saida.write('| Q .......................................     ');saida.write(str('%5.2f'%Q));saida.write('  |\n')
            saida.write('| Mach ....................................     ');saida.write(str('%5.4f'%Mach));saida.write('  |\n')
            saida.write('|                                                       |\n')
            saida.write('| COEFICIENTES ADIMENSIONAIS:                           |\n')
            saida.write('|                                                       |\n')
            saida.write('|           |      Y      |      N      |      L        |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| β            ');saida.write(str('%5.4f'%C_YB));saida.write('        '+str('%5.4f'%self.C_nB));saida.write('        '+str('%5.4f'%self.C_lB));saida.write('     |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| P            ');saida.write(str('%5.4f'%C_Yp));saida.write('        '+str('%5.4f'%C_Np));saida.write('        '+str('%5.4f'%C_lp));saida.write('     |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('| r            ');saida.write(str('%5.4f'%C_Yr));saida.write('        '+str('%5.4f'%C_Nr));saida.write('        '+str('%5.4f'%C_lr));saida.write('      |\n')
            saida.write('| ---------  ------------- ------------- -------------  |\n')
            saida.write('|                                                       |\n')
            saida.write('+-------------------------------------------------------+\n')
        return M_Long,M_LatDir
       
        
    
        

