import pytest
from src.laboratory import Laboratory


class TestLaboratoryInitialization:
    def test_create_laboratory_with_empty_list(self):
        """Should create a laboratory with an empty list of substances."""
        lab = Laboratory([])
        assert lab is not None   

    def test_create_laboratory_with_valid_substances(self):
        lab = Laboratory(["Water", "Ethanol"])
        assert lab is not None

    def test_get_quantity_returns_zero_for_known_substance(self):
        lab = Laboratory(["Water"])
        assert lab.get_quantity("Water") == 0.0

    def test_get_quantity_raises_for_unknown_substance(self):
        lab = Laboratory(["Water", "Ethanol"])
        with pytest.raises(ValueError, match="Unknown substance: Unknown"):
          lab.get_quantity("Unknown")

    def test_create_laboratory_with_none_raises_type_error(self):
        with pytest.raises(TypeError):
            Laboratory(None)

    def test_create_laboratory_with_non_string_element_raises_type_error(self):
        with pytest.raises(TypeError):
            Laboratory(["Water", 123])

    def test_create_laboratory_with_empty_string_raises_value_error(self):
        with pytest.raises(ValueError):
            Laboratory([""])

    def test_create_laboratory_with_whitespace_only_raises_value_error(self):  
        with pytest.raises(ValueError):
            Laboratory(["   "])

    def test_create_laboratory_with_duplicates_raises_value_error(self):
        with pytest.raises(ValueError):
            Laboratory(["Water", "Water"])

class TestLaboratoryAdd:

    def test_add_quantity_to_substance(self):
        lab = Laboratory(["Water"])
        lab.add("Water", 5.5)
        assert lab.get_quantity("Water") == 5.5

    def test_add_to_unknown_substance_raises_value_error(self):
        lab = Laboratory(["Water"])
        with pytest.raises(ValueError):
            lab.add("Unknown", 5.0)

    def test_add_negative_quantity_raises_value_error(self):
        lab = Laboratory(["Water"])
        with pytest.raises(ValueError):
            lab.add("Water", -5.0)

    def test_add_non_numeric_quantity_raises_type_error(self):
        lab = Laboratory(["Water"])
        with pytest.raises(TypeError):
          lab.add("Water", "five")