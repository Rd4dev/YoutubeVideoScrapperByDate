## Instructions

## modules

```
pip install google-auth-oauthlib
pip install google-api-python-client
```

## client_secrets.json file

Provided client_secrets.json is an empty file replace it with your own client_secrets.json

- Go to the Google Cloud Console and sign in with your Google account.
- Select the project you created earlier, or create a new project.
- In the left sidebar, click on "APIs & Services" and then click on "Credentials".
- Click on the "+ CREATE CREDENTIALS" button and select "OAuth client ID".
- Follow the prompts to configure the OAuth consent screen.
- Select "Desktop app" as the application type.
- Enter a name for your client ID and click "Create".
- Download the client_secrets.json file by clicking on the download icon next to the client ID you just created.

Once you have downloaded the client_secrets.json file, save it in the same directory as your Python script. In the youtube_client() function, replace "client_secrets.json" with the path to the client_secrets.json file on your local machine.

## API_KEY

The API key is a unique identifier that authenticates your requests to the YouTube Data API. You can obtain an API key by following the steps below:

- Go to the Google Cloud Console and sign in with your Google account.
- Click on the "Select a Project" drop-down menu in the top navigation bar and select "New Project".
- Enter a name for your project and click "Create".
- In the left sidebar, click on "APIs & Services" and then click on "Dashboard".
- Click on the "+ ENABLE APIS AND SERVICES" button at the top of the page.
- Search for "YouTube Data API" and click on the API.
- Click on the "Enable" button to enable the API.
- In the left sidebar, click on "Credentials" and then click on the "+ CREATE CREDENTIALS" button.
- Select "API key" from the drop-down menu and copy the API key that is generated.

In the code example you provided, replace "YOUR_API_KEY" with the API key you obtained from the Google Cloud Console.

## Channel ID

- Go to any video from the channel.
- Look at the URL in your browser's address bar.
- The channel ID is the string of letters and numbers that comes after "channel/" in the URL before the video ID.

If not available check the View Page Source and search for ChannelID which usually follows after the href="https://www.youtube.com/channel/UIOHUGXXXXXXXX" The "UIOHUGXXXXXXXX" is the Channel ID