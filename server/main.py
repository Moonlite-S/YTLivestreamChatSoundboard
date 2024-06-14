import optional as op
import pytchat
import Users

from database import createDatabase
from config import YOUR_VIDEO_ID

activeUsers  = []    # List of active users on the stream

def main():
    # Optional: Creates a text file with all the current sound triggers. This is useful for the viewers to know what sounds they can trigger.
    op.createSoundList()

    createDatabase()

    chat = pytchat.create(video_id=YOUR_VIDEO_ID)

    print("We are live! Waiting for chat messages...")

    # Loops until the stream is over or if something goes wrong
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.datetime} : {c.author.name} : {c.message}")

            user: Users.YTUser = Users.AddUser(c.author.name)

            active_user_names = [i[0] for i in activeUsers]
            if user.name not in active_user_names:
                activeUsers.append((user.name, user))
                print("Active users: " + str(activeUsers))

            user.searchForSound(c.message)

    # Error handling
    try:
        chat.raise_for_status()
    except pytchat.ChatdataFinished:
        print("chat data finished")
    except Exception as e:
            print(type(e), str(e))

if __name__ == "__main__":
    main()