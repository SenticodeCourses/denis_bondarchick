from monitor import FolderMonitor
from tree import make_tree

path = 'D:/temp/dev'
some = FolderMonitor(path)
some.run()
# while True:
#     intakes = input()
#     if intakes == 'go':
#         some.start()
#     if intakes == 'stop':
#         some.stop()

make_tree(path)
