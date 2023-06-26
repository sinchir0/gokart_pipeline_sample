import pandas as pd
from sklearn.datasets import load_iris

from gokart_pipeline_sample.utils.template import GokartTask


class LoadDataTask(GokartTask):
    def run(self) -> None:
        iris = load_iris()

        feature_name = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

        data = pd.DataFrame(iris.data, columns=feature_name)

        # idを追加
        data["id"] = data.index

        # ターゲット変数を追加
        data["target"] = iris.target

        return self.dump(data)
