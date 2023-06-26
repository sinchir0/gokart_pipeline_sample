import gokart
import luigi

from gokart_sample.utils.template import GokartTask


class GetDataTask(GokartTask):
    data_task = gokart.TaskInstanceParameter()
    name = luigi.Parameter()

    def requires(self):
        return self.data_task

    def run(self):
        data = self.load()
        data = data[self.name]

        self.dump(data)
