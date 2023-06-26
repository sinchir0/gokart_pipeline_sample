import gokart
import numpy as np
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame

from gokart_pipeline_sample.pipeline.shcemas.schema import OutputSchema
from gokart_pipeline_sample.utils.template import GokartTask


class MakeOutputTask(GokartTask):
    pred_task = gokart.TaskInstanceParameter()
    test_task = gokart.TaskInstanceParameter()

    def requires(self) -> dict[str, gokart.TaskInstanceParameter]:
        return {"pred": self.pred_task, "test": self.test_task}

    @pa.check_types
    def make_output_data(self, id: pd.Series, pred: np.ndarray) -> DataFrame[OutputSchema]:
        return pd.DataFrame({"id": id, "pred": pred})

    def run(self) -> None:
        pred = self.load("pred")
        test = self.load("test")

        X_test = test["X_test"]

        output = self.make_output_data(id=X_test["id"], pred=pred)

        self.dump(output)
