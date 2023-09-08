import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Set a random seed for reproducibility
np.random.seed(42)

# Generate 20 data points for x between 0 and 10
x = 10 * np.random.rand(20)

# Generate y values with a linear relationship and add some noise
y = 2 * x + 10 + np.random.randn(20) * 5

X = x.reshape(-1,1)

reg = LinearRegression().fit(X, y)
y_pred = reg.predict(X)

fig, ax = plt.subplots(1,1)
ax.scatter(x, y)
ax.plot(x, y_pred, color="orange")

sample_indexes = [15, 17, 18]
for i in sample_indexes:
    x1, y1 = x[i], y[i]
    x2, y2 = x[i], y_pred[i]
    ax.plot([x1, x2], [y1, y2], color="red", linestyle="--")
    ax.text(x[i], np.mean([y[i], y_pred[i]]), f" $|y_{{{i}}} - \hat y_{{{i}}}|$")
    # ax.text(x[i], y[i], f" $y_{{{i}}}$")
    # ax.text(x[i], y_pred[i], f" $\hat y_{{{i}}}$")

ax.text(6, 10, r"$MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat y_i|$")

ax.set_xlabel("X  $\\;\\rightarrow$")
ax.set_ylabel("y  $\\;\\rightarrow$")
# fig.savefig("../img/mae_error")
plt.show()
