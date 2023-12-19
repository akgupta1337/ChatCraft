from ChatCraft import ChatCraft


def main():
    """
    Before starting I suggest you to create a new profile in chrome and login with whatsapp in that,
    then right click on the new chrome shorcut of your profile > show properties and in the Target section 
    at the end you will see something like Profile 2 or whatever number, put that here since it will sign you
    out while opening the browser.

    """
    
    test_bot = ChatCraft(profile="Profile X", user_name="your user name")

    test_bot.start(chat_name="exact name of chat you want to deploy this bot in")


if __name__ == "__main__":
    main()
