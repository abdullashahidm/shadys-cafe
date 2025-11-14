import builtins
import pytest
from unittest.mock import patch
import sys
from unittest.mock import MagicMock
sys.modules["sound"]=MagicMock()
import cafe

@pytest.mark.parametrize("usrinput, e_qty, e_name", #e_=expected
[("3 pizza",3,"pizza"),("biryani",1,"biryani"),("29 ice cream",0,"ice cream")],)
def test_gq(usrinput,e_qty,e_name,capsys):
    with patch("time.sleep"):
        qty,name=cafe.gq(usrinput)
    assert qty==e_qty
    assert name==e_name
    if e_qty==0:
        captured=capsys.readouterr().out
        assert "won't be possible" in captured
        
def test_summ(capsys): #test valid/invalid items
    order=["2 pizza","biryani","hot chocolate"]
    result,price=cafe.summ(order)
    captured=capsys.readouterr().out
    assert any("removed" in captured for _ in captured)
    assert "Hot chocolate" in captured
    assert "Pizza" in result[0]
    assert price==pytest.approx(11*2+3.5,0.01)
    
def test_order(monkeypatch):
    inputs=iter(["pizza","no"])
    monkeypatch.setattr("builtins.input",lambda *args:next(inputs))
    with patch("random.choice",lambda x:x[0]):
        final,price=cafe.order()
    assert final==["1 Pizza"]
    assert price==11
    
def test_slip(capsys):
    items=["1 Pizza","2 Ice cream"] 
    price=17.0
    cafe.slip(items,price)
    output=capsys.readouterr().out
    assert "ITEM BILL" in output
    assert "Pizza" in output
    assert "TOTAL: $17.0" in output
    
def test_main(monkeypatch):
    inputs=iter(["","pizza","no","","",""])
    monkeypatch.setattr("builtins.input",lambda *args:next(inputs))
    with patch("cafe.sound.start_music"),patch("time.sleep"),patch("cafe.serve"),patch("cafe.summ",return_value=(["1 Pizza"],11)):
        cafe.main()
