from threading import Thread, Lock
from time import gmtime, strftime
from infoRet import get_data_rss


class Daemon(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.mutex = Lock()
        self._quit = False

    def stopped(self):
        self.mutex.acquire()
        val = self._quit
        self.mutex.release()
        return val

    def stop(self):
        self.mutex.acquire()
        self._quit = True
        self.mutex.release()

    def run(self):
        while True:
            if str(strftime("%H:%M:%S", gmtime())) == ('12:00:00' or '24:00:00'):
                get_data_rss()


def main_fct():
    t = Daemon()
    t.start()


if __name__ == "__main__":
    main_fct()