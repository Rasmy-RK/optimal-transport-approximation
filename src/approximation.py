import numpy as np
import time
import csv
import matplotlib.pyplot as plt

np.random.seed(42)

# Experiment settings
dimensions = [2, 5, 10, 20, 50]
sample_size = 5000
trials = 10

# Number of projections
reference_projections = 500
approx_projections = 50

results = []


def sliced_wasserstein(data_a, data_b, num_projections):
    """
    Approximate Wasserstein distance in multiple dimensions
    using random 1D projections.
    """

    dimension = data_a.shape[1]

    total_distance = 0

    for _ in range(num_projections):

        # Generate random direction
        direction = np.random.normal(0, 1, dimension)

        # Normalize direction
        direction = direction / np.linalg.norm(direction)

        # Project data onto the direction
        projection_a = data_a @ direction
        projection_b = data_b @ direction

        # Sort projected values
        projection_a = np.sort(projection_a)
        projection_b = np.sort(projection_b)

        # 1D Wasserstein distance
        distance = np.mean(np.abs(projection_a - projection_b))

        total_distance += distance

    return total_distance / num_projections


for dimension in dimensions:

    errors = []
    runtimes = []

    for trial in range(trials):

        # Generate two distributions
        data_a = np.random.normal(
            0, 1, (sample_size, dimension)
        )

        data_b = np.random.normal(
            2, 1, (sample_size, dimension)
        )

        # Reference distance
        reference_distance = sliced_wasserstein(
            data_a,
            data_b,
            reference_projections
        )

        # Approximate distance
        start = time.perf_counter()

        approximate_distance = sliced_wasserstein(
            data_a,
            data_b,
            approx_projections
        )

        end = time.perf_counter()

        runtime = end - start

        error = abs(
            reference_distance - approximate_distance
        )

        errors.append(error)
        runtimes.append(runtime)

    average_error = np.mean(errors)
    error_std = np.std(errors)
    average_runtime = np.mean(runtimes)

    results.append([
        dimension,
        average_error,
        error_std,
        average_runtime
    ])

    print("Dimension:", dimension)
    print("Average error:", average_error)
    print("Error standard deviation:", error_std)
    print("Average time:", average_runtime, "seconds")
    print()


# Save results
with open(
    "results/tables/dimensionality_results.csv",
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Dimension",
        "Average Error",
        "Error Standard Deviation",
        "Average Time"
    ])

    writer.writerows(results)


# Extract values for plots
dims = [row[0] for row in results]
errors = [row[1] for row in results]
runtimes = [row[3] for row in results]


# Error graph
plt.figure()

plt.plot(
    dims,
    errors,
    marker="o"
)

plt.xlabel("Data Dimension")
plt.ylabel("Average Approximation Error")
plt.title("Approximation Error vs Data Dimension")

plt.grid(True)

plt.savefig(
    "results/figures/error_vs_dimension.png"
)

plt.show()


# Runtime graph
plt.figure()

plt.plot(
    dims,
    runtimes,
    marker="o"
)

plt.xlabel("Data Dimension")
plt.ylabel("Average Runtime (seconds)")
plt.title("Runtime vs Data Dimension")

plt.grid(True)

plt.savefig(
    "results/figures/runtime_vs_dimension.png"
)

plt.show()


print(
    "Results saved to "
    "results/tables/dimensionality_results.csv"
)