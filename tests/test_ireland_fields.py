import sys
import os

# Add the src/ directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from ireland_code_pkg import IrishCountyField, IrishEircodeField
from django.core.exceptions import ValidationError
import unittest

class TestIrishFields(unittest.TestCase):
    def test_valid_counties(self):
        """Test valid Irish counties."""
        valid_counties = [code for code, name in [
            ('CW', 'Carlow'), ('D', 'Dublin'), ('KY', 'Kerry')]]
        for county in valid_counties:
            self.assertIn(county, [c[0] for c in IrishCountyField().choices])

    def test_invalid_eircode(self):
        """Test invalid Eircodes."""
        invalid_eircodes = ['1234', 'Invalid', 'ABC12']
        for eircode in invalid_eircodes:
            with self.assertRaises(ValidationError):
                IrishEircodeField().clean(eircode, None)

    def test_valid_eircode(self):
        """Test valid Eircodes."""
        valid_eircodes = ['D02 X285', 'T12 R5TP']
        for eircode in valid_eircodes:
            try:
                IrishEircodeField().clean(eircode, None)
            except ValidationError:
                self.fail(f"{eircode} raised ValidationError unexpectedly!")

if __name__ == "__main__":
    unittest.main()
