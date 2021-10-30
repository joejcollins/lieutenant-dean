from schematics.exceptions import ValidationError
from schematics.models import Model
from schematics.types import (
    StringType, IntType, BooleanType, DateTimeType, ListType, PolyModelType
    )
from schematics.types.serializable import serializable
from schematics.transforms import blacklist
from my_module.models.clothing import Trousers, Hat
import json
import os


class Person(Model):

    class Options:
        serialize_when_none = False
        _deprecated = blacklist('marital_status', 'gender')
        roles = {
            'remove_deprecated': _deprecated
        }

    def __init__(self, person_file_name, person_json):
        # Remember where the person came from
        self._person_file_name = person_file_name
        super().__init__(person_json)

    @staticmethod
    def find_by_file(person_file_name):
        """ Find a person based on their file name. """
        with open('./my_module/db/data/' + person_file_name) as json_file:
            person_json = json.load(json_file)
        person = Person(person_file_name, person_json)
        return person

    @staticmethod
    def all():
        """ Return all the people. """
        people = []
        for file in os.listdir('./my_module/db/data/'):
            if file.endswith(".json"):
                with open('./my_module/db/data/' + file) as json_file:
                    person_json = json.load(json_file)
                    person = Person(file, person_json)
                    people.append(person)
        return people

    name = StringType(required=True)
    age = IntType()
    clothing = ListType(PolyModelType([Hat, Trousers]))

    _male = BooleanType(serialized_name="male")
    _female = BooleanType(serialized_name="female")

    def get_male(self):
        return self._male

    def set_male(self, value):
        self._male = value
        self._female = not value

    male = property(get_male, set_male)

    def get_female(self):
        return self._female

    def set_female(self, value):
        self._female = value
        self._male = not value

    female = property(get_female, set_female)

    bald = BooleanType()
    bio = StringType(required=True)
    year_of_birth = DateTimeType(required=False)
    retired = BooleanType(required=False, default=False)

    def update(self, update_json):
        """ Add stuff using json. """
        for key in update_json:
            setattr(self, key, update_json[key])

    # Add an additional value
    @serializable
    def age_in_dog_years(self):
        """ Adding a field that is calculated from the original data. """
        return self.age * 7

    def validate_retired(self, data, value):
        if data['age'] > 65:
            raise ValidationError(u'Over 65 must be retired.')
        return value

    def save(self):
        stuff_to_save = self.to_primitive(role='remove_deprecated')
        with open('./my_module/db/data/' + self._person_file_name, 'w') as outfile:
            json.dump(stuff_to_save, outfile, indent=4, sort_keys=True)
