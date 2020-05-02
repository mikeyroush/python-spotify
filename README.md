# python-youtube-spotify

Pulls songs from liked YouTube videos into a Spotify playlist

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes.

### Prerequisites

- A working command line
- A Google Cloud Services account
  - A JSON account token with access to the YouTube Data API
- An app registered with the Spotify Web API
  - A python file housing the app id and secret

### Installing and Running

Download the zip then create a virtual environment and install the dependencies from requirements.txt 

Make sure you have `virtualenv`

```console
foo@bar:~$ pip3 install virtualenv
```

Navigate to the correct directory then create and source a virtual environment and install the dependencies

```console
foo@bar:~$ cd /path/to/directory/here
foo@bar:~$ virtualenv venv
foo@bar:~$ source venv/bin/activate
(venv) foo@bar:~$ pip install -r requirements.txt
```

At this point, make sure you have the appropriate JSON files and/or comment out the undesired functionality. Finally, execute the program. (main.py includes full functionality to take a picture and process it while visionAPI.py uses pictures from the images directory)

Demo

```console
(venv) foo@bar:~$ python create_playlist.py
Please visit this URL to authorize this application: <YOUR_URL>
Enter the authorization code: <YOUR_CODE>
Found videos:
Carly Pearce Michael Ray  Finish Your Sentences (Lyric Video): https://www.youtube.com/watch?v=Tg1eq05y5t0
[youtube] Tg1eq05y5t0: Downloading webpage
query: Finish Your Sentences Carly Pearce, Michael Ray
results: spotify:track:2rhnO6nvKeuC8nSReRCXm2
Dustin Lynch  Thinking ‘Bout You (feat Lauren Alaina) [Official Audio]: https://www.youtube.com/watch?v=C_JBsxuDivg
[youtube] C_JBsxuDivg: Downloading webpage
query: Thinking ‘Bout You (feat. Lauren Alaina) [Official Audio] Dustin Lynch
Jimmie Allen  Make Me Want To (Official Music Video): https://www.youtube.com/watch?v=OVdemLamwHs
[youtube] OVdemLamwHs: Downloading webpage
query: Make Me Want To (Acoustic) Jimmie Allen
results: spotify:track:49Kr9I14W3zHWU3Jdm91qw
Willie Jones  Runs In Our Blood (Official Video): https://www.youtube.com/watch?v=0NCD30AzmaM
[youtube] 0NCD30AzmaM: Downloading webpage
query: Runs In Our Blood Willie Jones
results: spotify:track:2LU95Xw5MU6nSApasaZo2b
Russell Dickerson  Yours (Official Video): https://www.youtube.com/watch?v=g83se50wTrs
[youtube] g83se50wTrs: Downloading webpage
query: Yours (Intl Mix) Russell Dickerson
results: spotify:track:34lL92tDUFfTCD85nuVRrC
analyzed all songs
['spotify:track:2rhnO6nvKeuC8nSReRCXm2', 'spotify:track:49Kr9I14W3zHWU3Jdm91qw', 'spotify:track:2LU95Xw5MU6nSApasaZo2b', 'spotify:track:34lL92tDUFfTCD85nuVRrC']
created playlist
{'snapshot_id': 'MyxlMWRlNWJhMzg2MzU0OTljZTA0OTFiNGFmMmM0MmFiYTVmZDE0Nzlm'}
```

## Authors

* **Michael Roush** - *Project completion*

## License

Copyright © 2020 Michael Roush. All rights reserved.


