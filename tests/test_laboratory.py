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

    def test_add_product_to_stock(self):
        reactions = {"Aspirin": [("Acid", 1.0)]}
        lab = Laboratory(["Acid"], reactions)
        lab.add("Aspirin", 10.0)
        assert lab.get_quantity("Aspirin") == 10.0

class TestLaboratoryReactions:
    def test_create_laboratory_with_empty_reactions(self):
        lab = Laboratory(["Water"], {})
        assert lab is not None
    
    def test_create_laboratory_with_valid_reactions(self):
        reactions = {
            "Aspirin": [("Salicylic Acid", 1.0), ("Acetic Anhydride", 1.2)]
        }
        lab = Laboratory(["Salicylic Acid", "Acetic Anhydride"], reactions)
        assert lab is not None

    def test_reaction_with_unknown_substance_raises_value_error(self):
        reactions = {
            "Product": [("Unknown", 1.0)]
        }
        with pytest.raises(ValueError):
            Laboratory(["Water"], reactions)

class TestLaboratoryMake:
    def test_make_product_returns_quantity(self):
        reactions = {"Product": [("A", 1.0), ("B", 2.0)]}
        lab = Laboratory(["A", "B"], reactions)
        lab.add("A", 10.0)
        lab.add("B", 20.0)
        result = lab.make("Product", 5.0)
        assert result == 5.0

    def test_make_consumes_substances(self):
        reactions = {"Product": [("A", 1.0), ("B", 2.0)]}
        lab = Laboratory(["A", "B"], reactions)
        lab.add("A", 10.0)
        lab.add("B", 20.0)
        lab.make("Product", 5.0)
        assert lab.get_quantity("A") == 5.0   # 10 - 5*1
        assert lab.get_quantity("B") == 10.0  # 20 - 5*2