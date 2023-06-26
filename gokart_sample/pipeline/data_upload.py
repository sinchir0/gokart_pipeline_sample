from sklearn.datasets import load_iris

from gokart_sample.utils.template import GokartTask

# 参考
# https://github.com/sansan-inc/randd-engineering-training/blob/master/python_training/batch/pipeline/tasks/data_uploader.py

# class GetDataTask(GokartTask):
#     def run(self) -> None:
#         data = load_iris()
#         return self.dump(data)
