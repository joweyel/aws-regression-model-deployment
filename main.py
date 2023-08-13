import numpy as np
import matplotlib.pyplot as plt
from util import get_data, func
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

def main():
    # Parameters
    m = 0.42
    b = 0.2
    std = 0.4
    X_train, y_train, X_test, y_test = get_data(train_split=0.7, m=m, 
                                                b=b, std=std)

    # Defining, training and evaluate LR-model
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    metrics = dict()
    metrics["mse"] = mean_squared_error(y_test, y_pred)
    metrics["rmse"] = np.sqrt(metrics["mse"])
    metrics["mae"] = mean_absolute_error(y_test, y_pred)

    print("Metrics: ", metrics)
    title = " | ".join([f"{k.upper()}: {metrics[k]:.4f}" for k, v in metrics.items()])


    # Print Predictions
    X = np.linspace(-2.3, 2.3, 200)[:, None]
    y = model.predict(X)
    y_true = func(X, m, b)

    plt.plot(X, y, color="black", label=r"$y_{pred}$")
    plt.plot(X, y_true, color="darkgreen", label=r"$y_{true}$")
    plt.scatter(X_train, y_train, color="blue", marker="X", label=r"$y_{train}$")
    plt.scatter(X_test, y_test, color="red", label=r"$y_{test}$")
    plt.legend(loc="upper left")
    plt.title(title)
    plt.grid(True)
    plt.savefig("plot.png", dpi=200)
    plt.show()

if __name__ == '__main__':
    main()