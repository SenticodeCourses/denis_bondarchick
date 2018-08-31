from monitor import FolderMonitor
from tree import make_tree

path = '.'
some = FolderMonitor(path)
some.start()
# while True:
#     intakes = input()
#     if intakes == 'go':
#         some.start()
#     if intakes == 'stop':
#         some.stop()

make_tree(path)
