import os
import time
import threading

class FolderMonitor(threading.Thread):
    def __init__(self, path):
        threading.Thread.__init__(self)
        self.path = path
        self.current = None
        self.last = None
        self.added = None
        self.deleted = None
        self.deamon = True

    def difference(self):
        if self.last is not None:
            self.added = self.current - self.last
            self.deleted = self.last - self.current
        if self.current != self.last:
                if self.added is not None:
                    print('Даданы', self.added)
                if self.deleted is not None:
                    print('Выдалены', self.deleted)

    def run(self, soe=None):
        while True:
            self.last_user_input = input('input something: ')
            self.current = set(os.listdir(self.path))
            self.difference()
            self.last = self.current
            time.sleep(0.2)
