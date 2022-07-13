"""
Write based on https://stackoverflow.com/questions/42255753/saving-files-to-a-subdirectory
"""

import os
import errno
import numpy as np


def do_not_overwrite(og_path, fname, ext, data, isnp=False):
    """
    Uses path, filename, and extension given. Appends a
    :param og_path: desired filepath without file name
    :param fname: name of file without extension
    :param ext: extension
    :param data: data to save
    :param isnp: True if wanting to save something in numpy
    :return:
    """
    saved = False
    num = 0
    path = os.path.join(og_path, "{}.{}".format(fname, ext))
    while not saved and num < 10:
        try:
            write(path, data, isnp)
            saved = True
            break
        except FileExistsError:
            path = os.path.join(og_path, "{}({:02d}).{}".format(fname, num, ext))
            num += 1

    return saved


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
