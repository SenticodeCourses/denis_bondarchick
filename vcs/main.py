from monitor import FolderMonitor
from tree import make_tree

path = '.'
some = FolderMonitor(path)
some.start()
# while True:
#     intakes = input()
#     if intakes == 'start':
#         some.start_checking()
#     if intakes == 'stop':
#         some.stop_checking()

make_tree(path)