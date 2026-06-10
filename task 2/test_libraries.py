import numpy
import pandas
import matplotlib
import seaborn


def test_library_installations():
    assert numpy.__version__
    assert pandas.__version__
    assert matplotlib.__version__
    assert seaborn.__version__
