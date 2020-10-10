import sys
sys.path.append("../src/")
from kanji2number import kanji2number as k2n
import pytest

success_test_cases = [
    ("壱",1),
    ("弐",2),
    ("壱拾",10),
    ("壱百壱",101),
    ("壱千壱拾",1010),
    ("壱万九百四拾七",10947),
    ("壱千壱百壱拾壱",1111),
    ("壱万壱千壱百壱拾壱",11111),
    ("壱千弐百参拾四万壱千弐百参拾四",12341234)
]
failure_test_cases = [
    "-1","あ","a","一","一万一千一百"
]

@pytest.mark.parametrize("kanji, num", success_test_cases)
def test_number2kanji_success(kanji, num):
    assert k2n(kanji) == num

@pytest.mark.parametrize("kanji", failure_test_cases)
def test_number2kanji_failure(kanji):
    with pytest.raises(Exception):
        k2n(kanji)