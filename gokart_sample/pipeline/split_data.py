import gokart
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

from gokart_sample.utils.template import GokartTask


class SplitDataTask(GokartTask):
    data_task = gokart.TaskInstanceParameter()

    def requires(self) -> None:
        return self.data_task

    def run(self) -> None:
        data = self.load()
        X, y = data.data, data.target

        # trainとtestに分割
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # trainとvalidに分割
        X_train, X_valid, y_train, y_valid = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

        train = {"X_train": X_train, "y_train": y_train}
        valid = {"X_valid": X_valid, "y_valid": y_valid}
        test = {"X_test": X_test, "y_test": y_test}

        data = {"train": train, "valid": valid, "test": test}

        self.dump(data)
