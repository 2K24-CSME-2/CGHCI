import numpy as np

def contrast_stretch(
    image: np.ndarray,
    in_min: float,
    in_max: float,
    out_min: float = 0.0,
    out_max: float = 255.0
) -> np.ndarray:

    result = (
        (image - in_min)
        / (in_max - in_min)
        * (out_max - out_min)
        + out_min
    )

    result = np.clip(result, out_min, out_max)

    return result.astype(np.float32)


problem_4_input = np.array(
    [50, 100, 150],
    dtype=np.float32
)

result = contrast_stretch(
    problem_4_input,
    50,
    150
)

print("Contrast Result:")
print(result)

expected = np.array(
    [0.0, 127.5, 255.0],
    dtype=np.float32
)

np.testing.assert_allclose(result, expected)

print("Problem 4 passed!")