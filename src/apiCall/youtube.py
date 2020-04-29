from threading import Thread
from apiCall.models import apiKeysModel
import time
from apiCall.task import getTheYoutubeResultsSave, checkKey


# This class helps in key management and calling the task
class youtube:
    def __init__(self):
        self._allKey = apiKeysModel.objects.all().order_by("pk")
        self._currentKeyIndex = 0
        self._currentKey = self._allKey[self._currentKeyIndex].key

    # Get the current running key
    def getKey(self):
        return self._currentKey

    # fetching the next possible key
    def nextKey(self):
        self._currentKeyIndex += 1

        try:
            self._currentKey = self._allKey[self._currentKeyIndex].key
        except:
            raise Exception("All_keys_expired")

        return self

    # Start running the process and fetch details
    def saveResults(self):
        while True:
            time.sleep(10)  # 10 Seconds delay

            # It checks whether the key is not exhausted
            if checkKey(self._currentKey):
                Thread(target=getTheYoutubeResultsSave, args=(self._currentKey,)).start()  # Create a thread to
                # execute the task

                # getTheYoutubeResultsSave.delay(self._currentKey) # Start a celery process
            else:
                try:
                    self.nextKey()
                except:
                    # It breaks when all the key is exhausted
                    break
        print("The API KEYS are exhausted")
