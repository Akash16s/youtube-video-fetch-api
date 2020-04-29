from datetime import datetime
from threading import Thread
from celery import shared_task
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from apiCall.models import youtubeModel


# This function checks whether the key is not exhausted
def checkKey(key):
    youtubeAPI = build('youtube', 'v3', developerKey=key)
    req = youtubeAPI.search().list(q='cricket',
                                   part='snippet',
                                   type='video',
                                   order='date',
                                   maxResults=1,
                                   publishedAfter=datetime.utcfromtimestamp(
                                       (datetime.now().timestamp())).
                                   strftime("%Y-%m-%dT%H:%M:%S.0Z"))
    try:
        req.execute()
    except HttpError:
        return False
    return True


def saveTheFigures(items):
    # This function saves the results in the database
    for i in items:
        youtubeModel.objects.create(
            video_title=i['snippet']['title'],
            description=i['snippet']['description'],
            publish_datetime=datetime.strptime((i['snippet']['publishedAt'][:-5]), "%Y-%m-%dT%H:%M:%S"),
            thumbnail_url=i['snippet']['thumbnails']['default']['url']
        )


# Function is a celery task for getting the youtube results
@shared_task
def getTheYoutubeResultsSave(apiKey, nextPageToken=None):
    # Creating youtubeAPI object with the apikey
    youtubeAPI = build('youtube', 'v3', developerKey=apiKey)

    # NextPageToken is for having the next possible results
    if nextPageToken is None:
        req = youtubeAPI.search().list(q='cricket',
                                       part='snippet',
                                       type='video',
                                       order='date',
                                       maxResults=50,
                                       publishedAfter=datetime.utcfromtimestamp(
                                           (datetime.now().timestamp()) - 10).strftime("%Y-%m-%dT%H:%M:%S.0Z"))
    else:
        req = youtubeAPI.search().list(q='cricket',
                                       part='snippet',
                                       type='video',
                                       order='date',
                                       maxResults=50,
                                       pageToken=nextPageToken,
                                       publishedAfter=datetime.utcfromtimestamp(
                                           (datetime.now().timestamp()) - 10).strftime("%Y-%m-%dT%H:%M:%S.0Z"))

    res = req.execute()

    # creating a thread to save the results
    Thread(target=saveTheFigures, args=(res['items'],)).start()

    # if the possible items is not 0 then go to the next page possible using pagination
    if len(res['items']) is not 0:
        if checkKey(apiKey):
            getTheYoutubeResultsSave(apiKey, res['nextPageToken'])
    return None
