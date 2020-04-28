from datetime import datetime
from googleapiclient.errors import HttpError
from apiCall.models import apiKeysModel, youtubeModel
from googleapiclient.discovery import build
import time


class youtube:
    def __init__(self):
        self._allKey = apiKeysModel.objects.all().order_by("pk")
        self._currentKeyIndex = 0
        self._currentKey = self._allKey[self._currentKeyIndex].key

    def getKey(self):
        return self._currentKey

    def nextKey(self):
        self._currentKeyIndex += 1

        try:
            self._currentKey = self._allKey[self._currentKeyIndex].key
        except:
            raise Exception("All_keys_expired")

        return self

    def getTheResults(self, nextPageKey=None):
        youtubeAPI = build('youtube', 'v3', developerKey=self._currentKey)
        if nextPageKey is not None:
            req = youtubeAPI.search().list(q='avengers',
                                           part='snippet',
                                           type='video',
                                           order='date',
                                           pageToken=nextPageKey,
                                           publishedAfter=datetime.utcfromtimestamp(
                                               (datetime.now().timestamp()) - 10000).
                                           strftime("%Y-%m-%dT%H:%M:%S.0Z"))
        else:
            req = youtubeAPI.search().list(q='avengers',
                                           part='snippet',
                                           type='video',
                                           order='date',
                                           pageToken=nextPageKey,
                                           publishedAfter=datetime.utcfromtimestamp((datetime.now().timestamp()) - 10).
                                           strftime("%Y-%m-%dT%H:%M:%S.0Z"))

        try:
            res = req.execute()
        except HttpError:

            try:
                self.nextKey()
                return self.getTheResults(nextPageKey)
            except:
                return None

        return res

    # def saveTheResults(self, dict):
    #     for i in dict:

    def saveResults(self):
        nextPageKey = None
        while True:
            print(nextPageKey)
            time.sleep(10)
            res = self.getTheResults(nextPageKey)
            nextPageKey = res['nextPageToken']
            print(res)
            if res is None:
                break
        print("The API KEYS are exhausted")
