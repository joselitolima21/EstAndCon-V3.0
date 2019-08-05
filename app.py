from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QHBoxLayout,
                 QMessageBox, QGroupBox, QCheckBox, QVBoxLayout, QRadioButton, QLabel,QGridLayout)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import main
import os
import shutil
import sys
class Janela(QWidget):
    def executar(self):
        pasta = os.path.dirname(os.path.abspath(__file__))
        if os.path.isdir(pasta+'/graficos'):
            pass
        else:
            os.makedirs(pasta+'/graficos')
        if os.path.isdir(pasta+'/resultados'):
            pass
        else:
            os.makedirs(pasta+'/resultados')
        sufixo = self.tag.text()
        if self.delete.isChecked():
            sufixo = '' 
            print(pasta)
            shutil.rmtree(pasta+'/graficos')
            shutil.rmtree(pasta+'/resultados')
            os.makedirs(pasta+'/graficos')
            os.makedirs(pasta+'/resultados')
        elif self.ndelete.isChecked():
            if sufixo == '':
                sufixo = '-new'
            else:    
                sufixo = '-'+self.tag.text()
        main.readinputs()
        main.coe()
        menssagens = []
        if self.check1.isChecked(): #Longitudinal
            main.longitudinalNelson(sufixo)
            menssagens.append('E.E.LON-NELSON-OK\n')
        else: pass
        if self.check2.isChecked(): #Lateral Perkins
            main.lateralPerkins(sufixo)
            menssagens.append('E.E.LAT-PERKINS-OK\n')
        else: pass
        if self.check3.isChecked(): #Lateral Raymer
            main.lateralRaymer(sufixo)
            menssagens.append('E.E.LAT-RAYMER-OK\n')
        else: pass
        if self.check4.isChecked(): #Direcional Nelson
            main.direcionalNelson(sufixo)
            menssagens.append('E.E.DIR-NELSON-OK\n')
        else: pass
        if self.check5.isChecked(): #Direcional Perkins
            main.direcionalPerkins(sufixo)
            menssagens.append('E.E.DIR-PERKINS-OK\n')
        else: pass
        if self.check8.isChecked(): #Controle
            main.longitudinalNelson(sufixo)
            menssagens.append('E.E.LON-NELSON-OK\n')
            main.lateralRaymer(sufixo)
            menssagens.append('E.E.LAT-RAYMER-OK\n')
            main.direcionalNelson(sufixo)
            menssagens.append('E.E.DIR-NELSON-OK\n')
            main.controle(sufixo)
            menssagens.append('CONTROLE-OK\n')
        else: pass
        if self.check6.isChecked(): ##Longitudinal Dinamica
            main.longitudinalDinamica(sufixo)
            menssagens.append('E.DIN-LONGITUDINAL-OK\n')
        else: pass
        if self.check7.isChecked(): #Latero Direcional
            main.laterodirecionalDinamica(sufixo)
            menssagens.append('E.DIN-LATERAL-OK\n')
        else: pass
        texto = ''
        for i in menssagens:
            texto = texto + i 
        self.messsage_box = QMessageBox.information(self,'FeedBack',texto)
    def __init__(self):
        QWidget.__init__(self)
        #Janela
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.setWindowTitle('Sol do Equador - Stability Analysis')
        self.setMaximumSize(400,300)
        #Botao
        self.button = QPushButton('Calcular')
        self.button.clicked.connect(self.executar)
        #Juntar os Layouts
        self.groupboxEstatica = QGroupBox('Estática')
        self.groupboxDinamica = QGroupBox('Dinâmica')
        self.groupboxOperacionais = QGroupBox('Escolhas Operacionais')
        self.groupboxInfos = QGroupBox('Sobre')
        #Escolha de opcoes
        self.check1 = QCheckBox('Longitudinal - Nelson')
        self.check2 = QCheckBox('Lateral - Perkins')
        self.check3 = QCheckBox('Lateral - Raymer')
        self.check4 = QCheckBox('Direcional - Nelson')
        self.check5 = QCheckBox('Direcional - Perkins')
        self.check6 = QCheckBox('Longitudinal')
        self.check7 = QCheckBox('Latero - Direcional')
        self.check8 = QCheckBox('Controle')
        #Layout de escolhas de Estatica
        self.layout_estatica = QVBoxLayout()
        self.layout_estatica.addWidget(self.check1)
        self.layout_estatica.addWidget(self.check2)
        self.layout_estatica.addWidget(self.check3)
        self.layout_estatica.addWidget(self.check4)
        self.layout_estatica.addWidget(self.check5)
        self.layout_estatica.addWidget(self.check8)
        self.groupboxEstatica.setLayout(self.layout_estatica)
        #Layout de escolhas de Dinamica
        self.layout_dinamica = QVBoxLayout()
        self.layout_dinamica.addWidget(self.check6)
        self.layout_dinamica.addWidget(self.check7)
        self.groupboxDinamica.setLayout(self.layout_dinamica)
        #Layout do botao
        self.layout_button = QHBoxLayout()
        self.layout_button.addWidget(self.button)
        #Layout de escolhas operacionais
        self.delete = QRadioButton('Sobrescrever resultados anteriores')
        self.ndelete = QRadioButton('Manter resultados anteriores')
        self.dica = QLabel('Se escolher manter os arquivos\nDigite aqui um sufixo para diferencia-los')
        self.dica.setAlignment(Qt.AlignCenter)
        self.tag = QLineEdit()
        self.ndelete.setChecked(True)
        self.layout_operacionais = QVBoxLayout()
        self.layout_operacionais.addWidget(self.delete)
        self.layout_operacionais.addWidget(self.ndelete)
        self.layout_operacionais.addWidget(self.dica)
        self.layout_operacionais.addWidget(self.tag)
        self.groupboxOperacionais.setLayout(self.layout_operacionais)
        #Label
        text = """ESTABILIDADE E CONTROLE\nSOL DO EQUADOR AERODESIGN\nDESENVOLVIDO POR: JOSELITO, LENO, NETO, SAVIO\nINTEGRANTES DE ESTABILIDADE E CONTROLE - 2018\nSOFTWARE PARA USO INTERNO DA EQUIPE\nVer. 3.0"""
        self.layout_infos = QVBoxLayout()
        self.infos = QLabel(text)
        self.infos.setAlignment(Qt.AlignCenter)
        self.layout_infos.addWidget(self.infos)
        self.groupboxInfos.setLayout(self.layout_infos)
        #Layout Principal
        self.layout_1 = QGridLayout()
        self.layout_1.addWidget(self.groupboxEstatica,0,0)
        self.layout_1.addWidget(self.groupboxDinamica,1,0)
        self.layout_1.addWidget(self.groupboxOperacionais,0,1)
        self.layout_1.addWidget(self.groupboxInfos,1,1)
        self.layout_2 = QVBoxLayout()
        self.layout_2.addLayout(self.layout_1)
        self.layout_2.addLayout(self.layout_button)
        self.setLayout(self.layout_2)
if __name__ == "__main__":
    app = QApplication(sys.argv)    
    tela = Janela()
    tela.show()
    sys.exit(app.exec_())