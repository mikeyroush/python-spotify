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
...
```

## Authors

* **Michael Roush** - *Project completion*

## License

Copyright © 2020 Michael Roush. All rights reserved.


