import numpy as np
from math import sqrt


def accuracy_score(y_true, y_predict):
    """计算模型预测的准确率"""
    assert y_true.shape[0] == y_predict.shape[0], \
        "the size of y_true must be equal to the size of y_predict"
    return sum(y_true == y_predict) / len(y_true)


def mean_squared_error(y_true, y_predict):
    """计算y_true和y_predict之间的MSE"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum((y_true - y_predict) ** 2) / len(y_true)

def root_mean_squared_error(y_true, y_predict):
    """计算y_true和y_predict之间的RMSE"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return sqrt(np.sum((y_true - y_predict) ** 2) / len(y_true))


def mean_absolute_error(y_true, y_predict):
    """计算y_true和y_predict之间的MAE"""
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum(np.absolute(y_true - y_predict)) / len(y_true)

def r2_score(y_true, y_predict):
    """计算y_true和y_predict之间的R Square"""

    return 1 - mean_squared_error(y_true, y_predict) / np.var(y_true)

def dJ_debug(J, theta, X_b, y, epsilon=0.0001):
    res = np.empty(len(theta))
    for i in range(len(theta)):
        theta_1 = theta.copy()
        theta_1[i] += epsilon
        theta_2 = theta.copy()
        theta_2[i] -= epsilon
        res[i] = (J(theta_1, X_b, y) - J(theta_2, X_b, y)) / (2 * epsilon)
    return res