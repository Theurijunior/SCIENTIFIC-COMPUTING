import numpy as np

# 12 two-hour average throughput readings in Mbps across a router link
throughput_mbps = np.array([
    45.0, 32.5, 28.0, 35.0, 60.0, 95.5,
    120.0, 145.2, 160.8, 130.4, 88.0, 54.0
])

avg_mbps = np.mean(throughput_mbps)
min_mbps = np.min(throughput_mbps)
max_mbps = np.max(throughput_mbps)

# Vectorized conversion from megabits per second (Mbps) to megabytes per second (MB/s)
throughput_mbs = throughput_mbps / 8.0

print(f"Average throughput: {avg_mbps:.2f} Mbps")
print(f"Lowest throughput: {min_mbps:.2f} Mbps")
print(f"Peak throughput: {max_mbps:.2f} Mbps")
print("First six readings in MB/s:", np.round(throughput_mbs[:6], 2))

