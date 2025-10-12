import numpy as np
import src.answers as A

def test_numpy_array_and_mean():
    assert isinstance(A.arr, np.ndarray), "Créez un array NumPy nommé `arr`."
    assert A.arr.shape == (3,), "L'array `arr` doit contenir exactement 3 éléments."
    assert np.all(A.arr == np.array([1, 2, 3])), "`arr` doit valoir [1, 2, 3]."
    assert np.isscalar(A.arr_mean), "`arr_mean` doit être un scalaire."
    assert A.arr_mean == np.mean(A.arr)

def test_normalize():
    x = np.array([0.0, 5.0, 10.0])
    y = A.normalize(x)
    assert isinstance(y, np.ndarray) and y.shape == x.shape
    assert np.allclose(y, np.array([0.0, 0.5, 1.0]))

    # cas plat
    z = np.array([3.14, 3.14, 3.14])
    yz = A.normalize(z)
    assert np.allclose(yz, np.zeros_like(z))
