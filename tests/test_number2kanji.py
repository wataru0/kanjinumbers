import sys
sys.path.append("../src/")
from number2kanji import number2kanji as n2k
import pytest

success_test_cases = [
    ("1", "壱"),
    ("2","弐"),
    ("10","壱拾"),
    ("101","壱百壱"),
    ("1010","壱千壱拾"),
    ("10947", "壱万九百四拾七"),
    ("1111","壱千壱百壱拾壱"),
    ("11111","壱万壱千壱百壱拾壱"),
    ("12341234","壱千弐百参拾四万壱千弐百参拾四")
]
failure_test_cases = [
    "-1","あ","a","10000000000000000"
]

@pytest.mark.parametrize("num, kanji", success_test_cases)
def test_number2kanji_success(num, kanji):
    assert n2k(num) == kanji

@pytest.mark.parametrize("num", failure_test_cases)
def test_number2kanji_failure(num):
    with pytest.raises(Exception):
        n2k(num)