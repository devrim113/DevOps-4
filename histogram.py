import numpy as np

import matplotlib.pyplot as plt

# Number of replicas
instances = [1, 2, 4, 8]

# Avg Req/Sec for each number of replicas
req_per_sec = [754.37, 860, 839.35, 813.60]

# Generate evenly spaced values for the x-axis
x = np.linspace(0, len(instances)-1, len(instances))

plt.figure(figsize=(10, 6))
plt.bar(x, req_per_sec, color='skyblue')
plt.xlabel('Number of Instances')
plt.ylabel('Req/Sec')
plt.title('Performance Scaling with Docker Swarm Replicas')
plt.xticks(x, instances)
plt.ylim(700, 900)
plt.grid(axis='y')

for i in range(len(instances)):
    plt.text(x[i], req_per_sec[i] + 10, str(req_per_sec[i]), ha='center')

plt.show()
