import pytchat
import vlc

import os
import threading

YOUR_VIDEO_ID = ""  # Your stream id here as a string
EXTENSION = ".mp3"  # File extension of the sound files
COOLDOWN = 10       # Cooldown in seconds
REQUIRE_PREFIX = (False, "")  # (Bool, "prefix") If true, the message must start with the prefix to trigger the sound. If false, the message must only contain the trigger word.

class YoutubeSoundBoard:
    def __init__(self) -> None:
        self.onCooldown = False
        self.timer = None
        self.chat = pytchat.create(video_id=YOUR_VIDEO_ID)

    def summonSound(self, sound):
        '''Plays the sound from the sfx folder. Make sure the name of the sound is the same as the trigger.'''
        print("Playing sound " + sound + "...")
        
        try:
            p = vlc.MediaPlayer("sfx/" + sound + EXTENSION)
            p.play()
        except Exception as e:
            print("\nSound not found."  + "\n")
            return
        
        self.onCooldown = True
        self.timer = threading.Timer(COOLDOWN, self.__commandCooldown).start()

    def searchForSound(self, chatMessage):
        '''Currently, the message needs to contain ONLY the trigger word.'''
        if self.onCooldown:
            print("Can't accept inputs right now. Cooldown in effect. \n")
            return
        
        self.onCooldown = False
        chatMessage = chatMessage.lower()

        if REQUIRE_PREFIX[0] and chatMessage.startswith(REQUIRE_PREFIX[1]):
            print("Prefix command found. Searching for sound...")
            self.summonSound(chatMessage[len(REQUIRE_PREFIX[1]):])
            return
        elif REQUIRE_PREFIX[0] and not chatMessage.startswith(REQUIRE_PREFIX[1]):
            print("Prefix command not found. Ignoring...")
            return
        else:
            print(chatMessage + " was sent. Searching for sound...")
            self.summonSound(chatMessage)

    def createSoundList(self):
        '''Optional: This creates a text file with all the current sound triggers. This is useful for the viewers to know what sounds they can trigger. 
        '''
        sfxDir = "sfx"

        with open("soundList.txt", "w") as f:
            f.write("Possible sound commands:\n\n")
            for filename in os.listdir(sfxDir):
                filename = filename[:-4]
                f.write(filename + "\n")

    def __commandCooldown(self):
        print("Accepting Inputs Again\n")
        self.onCooldown = False

liveStream = YoutubeSoundBoard()

# Comment this out if you don't want to create a sound list file
liveStream.createSoundList()

# Loops until the stream is over or if something goes wrong
while liveStream.chat.is_alive():
    for c in liveStream.chat.get().sync_items():
        print(f"{c.datetime} {c.author.name} {c.message}")
        liveStream.searchForSound(c.message)

# Error handling
try:
    liveStream.chat.raise_for_status()
except pytchat.ChatdataFinished:
    print("chat data finished")
except Exception as e:
        print(type(e), str(e))