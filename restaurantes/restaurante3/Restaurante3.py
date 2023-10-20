from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from restaurantes.restauranteMaster import RestauranteMaster
import os
JSON_FILES_PATH = os.path.dirname(__file__)
class Restaurante3(RestauranteMaster):
    _FILE_NAME = JSON_FILES_PATH + "/keyR3.pem"
    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =self.genererkey()
        self.public_key = self._private_key.public_key()
        self.iv = ""
        self._key = ""