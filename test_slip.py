import builtins
import pytest
from unittest.mock import patch
import sys
from unittest.mock import MagicMock
sys.modules["sound"]=MagicMock()
import project
   
def test_slip(capsys):
    items=["1 Pizza","2 Ice cream"] 
    price=17.0
    project.slip(items,price)
    output=capsys.readouterr().out
    assert "ITEM BILL" in output
    assert "Pizza" in output
    assert "TOTAL: $17.0" in output
