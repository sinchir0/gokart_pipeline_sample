import gokart
import luigi

from gokart_pipeline_sample.utils.template import GokartTask


class GetDataTask(GokartTask):
    data_task = gokart.TaskInstanceParameter()
    name = luigi.Parameter()

    def requires(self) -> gokart.TaskInstanceParameter:
        return self.data_task

    def run(self) -> None:
        data = self.load()
        data = data[self.name]

        self.dump(data)
