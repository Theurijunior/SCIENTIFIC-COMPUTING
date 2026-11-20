import numpy as np

# Real-world case: Monte Carlo estimation of monthly outage / SLA breach risk
# when daily demand and available capacity fluctuate randomly

rng = np.random.default_rng(seed=108)
n_trials = 50_000
days_per_month = 30

# Daily load (Mbps) ~ Normal(680, 75), daily link capacity (Mbps) ~ Normal(820, 55)
daily_load = rng.normal(loc=680.0, scale=75.0, size=(n_trials, days_per_month))
daily_cap = rng.normal(loc=820.0, scale=55.0, size=(n_trials, days_per_month))

overloaded_days = np.sum(daily_load > daily_cap, axis=1)
breach_prob = np.mean(overloaded_days >= 3)
avg_overload_days = np.mean(overloaded_days)

print(f"Simulated months: {n_trials}")
print(f"Average overload days per month: {avg_overload_days:.2f}")
print(f"Probability of 3 or more overload days in a month: {breach_prob:.4%}")
