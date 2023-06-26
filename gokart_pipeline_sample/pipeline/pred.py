import gokart
import numpy as np

from gokart_pipeline_sample.utils.template import GokartTask


class PredTask(GokartTask):
    model_task = gokart.TaskInstanceParameter()
    test_task = gokart.TaskInstanceParameter()

    def requires(self) -> dict[str, gokart.TaskInstanceParameter]:
        return {"model": self.model_task, "test": self.test_task}

    def run(self) -> None:
        model = self.load("model")
        test = self.load("test")

        X_test = test["X_test"]

        y_pred = model.predict(X_test)

        y_pred_argmax = np.argmax(y_pred, axis=1)

        self.dump(y_pred_argmax)
