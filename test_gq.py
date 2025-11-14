import builtins
import pytest
from unittest.mock import patch
import sys
from unittest.mock import MagicMock
sys.modules["sound"]=MagicMock()
import project

@pytest.mark.parametrize("usrinput, e_qty, e_name", #e_=expected
[("3 pizza",3,"pizza"),("biryani",1,"biryani"),("29 ice cream",0,"ice cream")],)
def test_gq(usrinput,e_qty,e_name,capsys):
    with patch("time.sleep"):
        qty,name=project.gq(usrinput)
    assert qty==e_qty
    assert name==e_name
    if e_qty==0:
        captured=capsys.readouterr().out
        assert "won't be possible" in captured
