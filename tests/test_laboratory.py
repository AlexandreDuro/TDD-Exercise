import pytest
from src.laboratory import Laboratory


class TestLaboratoryInitialization:
    def test_create_laboratory_with_empty_list(self):
        """Should create a laboratory with an empty list of substances."""
        lab = Laboratory([])
        assert lab is not None   

    def test_create_laboratory_with_valid_substances(self):
        lab = Laboratory(["Water", "Ethanol"]
        assert lab is not None
