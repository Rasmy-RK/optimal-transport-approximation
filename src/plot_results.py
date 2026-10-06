import csv
import matplotlib.pyplot as plt

sizes = []
times = []

with open("results/tables/baseline_results.csv", "r") as file:

    reader = csv.DictReader(file)

    for row in reader:
        sizes.append(int(row["Data Size"]))
        times.append(float(row["Average Time"]))

plt.plot(sizes, times, marker="o")

plt.xlabel("Data Size")
plt.ylabel("Average Time (seconds)")
plt.title("Wasserstein Distance Computation Time")

plt.grid(True)

plt.savefig("results/figures/runtime_vs_size.png")

plt.show()