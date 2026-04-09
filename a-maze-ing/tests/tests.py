import pytest


class TestCases:
    def test_assert(self):
        text = "hello"
        assert "H" in text, f"'H' must be in {text}"

    def raising_error(self, div: int):
        if div == 0:
            raise ValueError
        return 100 / div

    def test_f(self):
        with pytest.raises(ValueError):
            self.raising_error(10)

