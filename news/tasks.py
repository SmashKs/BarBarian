from celery import shared_task

from news.googlenews import news_job


@shared_task(ignore_result=True)
def background_fetch_news():
    news_job.celery_background()
