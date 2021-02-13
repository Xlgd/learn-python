import os

def search_files(substr):
    files = [x for x in os.listdir('.') if os.path.isfile(x)]
    dirs = [x for x in os.listdir('.') if os.path.isdir(x)]
    for file in files:
        if substr in file:
            print(file)
    for subdir in dirs:
        for file in [x for x in os.listdir(subdir) if os.path.isfile(x)]:
            if substr in file:
                print(file)


if __name__ == '__main__':
    search_files('test')
