"""MODULES"""
import json
from excepciones.excepcion import Excepcion


class JsonStoreMaster():
    """Class Store"""
    _FILE_PATH = ""
    _data_list = []
    _ID_FIELD = ""

    def __init__(self)->None:
        """Constructor"""
        self.load_store()

    def load_store(self)->None:
        """Cargar"""
        try:
            with open(self._FILE_PATH, "r", encoding="utf-8", newline="") as file:
                self._data_list = json.load(file)
        except FileNotFoundError:
            self._data_list = []
        except json.JSONDecodeError as ex:
            raise Excepcion("JSON Decode Error - Wrong JSON Format") from ex

    def save_store(self)->None:
        """Guardar"""
        try:
            with open(self._FILE_PATH, "w", encoding="utf-8", newline="") as file:
                json.dump(self._data_list, file, indent=2)
        except FileNotFoundError as ex:
            raise Excepcion("Wrong file or file path") from ex

    def find_data(self, data_to_find:str)->None:
        """Buscar fecha"""
        item_found = None
        for item in self._data_list:
            if item[self._ID_FIELD] == data_to_find:
                item_found = item
        return item_found

    def add_item(self, item:any)->None:
        """Añadir producto"""
        self.load_store()
        if isinstance(item, str):
            itemdict = json.loads(item)
            self._data_list.append(itemdict)
        else:
            self._data_list.append(item.__dict__())
        self.save_store()

    def data(self):
        self.load_store()
        return self._data_list
