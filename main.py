import gokart
import luigi
import numpy as np

import gokart_pipeline_sample

if __name__ == '__main__':
    gokart.add_config('./conf/param.ini')
    gokart.run()
