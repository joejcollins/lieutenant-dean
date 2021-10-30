from schematics.models import Model
from schematics.types import StringType, IntType
from schematics.transforms import wholelist


class Clothing(Model):

    class Options:
        serialize_when_none = True
        roles = {
            'remove_deprecated': wholelist()
        }

    colour = StringType(required=True)


class Trousers(Clothing):
    waist = IntType(required=True)
    style = StringType(required=True)
    inside_leg = IntType()


    @classmethod
    def _claim_polymorphic(cls, data):
        return data.get('waist')


class Hat(Clothing):
    size = IntType(required=True)

    @classmethod
    def _claim_polymorphic(cls, data):
        return data.get('size')