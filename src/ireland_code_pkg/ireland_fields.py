from django.db import models
from django.core.exceptions import ValidationError
import re

# List of Irish counties
IRISH_COUNTIES = [
    ('CW', 'Carlow'), ('CN', 'Cavan'), ('CE', 'Clare'), ('CO', 'Cork'),
    ('DL', 'Donegal'), ('D', 'Dublin'), ('G', 'Galway'), ('KY', 'Kerry'),
    ('KE', 'Kildare'), ('KK', 'Kilkenny'), ('LS', 'Laois'), ('LM', 'Leitrim'),
    ('LK', 'Limerick'), ('LD', 'Longford'), ('LH', 'Louth'), ('MO', 'Mayo'),
    ('MH', 'Meath'), ('MN', 'Monaghan'), ('OY', 'Offaly'), ('RN', 'Roscommon'),
    ('SO', 'Sligo'), ('TA', 'Tipperary'), ('WD', 'Waterford'),
    ('WH', 'Westmeath'), ('WX', 'Wexford'), ('WW', 'Wicklow')
]

# Regex pattern for validating Eircode
EIRCODE_REGEX = r"^[A-Za-z0-9]{3}[A-Za-z0-9 ]{4}$"

EIRCODE_REGEX = r"^[A-Za-z0-9]{3}[A-Za-z0-9 ]{4}$"

def validate_eircode(value):
    """Validate Irish Eircodes."""
    eircode_regex = re.compile(r'^[A-Z]{1}[0-9]{2} ?[0-9A-Z]{4}$')
    if not eircode_regex.match(value):
        raise ValidationError(f'{value} is not a valid Irish Eircode.')

class IrishCountyField(models.CharField):
    """Custom model field for Irish counties."""
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 2
        kwargs['choices'] = IRISH_COUNTIES
        super().__init__(*args, **kwargs)

class IrishEircodeField(models.CharField):
    """Custom model field for Irish Eircodes."""
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        kwargs['validators'] = [validate_eircode]
        super().__init__(*args, **kwargs)
