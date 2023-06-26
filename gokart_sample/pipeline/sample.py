from logging import getLogger

from gokart_sample.utils.template import GokartTask

logger = getLogger(__name__)


class Sample(GokartTask):
    def run(self):
        self.dump("sample output")
