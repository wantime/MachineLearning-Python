# MachineLearning-Python

### [02 资料](02-Machine-Learning-Basics)


pattern recognition and ML

Introduction to Machine Learning with Python

Zero-to-AI

### [03 Jupyter Notebook Basics](03-Jupyter-Notebook-Basics)

%run、%time等命令，快捷键的使用

### [04 kNN](04-kNN/)

python实现kNN算法与相关处理

### [05 线性回归模型](05-regression/)
python实现线性回归，MAE RMSE R-Square
线性回归模型的可解释性

### [06 梯度下降法](06-梯度下降法)

基于搜索的最优化方法

**梯度下降法：**对某个cost function，需要找到数值最小的位置，利用求导（微分）获取数值减小的方向并移动，不断重复上述过程，就可获得最优解

​	线性回归问题：正规方程解

​	局部最优解问题：多次计算，设定不同的初始值

​	梯度过大：可以对梯度进行归一化，仅获取方向

​	向量化：减少计算时间

**随机梯度下降：**当m很大时，每次计算所有样本的梯度会耗费大量时间，因此每次只随机选择一个样本，学习率需要先大后小，可以模拟退火思想，学习率= a/(i_iters + b)，引入两个超参数

**小批量随机梯度下降法**可以综合上述两种方法的优点
