import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import datetime

# Set the API key and channel ID
API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'ChannelID'

# Set the date for which you want to retrieve the videos
search_start_date = datetime.datetime(year=2021, month=3, day=10).strftime('%Y-%m-%dT00:00:00Z')
search_end_date = datetime.datetime(year=2023, month=5, day=13).strftime('%Y-%m-%dT00:00:00Z')

# Define the YouTube API client
def youtube_client():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        'client_secrets.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    credentials = flow.run_local_server(port=0)
    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)
    return youtube

# Retrieve the videos from the YouTube API
def get_channel_videos():
    youtube = youtube_client()

    request = youtube.search().list(
        part="id,snippet",
        channelId=CHANNEL_ID,
        maxResults=50,
        order="date",
        publishedAfter=search_start_date,
        publishedBefore=search_end_date,
        type='video'
    )
    response = request.execute()

    videos = []
    for item in response['items']:
        video = {
            'title': item['snippet']['title'],
            'url': f'https://www.youtube.com/watch?v={item["id"]["videoId"]}',
            'published_date': item['snippet']['publishedAt']
        }
        videos.append(video)

    return videos

# Print the list of videos
videos = get_channel_videos()
for video in videos:
    print(video)
