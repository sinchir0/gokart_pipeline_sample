import luigi
import numpy as np
import gokart

import gokart_sample

if __name__ == '__main__':
    gokart.add_config('./conf/param.ini')
    gokart.run()
