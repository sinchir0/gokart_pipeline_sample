import os
from io import StringIO

import boto3
import gokart
import pandas as pd

from gokart_pipeline_sample.utils.template import GokartTask


class UploadS3Task(GokartTask):
    output_task = gokart.TaskInstanceParameter()

    def requires(self) -> gokart.TaskInstanceParameter:
        return self.output_task

    def put_file(self, output_data: pd.DataFrame) -> None:
        s3 = boto3.resource("s3")
        bucket_name = os.environ["BUCKET_NAME"]

        with StringIO() as csv_buffer:
            output_data.to_csv(csv_buffer, index=False)
            s3.Object(bucket_name, "output.csv").put(Body=csv_buffer.getvalue())

    def run(self) -> None:
        output = self.load_data_frame()

        self.put_file(output)

        self.dump(self.__class__.__name__)
