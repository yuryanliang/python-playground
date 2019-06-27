import re

# files = [ '/a/b/c/la_seg_x005_y003.png',
#           '/a/b/c/la_seg_x005_y003.npy',
#           '/a/b/c/la_seg_x004_y003.png',
#           '/a/b/c/la_seg_x004_y003.npy',
#           '/a/b/c/la_seg_x003_y003.png',
#           '/a/b/c/la_seg_x003_y003.npy', ]
#
# regex = re.compile(r'_x\d+_y\d+\.npy')
#
# selected_files = filter(regex.search, files)
# for i in selected_files:
#     print(i)


s3_files=[
    'sample.log',
    'logs/2006/January/sample.log',
    'logs/2006/February/sample2.log',
    'logs/2006/February/sample3.log',
    'logs/2006/February/sample4.log',
]

string='logs3as*'

try:
    # regex = re.compile(r'[')
    regex = re.compile(string)

except re.error:
    print("no valid")



i=bool(regex.match('logs/2006/January/sample.log'))
1==1

print(i)
# selected_files = filter(regex.search, s3_files )
# for i in selected_files:
#     print(i)