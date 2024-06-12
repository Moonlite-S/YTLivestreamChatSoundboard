# YT Livestream Chat Soundboard

Have your Youtube livestream chat play audio based on their responses.

## Description

This small script uses both *pytchat* to communicate with your stream and *vlc* to play the audio.

Have your viewers type in a certain word in chat to play an audio file.

## Installation

- Download dependencies [ pip install -r requirements.txt ]

- Go to /server/config.py and replace the `YOUR_VIDEO_ID` with your stream ID when you start streaming.

- Run the file and you're good to go!

## Usage

`YOUR_VIDEO_ID` = The string ID in your Youtube livestream, usually everything after '/live/'. (ex: <https://youtube.com/live/adetx1rf2uTA>)

`COOLDOWN` = The amount of time in seconds where commands will not run.

`REQUIRE_PREFIX` = A (bool, prefix str) tuple. If true, chat messages *must* start with the *prefix* in order to play sounds. Default is False.

`EXTENSION` = The file extension for your audios. The files must be consistent with this. So if all files are mp3, everything must be mp3.

`VOLUME` = Adjusts the volume of the audio playback in a percentage.

### Sound List

When you run the file, it creates a txt file in the same directory that lists all the files in the 'sfx' folder. This is useful if you want to show the possible trigger commands to your chat. You can optionally comment this out if you don't want this.

#### Changelog

2/26/2024
> Added a volume variable.
>
> Fixed a bug where every message would proc the countdown
>
> Fixed a small bug where the text file in the 'sfx' folder would be included in the soundList.txt

2/25/2024
> Fixed a bug where requiring a prefix wouldn't play any sound.
