import numpy as np
from scipy.interpolate import CubicSpline

# Real-world case: interpolating elevation along a trail/route from GPS checkpoints
# distance_km: cumulative distance along route
# elevation_m: recorded altitude in meters at each checkpoint

distance_km = np.array([0.0, 1.5, 3.2, 5.0, 7.4, 10.0])
elevation_m = np.array([1450.0, 1520.0, 1610.0, 1585.0, 1740.0, 1810.0])

route_profile = CubicSpline(distance_km, elevation_m, bc_type="natural")
sample_km = np.array([0.75, 2.35, 4.10, 6.20, 8.70])
sample_elev = route_profile(sample_km)

for d, e in zip(sample_km, sample_elev):
    print(f"At {d:.2f} km -> estimated elevation: {e:.2f} m")
