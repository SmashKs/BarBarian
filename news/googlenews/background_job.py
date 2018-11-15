import logging
import time
from threading import Thread
from typing import List

from pyfcm import FCMNotification

from external import FIREBASE_API_KEY
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
        self.__idle_interval_time = 15 * 60  # 15 mins

        self.__country_name = 'jp'

        self.__push_service = FCMNotification(api_key=FIREBASE_API_KEY)

    def run(self):
        self.__retrieving_news()

    def stop(self):
        self.__signal = False

    def celery_background(self):
        self.__retrieving_news()

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
            data_not_in_database = self.__persist_news(newses)  # type: List[News]

            for data in data_not_in_database:  # type: News
                self.__notify_subscribers(data, Subscriber.get_all_with_keywords())
            # endregion

            # Break time.
            self.__times += 1
            time.sleep(self.__idle_interval_time)
            logging.info(f'hello world!! I retrieved news - {self.__times}')

    def __persist_news(self, data):  # type: (BackgroundJob, List[News]) -> List[News]
        return News.persist_to_database(data)

    def __notify_subscribers(self, data, subscribers):  # type: (BackgroundJob, News, List[Subscriber]) -> None
        text = f'{data.title} {data.content}'
        firebase_subscribers_token = []

        # Collecting the subscribers who are interested in this news.
        for subscriber in subscribers:
            if any(keyword in text for keyword in subscriber.keywords):
                firebase_subscribers_token.append(subscriber.firebase_token)

        # If there's no subscribers, just return.
        if len(firebase_subscribers_token) == 0:
            return

        msg_data = {'title': 'Bullet News',
                    'news_title': data.title,
                    'news_body': data.description,
                    'news_author': data.author,
                    'image_url': data.urlToImage,
                    'new_url': data.url,
                    'published_date': data.published_at}
        self.__push_service.notify_multiple_devices(registration_ids=firebase_subscribers_token, data_message=msg_data)
