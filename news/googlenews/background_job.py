from threading import Thread

from news.googlenews.fetcher import Fetcher
from news.models import News


class BackgroundJob(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._job = None
        self.__signal = True
        self.__times = 0

    def __retrieving_news(self):
        # while self.__signal:
        #     self.__times += 1
        #     time.sleep(1)
        #     print(f'hello world!! I say {s} - {self.__times}')
        f = Fetcher()
        data = f.top_headline()
        news_list = News.parse_dict(data)
        News.persist_to_database(news_list)

    def run(self):
        self.__retrieving_news()

    def stop(self):
        self.__signal = False
