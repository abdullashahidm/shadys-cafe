import builtins
import pytest
from unittest.mock import patch
import sys
from unittest.mock import MagicMock
sys.modules["sound"]=MagicMock()
import project
    
def test_main(monkeypatch):
    inputs=iter(["","pizza","no","","",""])
    monkeypatch.setattr("builtins.input",lambda *args:next(inputs))
    with patch("project.sound.start_music"),patch("time.sleep"),patch("project.serve"),patch("project.summ",return_value=(["1 Pizza"],11)):
        project.main()
