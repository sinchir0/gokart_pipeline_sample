from gokart_pipeline_sample.pipeline.load_data import LoadDataTask
from gokart_pipeline_sample.pipeline.preprocess import PreprocessTask
from gokart_pipeline_sample.pipeline.split_data import SplitDataTask
from gokart_pipeline_sample.utils.template import GokartTask


class PrepareDataTask(GokartTask):
    def requires(self):
        data_task = LoadDataTask()
        data_task = PreprocessTask(data_task=data_task)
        data_task = SplitDataTask(data_task=data_task)
        return data_task
    
    def run(self) -> None:
        data = self.load()
        self.dump(data)