import numpy as np

np.set_printoptions(legacy='1.13')  # This ensures the output format meets HackerRank's requirements.

# Read the values of N and M from input
N, M = map(int, input().split())

# Create the N x M identity matrix
identity_matrix = np.eye(N, M, k=0)

# Print the N x M identity matrix
print(identity_matrix)
