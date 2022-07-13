"""
Write based on https://stackoverflow.com/questions/42255753/saving-files-to-a-subdirectory
"""

import os
import errno
import numpy as np


def write(path, text, is_np=False):
    if os.path.isfile(path):
        raise FileExistsError
    try:
        if is_np:
            np.savetxt(path, text, delimiter=",")
        else:
            with open(path, 'w') as outFile:
                outFile.write(text)
    except IOError as exception:
        raise IOError("%s: %s" % (path, exception.strerror))


if __name__ == '__main__':
    pass
