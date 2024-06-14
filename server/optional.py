import os
import config

def createSoundList():
    '''Optional: This creates a text file with all the current sound triggers. This is useful for the viewers to know what sounds they can trigger. 
    '''
    sfxDir = "sfx"

    with open("soundList.txt", "w") as f:
        f.write("Possible sound commands:\n\n")
        for filename in os.listdir(sfxDir):
            if filename.endswith(config.EXTENSION):
                filename = filename[:-4]
                f.write(filename + "\n")