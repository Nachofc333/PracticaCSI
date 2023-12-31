from interfaces.PedidoR1W import Ui_Pedido1
from interfaces.PedidoR2W import Ui_Pedido2
from interfaces.PedidoR3W import Ui_Pedido3
from interfaces.PedidoR4W import Ui_Pedido4

from PyQt5 import QtWidgets
import json
from PyQt5.QtWidgets import QMessageBox
from pedido.pedido import Pedido
from pedido.pedidoCifrado import PedidoCifrado
from restaurantes.restaurante1.jsonAlmacenPedidos1 import JsonAlmacenPedidos1
from restaurantes.restaurante2.jsonAlmacenPedidos2 import JsonAlmacenPedidos2
from restaurantes.restaurante3.jsonAlmacenPedidos3 import JsonAlmacenPedidos3
from restaurantes.restaurante4.jsonAlmacenPedidos4 import JsonAlmacenPedidos4
from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
from controladores.controladorRestaurantes import Controlador_restaurante



class Controlador_pedido(QtWidgets.QMainWindow):
    def __init__(self, user, restaurante):
        super().__init__()
        self.user = user
        self.restaurante = restaurante
        if self.restaurante == "Restaurante1":
            self.ui=Ui_Pedido1()
        elif self.restaurante == "Restaurante2":
            self.ui=Ui_Pedido2()
        elif self.restaurante == "Restaurante3":
            self.ui = Ui_Pedido3()
        elif self.restaurante == "Restaurante4":
            self.ui=Ui_Pedido4()
        self.ui.setupUi(self)
        self.InicializarGui()
        self.controlador_restaurantes = Controlador_restaurante()
        self.almacen1 = JsonAlmacenPedidos1()
        self.almacen2 = JsonAlmacenPedidos2()
        self.almacen3 = JsonAlmacenPedidos3()
        self.almacen4 = JsonAlmacenPedidos4()

    def InicializarGui(self):
        self.ui.EnviarPedido.clicked.connect(self.ComprobarRestaurante)
        #self.ui.Pedidos.clicked.connect(self.IniciarRestaurantes)
        self.ui.Pedidos.clicked.connect(self.seleccionarrestaurante)

    def IniciarRestaurantes(self):
        self.close()

    def seleccionarrestaurante(self):
        self.close()

    def ComprobarRestaurante(self):
        restaurante = self.ui.SelectorRestaurante.currentText()
        if restaurante != "Selecciona restaurante":
            if self.comprobarPlatos():
                self.crearPedido()
        else:
            alerta = QMessageBox.information(self, 'Error', 'Selecciona un restaurante válido', QMessageBox.Ok)

    def comprobarPlatos(self):
        platos = [self.ui.Pasta.checkState(), self.ui.Filete.checkState(), self.ui.Lentejas.checkState(),
                  self.ui.Hamburguesa.checkState()]
        if not any(plato > 0 for plato in platos):
            QMessageBox.information(self, 'Error', 'Selecciona al menos un plato', QMessageBox.Ok)
            return False
        return True

    def crearPedido(self):
        restaurante = self.ui.SelectorRestaurante.currentText()
        pedido = Pedido(
            restaurante=self.restaurante,
            pasta = self.ui.Pasta.checkState() -1 if self.ui.Pasta.checkState() >0 else 0,
            filete = self.ui.Filete.checkState() -1 if self.ui.Filete.checkState() > 0 else 0,
            lentejas = self.ui.Lentejas.checkState() -1 if self.ui.Lentejas.checkState() > 0 else 0,
            hamburguesa = self.ui.Hamburguesa.checkState() -1 if self.ui.Hamburguesa.checkState() > 0 else 0,
            tarta = self.ui.Tarta.checkState() -1 if self.ui.Tarta.checkState() >0 else 0,
            brownie = self.ui.Brownie.checkState() -1 if self.ui.Brownie.checkState() else 0)
        ct, key, iv = self.user.encriptar(pedido)
        if ct:
            pedido_cifrado = PedidoCifrado(ct, key, iv)
            if self.restaurante == "Restaurante1":
                restaurante = Restaurante1()
                self.almacen1.add_item(pedido_cifrado)
            elif self.restaurante == "Restaurante2":
                restaurante = Restaurante2()
                self.almacen2.add_item(pedido_cifrado)
            elif self.restaurante == "Restaurante3":
                restaurante = Restaurante3()
                self.almacen3.add_item(pedido_cifrado)
            elif self.restaurante == "Restaurante4":
                restaurante = Restaurante4()
                self.almacen4.add_item(pedido_cifrado)
            self.terminar()

    def terminar(self):
        alerta = QMessageBox.information(self, 'Exito', 'Pedido realizado con éxito', QMessageBox.Ok)
        self.close()



