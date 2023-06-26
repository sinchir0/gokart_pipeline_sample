from sklearn.datasets import load_iris

from gokart_sample.utils.template import GokartTask


class LoadDataTask(GokartTask):
    def run(self) -> None:
        data = load_iris()
        return self.dump(data)
