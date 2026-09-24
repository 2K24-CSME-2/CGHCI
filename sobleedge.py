import numpy as np

def sobel_response(block: np.ndarray) -> tuple[float, float, float]:

    Gx = np.array([
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ])

    Gy = np.array([
        [-1, -2, -1],
        [0, 0, 0],
        [1, 2, 1]
    ])

    gx = np.sum(block * Gx)
    gy = np.sum(block * Gy)

    strength = np.sqrt(gx * gx + gy * gy)

    return float(gx), float(gy), float(strength)


problem_5_input = np.array(
    [[20, 20, 200],
     [20, 20, 200],
     [20, 20, 200]],
    dtype=np.float32
)

gx, gy, strength = sobel_response(problem_5_input)

print("Gx:", gx)
print("Gy:", gy)
print("Edge Strength:", strength)

assert gx == 720.0
assert gy == 0.0

print("Problem 5 passed!")