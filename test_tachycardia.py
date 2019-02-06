from tachycardia import is_tachycardic
import pytest


@pytest.mark.parametrize("input, exp",
                         [('tachycardic', True), ('  tachycardic', True),
                          ('tachycardic', True), ('tachycardic.', True),
                          ('tachycardi', False), ('TachyCardic', True),
                          ('TACHYCARDIC', True), (6, False)])
def test_is_tachycardic(input, exp):
    ans = is_tachycardic(input)
    assert ans == exp
