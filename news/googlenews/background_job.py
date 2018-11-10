import time
from threading import Thread

from news.googlenews.fetcher import Fetcher
from news.models import News


class BackgroundJob(Thread):
    def __init__(self):
        Thread.__init__(self)

        self._fetcher = Fetcher()
        self._job = None

        self.__signal = True
        self.__times = 0

    def run(self):
        self.__retrieving_news()

    def stop(self):
        self.__signal = False

    def __retrieving_news(self):
        """
        Forever loop for retrieving all news data from remote server.
        """
        while self.__signal:
            # Fetch the data from remote news server.
            data = self._fetcher.top_headline('jp')  # type: dict

            # Parsing news data and Persisting them into database.
            newses = News.parse_dict(data)  # type: list
            News.persist_to_database(newses)

            # Break time.
            self.__times += 1
            time.sleep(30)
            print(f'hello world!! I retrieved news - {self.__times}')
