import numpy as np
from scipy.integrate import solve_ivp

# Real-world case: SIR epidemic spread model over a 30-day window
# S: susceptible fraction, I: infectious fraction, R: recovered fraction

beta = 0.35
gamma = 0.10

def sir_model(t, state):
    s, i, r = state
    ds = -beta * s * i
    di = beta * s * i - gamma * i
    dr = gamma * i
    return [ds, di, dr]

init_state = [0.99, 0.01, 0.0]
t_days = np.linspace(0.0, 30.0, 7)
sim = solve_ivp(sir_model, (0.0, 30.0), init_state, t_eval=t_days, method="RK45")

for day, s_val, i_val, r_val in zip(sim.t, sim.y[0], sim.y[1], sim.y[2]):
    print(f"Day {day:4.1f} | S={s_val:.4f} | I={i_val:.4f} | R={r_val:.4f}")
