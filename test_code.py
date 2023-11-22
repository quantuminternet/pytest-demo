import pytest
import my_code

@pytest.mark.parametrize(['x', 'y', 'expected'], [(1, 1, 2), (1, 2, 3), (1, 1, 3)]) 
def test_add(x, y, expected):
  result = my_code.add(x, y)
  assert result == expected
  
