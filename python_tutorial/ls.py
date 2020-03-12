import os, argparse, time


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", help="display the details about the file",
    action="store_true")
    parser.add_argument("-lh", help="show the file size (kb)",
    action="store_true")

    args = parser.parse_args()
    local_dir = os.getcwd()
    if args.l is True:
        filenames = os.listdir(local_dir)
        filetimes  = []
        fileslength = []
        filesmode = []

        for name in filenames:
            temp_path = os.path.join(local_dir, name)
            state = os.stat(temp_path)
            modified_time = time.ctime(state.st_atime)
            length = str(state.st_size)
            filetimes.append(modified_time)
            fileslength.append(length)

        print('LastWriteTime' + '\t' * 3 + 'Name' + '\t' * 2 + 'Length' + '\n')
        for time, name, length in zip(filetimes, filenames, fileslength):
            print(time + '\t' + name + '\t' * 2 + length)
    elif args.lh is True:
        filenames = os.listdir(local_dir)
        filesize = []

        for name in filenames:
            temp_path = os.path.join(local_dir, name)
            fsize = os.path.getsize(temp_path)
            fsize = fsize / float(1024)
            filesize.append(str(round(fsize, 2)))

        print('Name' + '\t' * 2 + 'Size(KB)' + '\n')
        for name, size in zip(filenames, filesize):
            print(name + '\t' * 2 + size)
        
        
    else:
        filenames = os.listdir(local_dir)

        for name in filenames:
            print(name, end='\n')