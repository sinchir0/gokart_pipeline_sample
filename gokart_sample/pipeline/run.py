import gokart

from gokart_sample.pipeline.gokart_util import GetDataTask
from gokart_sample.pipeline.load_data import LoadDataTask
from gokart_sample.pipeline.split_data import SplitDataTask
from gokart_sample.pipeline.train import TrainTask
from gokart_sample.utils.template import GokartTask


class RunTask(GokartTask):
    def requires(self):
        data_task = LoadDataTask()
        data_task = SplitDataTask(data_task=data_task)
        train_task = GetDataTask(data_task=data_task, name="train")
        valid_task = GetDataTask(data_task=data_task, name="valid")
        test_task = GetDataTask(data_task=data_task, name="test")

        model_task = TrainTask()
        # pred_task = PredictionTask()

        # s3_task = UploadS3Task()

        return model_task

    def run(self):
        self.dump(self.__class__.__name__)
