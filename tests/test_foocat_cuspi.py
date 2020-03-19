from foocat_cuspi import foocat_cuspi
import pandas as pd

#{pyt{python foocat-test, eval = FALSE}m foocat import foocat import pandas as pd

def test_catbind():
    a = pd.Categorical(["character", "hits", "your", "eyeballs"])
    b = pd.Categorical(["but", "integer", "where it", "counts"])
    assert((foocat_cuspi.catbind(a, b)).codes == [1, 4, 7, 3, 0, 5, 6, 2]).all()
    assert((foocat_cuspi.catbind(a, b)).categories == ["but", "character", "counts", "eyeballs", "hits", "integer", "where it", "your"]).all()