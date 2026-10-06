import numpy as np
import time
import csv

np.random.seed(42)

sizes = [100, 500, 1000, 5000, 10000]
trials = 10

results = []

for size in sizes:

    times = []
    distances = []

    for trial in range(trials):

        data_a = np.random.normal(0, 1, size)
        data_b = np.random.normal(2, 1, size)

        start = time.perf_counter()

        data_a = np.sort(data_a)
        data_b = np.sort(data_b)

        distance = np.mean(np.abs(data_a - data_b))

        end = time.perf_counter()

        times.append(end - start)
        distances.append(distance)

    avg_time = np.mean(times)
    avg_distance = np.mean(distances)
    std_time = np.std(times)

    results.append([
        size,
        avg_distance,
        avg_time,
        std_time
    ])

    print("Data size:", size)
    print("Average Wasserstein distance:", avg_distance)
    print("Average time:", avg_time, "seconds")
    print("Time standard deviation:", std_time)
    print()

with open("results/tables/baseline_results.csv", "w", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Data Size",
        "Average Wasserstein Distance",
        "Average Time",
        "Time Standard Deviation"
    ])

    writer.writerows(results)

print("Results saved to results/tables/baseline_results.csv")