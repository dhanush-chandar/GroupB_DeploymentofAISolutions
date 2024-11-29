# test_performance.py

import pytest
from optimization_model import linprog

@pytest.mark.benchmark(group="optimization")
def test_performance(benchmark):
    result = benchmark(lambda: linprog(c=[5, 4, 6], A_ub=[[1, 1, 1]], b_ub=[500], bounds=[(0, None)]*3, method='simplex'))
    assert result.success
