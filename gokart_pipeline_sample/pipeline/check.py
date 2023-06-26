import gokart
import luigi
from sklearn.metrics import accuracy_score

from gokart_pipeline_sample.utils.template import GokartTask


class CheckAccuracyTask(GokartTask):
    pred_task = gokart.TaskInstanceParameter()
    test_task = gokart.TaskInstanceParameter()
    require_acc = luigi.FloatParameter()

    def requires(self) -> dict[str, gokart.TaskInstanceParameter]:
        return {"pred": self.pred_task, "test": self.test_task}

    def run(self) -> None:
        pred = self.load("pred")
        test = self.load("test")

        y_test = test["y_test"]

        acc = accuracy_score(y_test, pred["pred"])
        if acc <= self.require_acc:
            raise ValueError(f"必要な精度に達していません 必要精度:{self.require_acc} 実際の精度:{acc}")

        self.dump(pred)
