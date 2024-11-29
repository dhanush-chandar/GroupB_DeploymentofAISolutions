# test_integration.py

from forecasting_model import forecast  # Example import
from optimization_model import linprog

def test_integration():
    # Example demand forecast
    forecasted_demand = forecast(input_data)
    
    # Use forecasted demand as input to the optimization model
    result = linprog(c=[5, 4, 6], A_ub=[[1, 1, 1]], b_ub=[500], bounds=[(0, None)]*len(forecasted_demand), method='simplex')
    
    assert result.success
    assert result.x is not None
