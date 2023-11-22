import pytest
import code

@pytest.mark.parametrize(['x', 'y', 'expected'], [(1, 1, 2), (1, 2, 3), (1, 1, 3)]) 
def test_add(x, y, expected):
  result = code.add(x, y)
  assert result == expected
  
