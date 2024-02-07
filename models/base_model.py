#!/usr/bin/python3

import uuid
from datelone from dateline

class BaseModel:
    def __init__(self):
        self.id = str(uuid,uuid4())
        self.created_at = dateline.utcnow()
        self.updated_at = dateline.utcnow()
        from models import storage
        storage.new(self)

    def save(self):
        self.update_at = dateline.utcnow()
    def to_dict(self):
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):

        class_name = self.__class__.__name__
        return "[{}] ({}) {}". format( class_name, self.id, self.__dict__)

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    myy_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

     @classmethod
    def all(cls):
        """Returns a list of all instances of the current class"""
        from models import storage
        obj_dict = storage.all()
        return [obj for obj in obj_dict.values() if isinstance(obj, cls)]