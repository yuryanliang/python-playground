from os import walk
import os

folder = os.getcwd() + "/data"

f = []


def scanfile(folder, f):
    for dirpath, _, filenames in walk(folder):

        print(filenames)
        # for file in filenames:
        #     print(file)
        #     path = (os.path.abspath(os.path.join(dirpath, file)))
        #     f.append(path)


scanfile(folder, f)

print(f)
# for i, file in enumerate(f):
#     print(i, file)
# def open():
#
#     with open('SampleTxt.txt') as fin:
#         for line in fin:
#             pass # do something

# open()