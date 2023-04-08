import numpy as np
from .metrics import accuracy_score


class LogisticRegression:

    def __int__(self):
        """初始化Linear Regression模型"""
        self.coef_ = None
        self.intercept_ = None
        self._theta = None

    def _sigmoid(self, t):
        return 1. / (1. + np.exp(-t))
    def fit(self, X_train, y_train, eta=0.01, n_iters=1e4):
        """
        根据训练集X_train, y_train, 使用梯度下降法训练Logistic Regression模型
        eta: 学习率
        n_iters: 迭代次数
        """
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_trian"

        def J(theta, X_b, y):
            y_hat = self._sigmoid(X_b.dot(theta))
            try:
                return np.sum(y*np.log(y_hat) + (1-y)*np.log(1-y_hat)) / len(y)
            except:
                return float('inf')

        def dJ(theta, X_b, y):
            return X_b.T.dot(self._sigmoid(X_b.dot(theta)) - y) / len(X_b)

        def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):

            theta = initial_theta
            cur_iter = 0

            while cur_iter < n_iters:
                gradient = dJ(theta, X_b, y)
                last_theta = theta
                theta = theta - eta * gradient

                if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
                    break

                cur_iter += 1
            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(X_b,y_train,initial_theta,eta,n_iters)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def fit_sgd(self, X_train, y_train, n_iters=5, t0=5, t1=50):
        """根据训练集X_train, y_train, 使用梯度下降法训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_trian"
        assert n_iters >= 1, \
            "the n_iters must be large than 0"
        def dJ_sgd(theta, X_b_i, y_i):
            return X_b_i.T.dot(X_b_i.dot(theta) - y_i) * 2.

        def sgd(X_b, y, initial_theta, n_iters, t0=5, t1=50):

            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            m = len(X_b)

            for cur_iter in range(n_iters):
                indexes = np.random.permutation(m)
                X_b_new = X_b[indexes]
                y_new = y[indexes]
                for i in range(m):
                    gradient = dJ_sgd(theta, X_b_new[i], y_new[i])
                    theta = theta - learning_rate(cur_iter*m + i) * gradient

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = sgd(X_b,y_train,initial_theta,n_iters)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def fit_mbgd(self, X_train, y_train, k=10, n_iters=2, t0=5, t1=50):
        """根据训练集X_train, y_train, 使用梯度下降法训练Linear Regression模型"""
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_trian"
        assert n_iters >= 1, \
            "the input n_iters must be large than 0"
        assert k > 1, \
            "the input k must be large than 1"

        def dJ_mbgd(theta, X_b_k, y_k):
            return X_b_k.T.dot(X_b_k.dot(theta) - y_k) * 2. / len(y_k)

        def mbgd(X_b, y, initial_theta, k, n_iters, t0=5, t1=50):

            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            m = len(X_b)

            for cur_iter in range(n_iters):
                indexes = np.random.permutation(m)
                X_b_new = X_b[indexes]
                y_new = y[indexes]
                for i in range(m // k):
                    rand_k = np.arange(i * k, (i + 1) * k)
                    gradient = dJ_mbgd(theta, X_b_new[rand_k], y_new[rand_k])
                    theta = theta - learning_rate(cur_iter*(m // k) + i) * gradient

            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = mbgd(X_b, y_train, initial_theta, k, n_iters)
        self.intercept_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def predict_proba(self, X_predict):
        """
        给定待预测数据集X_predict, 返回表示X_predict的结果向量
        :param X_predict:待预测数据集
        :return:y_predict
        """
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return self._sigmoid(X_b.dot(self._theta))


    def predict(self, X_predict):
        """
        给定待预测数据集X_predict, 返回表示X_predict的结果向量
        :param X_predict:待预测数据集
        :return:y_predict
        """
        assert self.intercept_ is not None and self.coef_ is not None, \
            "must fit before predict!"
        assert X_predict.shape[1] == len(self.coef_), \
            "the feature number of X_predict must be equal to X_train"

        #X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])

        proba = self.predict_proba(X_predict)
        return np.array(proba >= 0.5, dtype='int')

    def score(self, X_test, y_test):
        """根据测试数据集 X_test 和 y_test 确定当前模型的准确度"""

        y_predict = self.predict(X_test)
        return accuracy_score(y_test, y_predict)

    def __repr__(self):
        return "LogisticRegression()"
