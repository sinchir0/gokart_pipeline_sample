from gokart_sample.pipeline.check import CheckAccuracyTask
from gokart_sample.pipeline.gokart_util import GetDataTask
from gokart_sample.pipeline.load_data import LoadDataTask
from gokart_sample.pipeline.make_output import MakeOutputTask
from gokart_sample.pipeline.pred import PredTask
from gokart_sample.pipeline.preprocess import PreprocessTask
from gokart_sample.pipeline.run_middle import PrepareDataTask
from gokart_sample.pipeline.split_data import SplitDataTask
from gokart_sample.pipeline.train import TrainTask
from gokart_sample.pipeline.upload import UploadS3Task
from gokart_sample.utils.template import GokartTask


class RunTask(GokartTask):
    def requires(self):
        data_task = LoadDataTask()
        data_task = PreprocessTask(data_task=data_task)
        data_task = SplitDataTask(data_task=data_task)

        train_data_task = GetDataTask(data_task=data_task, name="train")
        valid_data_task = GetDataTask(data_task=data_task, name="valid")
        test_data_task = GetDataTask(data_task=data_task, name="test")

        model_task = TrainTask(train_task=train_data_task, valid_task=valid_data_task)
        pred_task = PredTask(model_task=model_task, test_task=test_data_task)

        output_task = MakeOutputTask(pred_task=pred_task, test_task=test_data_task)

        checked_output_task = CheckAccuracyTask(
            pred_task=output_task,
            test_task=test_data_task,
            require_acc=0.9
        )

        s3_upload_task = UploadS3Task(output_task=checked_output_task)

        return s3_upload_task

    def run(self):
        self.dump(self.__class__.__name__)


class RunNestTask(GokartTask):
    def requires(self):
        data_task = PrepareDataTask()

        train_data_task = GetDataTask(data_task=data_task, name="train")
        valid_data_task = GetDataTask(data_task=data_task, name="valid")
        test_data_task = GetDataTask(data_task=data_task, name="test")

        model_task = TrainTask(train_task=train_data_task, valid_task=valid_data_task)
        pred_task = PredTask(model_task=model_task, test_task=test_data_task)

        output_task = MakeOutputTask(pred_task=pred_task, test_task=test_data_task)

        checked_output_task = CheckAccuracyTask(
            pred_task=output_task,
            test_task=test_data_task,
            require_acc=0.9
        )

        s3_upload_task = UploadS3Task(output_task=checked_output_task)

        return s3_upload_task

    def run(self):
        self.dump(self.__class__.__name__)