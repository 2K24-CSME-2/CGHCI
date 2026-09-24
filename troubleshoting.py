import numpy as np

def threshold_image(image: np.ndarray, threshold: int) -> np.ndarray:
    result = np.where(image >= threshold, 255, 0)
    return result.astype(np.uint8)


problem_1_input = np.array(
    [[20, 128, 200],
     [100, 150, 250]],
    dtype=np.uint8
)

result = threshold_image(problem_1_input, 128)

print("Threshold Result:")
print(result)

expected = np.array(
    [[0, 255, 255],
     [0, 255, 255]],
    dtype=np.uint8
)

np.testing.assert_array_equal(result, expected)

print("Problem 1 passed!")