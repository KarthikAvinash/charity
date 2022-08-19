from import_export import resources
from .models import data

class PersonResource(resources.ModelResource):
    class meta:
        model=data