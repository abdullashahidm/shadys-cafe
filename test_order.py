import builtins
import pytest
from unittest.mock import patch
import sys
from unittest.mock import MagicMock
sys.modules["sound"]=MagicMock()
import project
        
def test_order(monkeypatch):
    inputs=iter(["pizza","no"])
    monkeypatch.setattr("builtins.input",lambda *args:next(inputs))
    with patch("random.choice",lambda x:x[0]):
        final,price=project.order()
    assert final==["1 Pizza"]
    assert price==11
