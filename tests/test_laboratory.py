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