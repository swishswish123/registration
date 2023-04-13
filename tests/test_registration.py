from registration import perform_registration
import copy
from generate_pc_data import generate_shape
import pytest
import numpy as np


def test_ICP_registration():

    x_translation = 10
    y_translation = 10
    z_translation = 10
    source = generate_shape(shape='')
    target = copy.deepcopy(source).translate((x_translation, y_translation, z_translation))

    T = perform_registration(source, target)

    assert np.isclose(T[0,3] , x_translation)
    assert np.isclose(T[1, 3] , y_translation)
    assert np.isclose(T[2, 3] , z_translation)
