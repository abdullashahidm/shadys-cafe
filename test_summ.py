import builtins
import pytest
from unittest.mock import patch
import sys
from unittest.mock import MagicMock
sys.modules["sound"]=MagicMock()
import project
        
def test_summ(capsys): #test valid/invalid items
    order=["2 pizza","biryani","hot chocolate"]
    result,price=project.summ(order)
    captured=capsys.readouterr().out
    assert any("removed" in captured for _ in captured)
    assert "Hot chocolate" in captured
    assert "Pizza" in result[0]
    assert price==pytest.approx(11*2+3.5,0.01)
