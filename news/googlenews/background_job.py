import time
from threading import Thread
from typing import List

from news.googlenews.fetcher import Fetcher
from news.models import News, Subscriber


class BackgroundJob(Thread):
    """
    Running on the background service for doing some jobs.
    """

    def __init__(self):
        Thread.__init__(self)

        self._fetcher = Fetcher()
        self._job = None

        self.__signal = True
        self.__times = 0

        self.__country_name = 'jp'

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
            data = self._fetcher.top_headline(self.__country_name)  # type: dict

            # Parsing news data and Persisting them into database.
            newses = News.parse_dict(data, self.__country_name)  # type: list

            # region XXX(jieyi): 2018-11-11 to be a decorator.
            data_not_in_database = self.__persist_news(newses)

            for data in data_not_in_database:
                self.__notify_subscribers(data, Subscriber.get_all_with_keywords())
            # endregion

            # Break time.
            self.__times += 1
            time.sleep(40)
            print(f'hello world!! I retrieved news - {self.__times}')

    def __persist_news(self, data):  # type: (BackgroundJob, List[News]) -> List[News]
        return News.persist_to_database(data)

    def __notify_subscribers(self, data, subscribers):  # type: (BackgroundJob, News, List[Subscriber]) -> None
        text = f'{data.title} {data.content}'

        for subscriber in subscribers:
            if any(keyword in text for keyword in subscriber.keywords):
                # TODO(jieyi): 2018-11-11 Send the News to the subscriber.
                ...
