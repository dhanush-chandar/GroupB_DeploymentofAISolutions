# test_optimization.py

import pytest
from optimization_model import linprog

def test_optimal_restocking():
    demand = [100, 200, 150]
    costs = [5, 4, 6]
    result = linprog(c=costs, A_ub=[[1, 1, 1]], b_ub=[500], bounds=[(0, None)]*len(demand), method='simplex')
    
    # Test if optimal restocking quantities are within expected range
    assert all(0 <= x <= 200 for x in result.x)
