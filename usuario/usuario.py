from restaurantes.restaurante1.Restaurante1 import Restaurante1
from restaurantes.restaurante2.Restaurante2 import Restaurante2
from restaurantes.restaurante3.Restaurante3 import Restaurante3
from restaurantes.restaurante4.Restaurante4 import Restaurante4
from cryptography.hazmat.primitives.asymmetric import padding as pd
import os
from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from CA.CAUsuarios.CAUsuarios import CAUsuarios
from CA.CAR.CAR import CAR
from CA.CARestaurante.CARestaurante import CARestaurante
from datetime import datetime


JSON_FILES_PATH = os.path.dirname(__file__)
now = datetime.utcnow()

class Usuario():
    def __init__(self, nombre, contraseña, telefono, salt):
        self.nombre = nombre
        self.contraseña = contraseña.decode('latin-1')
        self.telefono = telefono
        self.salt = salt.decode('latin-1')
        self._key = os.urandom(32)
        self.iv = os.urandom(16)
        self.cipherkey = ""
        self._key_rsa = self.leerkey()
        self.key_public = self._key_rsa.public_key()
        self.name = self.generarName()
        self.cert = self.requestCA()
        if not self.cert.not_valid_before <= now <= self.cert.not_valid_after:
            self.recargarCA()
        self.car = CAR()
        self.CARestaurante = CARestaurante()

    def __dict__(self):
        return {"nombre": self.nombre, "password": self.contraseña, "telefono": self.telefono, "salt":self.salt}

    def encriptariv(self, restaurante):
        pk_restaurante = restaurante.public_key
        self.ivencrip = pk_restaurante.encrypt(
            self.iv,
            pd.OAEP(
                mgf=pd.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        return self.ivencrip

    def encriptar(self, pedido):  # funcion encargada de buscar el restaurante al que se esta pidiendo, para obtener su PK
        restaurante_pedido = pedido.restaurante
        restaurante = None
        if restaurante_pedido == "Restaurante1":
            restaurante = Restaurante1()
        elif restaurante_pedido == "Restaurante2":
            restaurante = Restaurante2()
        elif restaurante_pedido == "Restaurante3":
            restaurante = Restaurante3()
        elif restaurante_pedido == "Restaurante4":
            restaurante = Restaurante4()
        else:
            print("error")
        if self.validarCertificados(self.car.cert, self.CARestaurante.cert, restaurante.cert):
            self.encriptarKEY(restaurante, self._key)  # llamada a encriptarKey, que encriptará la key con la PK del restaurante
            ct = self.encriptarPedido(pedido, restaurante, self._key, self.iv)  # pedido encriptado simetricamente
            if ct:
                return ct
        return False

    def encriptarPedido(self, pedido, restaurante, key, iv):  # funcion encargada de encriptar el pedido de forma simetrica

        h = hmac.HMAC(self._key, hashes.SHA256())
        h.update(str(pedido).encode('latin-1'))
        hash = h.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        # Crear un nuevo padder para el pedido
        padder_pedido = padding.PKCS7(128).padder()
        padded_data = padder_pedido.update(str(pedido).encode("latin-1")) + padder_pedido.finalize()
        ct = encryptor.update(padded_data) + encryptor.finalize()

        # Firmar el hash
        signature = self._key_rsa.sign(
            hash,
            pd.PSS(
                mgf=pd.MGF1(hashes.SHA256()),
                salt_length=pd.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        ivencrip = self.encriptariv(restaurante)
        if restaurante.descifrarPedido(ct, signature, ivencrip, self.key_public, self.cert):  # el restaurante descifrara el pedido con la key descifrada
            return ct, self.cipherkey, ivencrip
        return False

    def encriptarKEY(self, restaurante, key):  # funcion encargada de encriptar la key simetrica con la pk del restaurante al que se le realizo el pedido
        pk_restaurante = restaurante.public_key
        message = key
        self.cipherkey = pk_restaurante.encrypt(
            message,
            pd.OAEP(
                mgf=pd.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))
        restaurante.descifrarKEY(self.cipherkey)  # el restaurante descifrara la key con su clave privada

    def leerkey(self):
        # Lee la clave privada desde un archivo PEM
        path = JSON_FILES_PATH + "/../almacen/" + self.nombre + "/key.pem"
        with open(path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
            )
        return private_key

    def generarName(self):
        return x509.Name([
            x509.NameAttribute(NameOID.COMMON_NAME, self.nombre),
        ])
    def requestCA(self):
        # Generate a CSR
        csr = x509.CertificateSigningRequestBuilder().subject_name(self.name).sign(self._key_rsa, hashes.SHA256())
        Autoridad = CAUsuarios()
        certificado = Autoridad.crearCA(csr, self.key_public , self.name)

        path = JSON_FILES_PATH + "/../almacen/" + self.nombre + "/cert.pem"
        with open(path, "wb") as f:
            f.write(certificado.public_bytes(serialization.Encoding.PEM))
        return certificado
    def recargarCA(self):
        path = JSON_FILES_PATH + "/../almacen/" + self.nombre + "/cert.pem"
        os.remove(path)
        self.cert = self.requestCA()
    def validarCertificados(self, caR, caRes, restaurante):
        # Se verifica la cadena de certificados
        try:
            caRes.public_key().verify(
                restaurante.signature,
                restaurante.tbs_certificate_bytes,
                pd.PKCS1v15(),
                hashes.SHA256(),
            )
            caR.public_key().verify(
                caRes.signature,
                caRes.tbs_certificate_bytes,
                pd.PKCS1v15(),
                hashes.SHA256(),
            )
            return True
        except Exception:
            return False

