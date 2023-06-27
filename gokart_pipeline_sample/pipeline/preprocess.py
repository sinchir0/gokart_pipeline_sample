import gokart
import pandas as pd
import pandera as pa
from pandera.typing import DataFrame

from gokart_pipeline_sample.pipeline.schemas.schema import IrisFeatureSchema, PreprocessedSchema
from gokart_pipeline_sample.utils.template import GokartTask


class PreprocessTask(GokartTask):
    data_task = gokart.TaskInstanceParameter()

    def requires(self) -> gokart.TaskInstanceParameter:
        return self.data_task

    @staticmethod
    def make_area(length: pd.Series, width: pd.Series) -> pd.Series:
        return length * width

    @pa.check_types
    def add_area_feature(self, data: DataFrame[IrisFeatureSchema]) -> DataFrame[PreprocessedSchema]:
        # 花びらの面積を新たな特徴量として追加
        data["petal_area"] = self.make_area(data["petal_length"], data["petal_width"])

        return data

    def run(self) -> None:
        data = self.load_data_frame()
        df = self.add_area_feature(data=data)
        self.dump(df)
