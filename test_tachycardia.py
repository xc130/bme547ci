from tachycardia import is_tachycardic
import pytest


@pytest.mark.parametrize("inputs, exp",
                         [('tachycardic', True), ('  tachycardic', True),
                          ('tachycardic', True), ('tachycardic.', True),
                          ('tachycardi', False), ('TachyCardic', True),
                          ('TACHYCARDIC', True), (6, False)])
def test_is_tachycardic(inputs, exp):
    ans = is_tachycardic(inputs)
    assert ans == exp
