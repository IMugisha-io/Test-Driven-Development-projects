import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.multiply import multiply

def test_multiply():
    assert multiply (1,1)==1