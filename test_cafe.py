import cafe
import unittest
from unittest.mock import patch,MagicMock

class TestCafe(unittest.TestCase):
	@patch("cafe.summ")
	@patch("cafe.random.choice",rV="Ok") #return Value
	@patch("builtins.input",sideeffect=["","yes","croissant"])
    def test_order():
        ...

    def test_summ():
        ...
	
    def test_slip():
        ...
	
    def test_gq():
        ...
        
if __name__=="__main__":
    unittest.main()
