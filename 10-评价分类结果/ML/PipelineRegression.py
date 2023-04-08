from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

class PolyRegression:


    def __init__(self, degree):

        self.degree_ = degree

    def PolynomialRegression(self, degree):
        return Pipeline([
            ("poly", PolynomialFeatures(degree=self.degree)),
            ("std_scaler", StandardScaler()),
            ("lin_reg", LinearRegression())
        ])
