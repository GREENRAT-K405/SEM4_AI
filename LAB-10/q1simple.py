import numpy as np
import csv

#load cities
cities = []
with open("cities.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        cities.append([float(row[0]), float(row[1])])

cities = np.array(cities)

K = 3   # number of airports


#assign cities to nearest airport
def assign_clusters(cities, centroids):
    labels = []
    for city in cities:
        distances = [np.sum((city-c)**2) for c in centroids]
        labels.append(np.argmin(distances))
    return np.array(labels)


#compute ssd per cluster
def cluster_ssd(cities, centroids, labels):

    total = 0

    for k in range(K):

        pts = cities[labels == k]
        ssd = 0

        for p in pts:
            ssd += np.sum((p-centroids[k])**2)

        print(f"Airport {k+1} SSD:", round(ssd,2))
        total += ssd

    print("Total SSD:", round(total,2))


#Gradient Descent Method
def gradient_descent(cities):

    centroids = cities[np.random.choice(len(cities), K, replace=False)]

    for _ in range(100):

        labels = assign_clusters(cities, centroids)

        for k in range(K):

            pts = cities[labels == k]

            if len(pts) > 0:
                grad = -2*np.mean(pts-centroids[k], axis=0)
                centroids[k] = centroids[k] - 0.1*grad

    return centroids, labels

# Newton-Raphson Method
def newton_method(cities):

    centroids = cities[np.random.choice(len(cities), K, replace=False)]

    for _ in range(20):

        labels = assign_clusters(cities, centroids)

        for k in range(K):

            pts = cities[labels == k]

            if len(pts) > 0:
                centroids[k] = np.mean(pts, axis=0)

    return centroids, labels


# Run Gradient Descent
print("\n--- Gradient Descent Method ---")

gd_centroids, gd_labels = gradient_descent(cities)

for i,c in enumerate(gd_centroids):
    print(f"Airport {i+1} location:", c)

print("\nCluster SSD (Gradient Descent)")
cluster_ssd(cities, gd_centroids, gd_labels)


# Run Newton-Raphson
print("\n--- Newton-Raphson Method ---")

nr_centroids, nr_labels = newton_method(cities)

for i,c in enumerate(nr_centroids):
    print(f"Airport {i+1} location:", c)

print("\nCluster SSD (Newton-Raphson)")
cluster_ssd(cities, nr_centroids, nr_labels)