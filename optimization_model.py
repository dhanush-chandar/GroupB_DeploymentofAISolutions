# optimization_model.py

from scipy.optimize import linprog

# Example of predicted demand and costs
demand = [100, 200, 150]  # Predicted demand for 3 products
costs = [5, 4, 6]         # Cost for restocking 3 products

# Constraints (e.g., stock capacity, max order quantity)
A = [[1, 1, 1]]  # Sum of all quantities to restock
b = [500]         # Max capacity for restocking

# Solve the linear programming problem
result = linprog(c=costs, A_ub=A, b_ub=b, bounds=[(0, None)]*len(demand), method='simplex')

# Output the optimal restocking quantities
print(f"Optimal restocking quantities: {result.x}")
