# youtube-video-fetch-api
The ideology is:
1. Start a parallel process to get the apiKey and keep 10 seconds timer
2. At every 10 seconds the Celery task is called to execute the task(Currently it is complex to setup the celery so I just
added the thread to it).

# Files
Key Files:
```buildoutcfg
1. src/apiCall/task.py
2. src/apiCall/youtube.py
3. src/youtube/celery.py
4. src/apiCall/   {API Folder}
```

# Functionality Covered
```buildoutcfg
- Server call the YouTube API continuously in background (async) with some interval (say 10 seconds)
- fetch the latest videos for a predefined search query 
- It stores the data of videosin a database with proper indexes
- A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
- It should be scalable and optimised.
- Added support for supplying multiple API keys so that if quota is exhausted on one, it automatically uses the next available key.
```
# Instructions to start server
1 Create virtualenv: 
```buildoutcfg
cd src
virtualenv venv
```

2 Install required packages

```buildoutcfg
pip install -r requirements.txt
```
3 Makemigrations, migrate
```buildoutcfg
python manage.py makemigrations
python manage.py migrate
```
4 Createsuperuser
```
python manage.py createsuperuser
```
5 Runserver
```buildoutcfg
python manage.py runserver
```

# APIs
```buildoutcfg
http://127.0.0.1:8000/youtube/
```
GET Request will return data in following json:
 ```buildoutcfg
{
    "count": 62,
    "next": "http://127.0.0.1:8000/youtube/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "video_title": "Cricket Super Star Sachin Ramesh Tendulkar",
            "description": "Master Blaster playing some classical cover drives.",
            "publish_datetime": "2020-04-29",
            "thumbnail_url": "https://i.ytimg.com/vi/GEW7HDvGGD4/default.jpg"
        },
        {
            "id": 2,
            "video_title": "India vs pakistan cricket match | 10 overs | wcc2 gameplay",
            "description": "This is a game play highlights ssk scored 34 in just 7 balls and take a wicket and get man of the match award.",
            "publish_datetime": "2020-04-29",
            "thumbnail_url": "https://i.ytimg.com/vi/l75-qhaJFAY/default.jpg"
        },
        {
            "id": 3,
            "video_title": "Financ Secretary Dr Bilal Rasool Qazi live Cricket Match",
            "description": "Video from ushah832.",
            "publish_datetime": "2020-04-29",
            "thumbnail_url": "https://i.ytimg.com/vi/DtQVSjviqlw/default.jpg"
        }
    ]
}
```
The API is query capable and paginated.