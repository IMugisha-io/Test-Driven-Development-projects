#If earnings < 12000 per year, pay no tax
#then with earnings between 12,000 and 36,000 pay 20% tax
#then with earnings greater than 36000 per year, pay 40% tax
#Use a test first approach.  Commit at least after every passing test.

from taxCalculator import taxcalculator

def test_taxcalculator_0():
    assert taxcalculator(0)==0

def test_taxcalculator_10000():
    assert taxcalculator(10000)==0    

def test_taxcalculator_12000():
    assert taxcalculator(12000)== 12000 *0.2   

def test_taxcalculator_30000():
    assert taxcalculator(30000)==30000 * 0.2 