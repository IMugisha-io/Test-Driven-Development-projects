from app.multiply import multiply

def test_multiply (x,y):
    assert multiply(1,1) == 1 , 'Test failed: multiply(1,1) shoud be 1'
    