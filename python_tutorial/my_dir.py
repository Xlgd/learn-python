import os
import time
import stat
import sys


def format_time(mtime):
    return time.strftime('%m %d %H:%M', time.localtime(mtime))


def my_dir(path):
    files = [x for x in os.listdir(path)]
    print('total %d' % len(files))
    for file in files:
        file_info = os.stat(file)
        filemode = file_info.st_mode
        print('%s %d %s %s %4d %s %s' % (stat.filemode(filemode), file_info.st_nlink, file_info.st_uid,
                                         file_info.st_gid, file_info.st_size,
                                         format_time(file_info.st_mtime), file))


if __name__ == '__main__':
    my_dir(sys.argv[1])
