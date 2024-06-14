import optional as op
import pytchat
import Users

from config import YOUR_VIDEO_ID

activeUsers: Users.YTUser  = []    # List of active users on the stream

def main():
    # Optional: Creates a text file with all the current sound triggers. This is useful for the viewers to know what sounds they can trigger.
    op.createSoundList()

    chat = pytchat.create(video_id=YOUR_VIDEO_ID)

    print("We are live! Waiting for chat messages...")

    # Loops until the stream is over or if something goes wrong
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"{c.datetime} : {c.author.name} : {c.message}")

            user: Users.YTUser = Users.GetUser(activeUsers, c.author.name)

            print("User Object id: " + str(user))
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