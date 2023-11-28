class PedidoCifrado():
    def __init__(self, pedido, key, iv):
        self.pedido = pedido.decode("latin-1")
        self.key = key.decode("latin-1")
        self.iv = iv.decode("latin-1")

    def __dict__(self):
        return {"Pedido" : self.pedido, "Cipher_key":self.key, "Cipher_IV":self.iv}
