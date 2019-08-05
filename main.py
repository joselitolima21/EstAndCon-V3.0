import scripts.ee_lon_nelson as nelsonLON
import scripts.ee_lat_perkins as perkinsLAT
import scripts.ee_lat_raymer as raymerLAT
import scripts.ee_dir_nelson as nelsonDIR
import scripts.ee_dir_perkins as perkinsDIR
import scripts.ed_coeficientes as coeDin
import scripts.ed_longitudinal as lonDin
import scripts.ed_lateral as latDin
import scripts.readInputs as ri
import scripts.controle as con
#Lendo os inputs
def readinputs():
    global inputs
    inputs = ri.inputs()
#Processando E.E Longitudinal Nelson
def longitudinalNelson(sufixo):
    global Cm
    lonNelson = nelsonLON.Aviao(inputs,sufixo)
    lonNelson.outputs()
    lonNelson.graphs()
    Cm = lonNelson.valor()
#Processando E.E Lateral PERKINS
def lateralPerkins(sufixo):
    latPerkins = perkinsLAT.Aviao(inputs,sufixo)
    latPerkins.outputs()
    latPerkins.graphs()
#Processando E.E Lateral RAYMER
def lateralRaymer(sufixo):
    global C_lB
    latRaymer = raymerLAT.Aviao(inputs,sufixo)
    latRaymer.outputs()
    latRaymer.graphs()
    C_lB = latRaymer.valor()
#Processando E.E Direcional NELSON
def direcionalNelson(sufixo):
    global C_nB
    dirNelson = nelsonDIR.Aviao(inputs,sufixo)
    dirNelson.outputs()
    dirNelson.graphs()
    C_nB = dirNelson.valor()
#Processando E.E Direcional PERKINS
def direcionalPerkins(sufixo):
    dirPerkins = perkinsDIR.Aviao(inputs,sufixo)
    dirPerkins.outputs()
    dirPerkins.graphs()
#Processando E.D COEFICIENTES
def coe():
    din = coeDin.Aviao(inputs)
    global matrizes
    matrizes = din.outputs()
#Processando E.D LONGITUDINAL 
def longitudinalDinamica(sufixo,):
    dinLON = lonDin.Aviao(matrizes[0],sufixo)
    dinLON.graphs()
#Processando E.D LATERAL 
def laterodirecionalDinamica(sufixo):
    dinLAT = latDin.Aviao(matrizes[1],sufixo)
    dinLAT.graphs()
#Processando CONTROLE
def controle(sufixo):
    conT = con.Aviao(inputs,sufixo,Cm,C_nB,C_lB)
    conT.outputs()
    conT.graphs()
