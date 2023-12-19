# ChatCraft: Automated WhatsApp Conversations

## Video Demo
[Watch the demo here](https://youtu.be/O1dv50w1hDM)

## Description
ChatCraft is an simple WhatsApp chat bot project that showcases expertise in web automation, smart command parsing, and dynamic content generation. Leveraging external APIs, it provides real-time information such as weather updates, news, and more. The project's robust reminder system enhances user engagement by delivering timely and personalized reminders.

## Usage
```bash
cd src
run main.py
```

## Key Features
1. **Web Automation with Selenium:**
    - Seamless interaction with the web version of WhatsApp using Selenium.
    - Robust element locating, waiting strategies, and browser automation.

2. **Text Processing and Command Parsing:**
    - Advanced text processing techniques for extracting and parsing user commands effectively.
    - Handles diverse command formats for an improved user experience.

3. **Dynamic Responses and Chat Interactions:**
    - Dynamic response generation based on user commands.
    - Interactive chat features delivering greetings, weather updates, news, jokes, quotes, and basic calculations.

4. **API Integration:**
    - Integration of external APIs for real-time data retrieval.
    - Proficient in making HTTP requests, processing JSON responses, and seamlessly integrating external data.

5. **Reminder System and Time Handling:**
    - Sophisticated reminder system for scheduling and delivering reminders.
    - Proficient in time-related operations, including parsing, formatting, and comparing time values.

## Usage
1. **Specify Target Group/Chat:**
    - Select a specific group or chat in the main function while accessing the `start` method of the class **Auto**.

2. **Specify Chrome Profile and Username:**
    - Set your `profile` and `username` to avoid rescanning the QR code for WhatsApp Web.

3. **Supported Commands:**
    - `!help`
    - `!add [numbers]`
    - `!multiply [numbers]`
    - `!yell [message]`
    - `!info`
    - `!greet [name]`
    - `!weather [location]`
    - `!news [category]`
    - `!quote`
    - `!joke`
    - `!define [word]`
    - `!reminder [time(24-hour)] [message]`

### Code Explanation:

First, I've created two classes: `Auto` and `Functions`. The role of the `Auto` class is to initialize the driver with specified chat name, profile data, and directory. It allows accessing web.whatsapp.com in an existing Chrome profile, eliminating the need to scan the QR code each time the bot runs. The `start` method opens the URL using the `driver.get` function from the Selenium module.

```python
class Auto:
    def start(self, chat_name, profile, user_name):
        # Code to initialize driver and open WhatsApp Web
        # ...
        self.get_group()
```

The get_group method is called at the end of the start method. It finds the group element based on the provided chat name, clicks on it, and initializes the text area for messages. A welcome message and emojis are then sent to the group. The start_reading method is invoked afterward.

```python
def get_group(self):
    # Code to locate the group, initialize the text area, and send a welcome message
    # ...
    self.start_reading()
```

The start_reading method continuously reads messages, checks if they start with "!", and calls the get_respond method to handle user commands. It sends the appropriate response back to the chat.
```python
def start_reading(self):
    while True:
        self.reminder()
        time.sleep(5)
        msg = self.get_chat()
        if msg.startswith("!"):
            # Code to prepare a response based on the user's command
            # ...
            self.send_input(send_msg)
        else:
            continue
```

The get_chat method retrieves the latest message by locating elements and returning the text of the last element.
```python
def get_chat(self):
    # Code to retrieve the latest message
    # ...
    return str(msg)
```

The reminder function handles reminders specified by the user. It parses the time, calculates the difference, and sends a reminder message at the appropriate time.
```python
elif msg.startswith("!reminder"):
    try:
        # Code to parse time, set reminders, and generate response
        # ...
        res = f"Sure! Will remind you to {self.rem.upper()} in {diff}"
        return res
```
This block ensures that reminders are sent to the user based on the specified time and message. A 5-second delay is added after sending the first reminder to prevent continuous reminders for one minute.
