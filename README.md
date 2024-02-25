# YT Livestream Chat Soundboard

Have your Youtube livestream chat play audio based on their responses.

## Description

This small script uses both *pytchat* to communicate with your stream and *vlc* to play the audio.

Have your viewers type in a certain word in chat to play an audio file.

## Usage

- Download dependencies first ([pytchat](https://github.com/taizan-hokuto/pytchat?tab=readme-ov-file) and [vlc](https://pypi.org/project/python-vlc/)).

Or you can just install using pip or pip3:

`pip install pytchat`

`pip install python-vlc`

- Download the Python file in releases or clone the repo at:

`https://github.com/Moonlite-S/YTLivestreamChatSoundboard.git`

- Ensure there is a 'sfx' folder. If there isn't one, create one. That is where you'll place all your audio files in. As you place your files, please keep the naming to just letters to ensure the files get read correctly. Files are *not* case sensitive. Keep file extensions consistent as well.

- Replace the `YOUR_VIDEO_ID` with your stream ID when you start streaming.

- Run the file and you're good to go!

`COOLDOWN` = The amount of time in seconds where commands will not run.

`REQUIRE_PREFIX` = A (bool, prefix str) tuple. If true, chat messages *must* start with the *prefix* in order to play sounds. Default is False.

### Sound List

When you run the file, it creates a txt file in the same directory that lists all the files in the 'sfx' folder. This is useful if you want to show the possible trigger commands to your chat.

#### Changelog

2/25/2024
> Fixed a bug where requiring a prefix wouldn't play any sound.
