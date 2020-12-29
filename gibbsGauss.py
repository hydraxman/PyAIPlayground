import numpy as np
import matplotlib.pyplot as plt

N = 2000
# 初始化y, 可以任选一个值
y = 0
xs = []
ys = []

for i in xrange(N):
    # 更新x_t
    x = np.random.normal(0.8*y, 0.6)
    # 更新y_t
    y = np.random.normal(0.8*x, 0.6)
    xs.append(x)
    ys.append(y)

xs2, ys2 = np.random.multivariate_normal( [0, 0], [[1,0.8],[0.8,1]], N ).T

plt.subplot(211)    
plt.scatter(xs, ys)
plt.subplot(212)
plt.scatter(xs2, ys2)
plt.show()


    