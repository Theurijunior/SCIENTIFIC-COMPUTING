import numpy as np
from scipy.optimize import minimize

# Real-world case: choosing order batch size q to minimize total annual inventory
# and holding/ordering cost: C(q) = (D / q) * S + (q / 2) * H

annual_demand = 12000.0
order_cost = 45.0
holding_cost = 2.4

def total_cost(q):
    batch = q[0]
    return (annual_demand / batch) * order_cost + 0.5 * batch * holding_cost

res = minimize(total_cost, x0=[100.0], bounds=[(1.0, None)], method="L-BFGS-B")
opt_q = res.x[0]

print(f"Optimal batch size: {opt_q:.2f} units")
print(f"Minimum annual cost: {res.fun:.2f}")
