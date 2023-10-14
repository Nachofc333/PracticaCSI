
from cryptography.hazmat.primitives.asymmetric import rsa
from restaurantes.restauranteMaster import RestauranteMaster
class Restaurante2(RestauranteMaster):
    def __init__(self):
        super(RestauranteMaster, self).__init__()
        self._private_key =rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            )
        self.public_key = self._private_key.public_key()