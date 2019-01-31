from slackclient import SlackClient

from external import SLACK_API_KEY


class SlackBot:
    API_CHAT_MSG = 'chat.postMessage'
    BOT_NAME = 'News Bot'
    DEFAULT_CHANNEL = 'news_notification'

    def __new__(cls, *p, **k):
        if '_the_instance' not in cls.__dict__:
            cls._the_instance = object.__new__(cls)
        return cls._the_instance

    def __init__(self):
        self.__slack_client = SlackClient(SLACK_API_KEY)

    def send_msg_to(self, text='', channel=DEFAULT_CHANNEL):
        self.__slack_client.api_call(SlackBot.API_CHAT_MSG,
                                     username=SlackBot.BOT_NAME,
                                     channel=channel,
                                     text=text)

    def send_formatted_msg_to(self, text='', channel=DEFAULT_CHANNEL):
        self.__slack_client.api_call(SlackBot.API_CHAT_MSG,
                                     username=SlackBot.BOT_NAME,
                                     mrkdwn=True,
                                     channel=channel,
                                     text=text)


if __name__ == '__main__':
    SlackBot().send_msg_to('hello world!!')
