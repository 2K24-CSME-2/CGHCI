import numpy as np

def mean_filter_3x3(neighborhood: np.ndarray) -> int:
    average = np.sum(neighborhood) / 9
    return int(round(average))


problem_3_input = np.array(
    [[10, 20, 10],
     [30, 50, 30],
     [10, 20, 10]],
    dtype=np.uint8
)

result = mean_filter_3x3(problem_3_input)

print("Mean Filter Result:", result)

assert result == 21

print("Problem 3 passed!")