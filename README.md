# ChatCraft: Automated WhatsApp Conversations
#### Video Demo:  https://youtu.be/O1dv50w1hDM
#### Description: **ChatCraft** is a chat bot project desgined to automate WhatsApp messages. You can use this bot by typing certain commands like !help, the bot interact with the the web version of WhatsApp ***https://web.whatsapp.com/***  using the power of *Selenium* and reply to those commands in real time.

#### Key Features:
1.	Web Automation with Selenium:
    - Employs Selenium for web automation, enabling seamless interaction with the web version of WhatsApp. Implements robust element locating, waiting strategies, and browser automation to streamline user interactions.
2.	Text Processing and Command Parsing:
    - Incorporates advanced text processing techniques to extract and parse user commands effectively. Handles diverse command formats and performs intelligent parsing for improved user experience.
3.	Dynamic Responses and Chat Interactions:
    - Demonstrates dynamic response generation based on user commands. Engages users with interactive chat features, delivering greetings, weather updates, news, jokes, quotes, and executing basic calculations.
4.	API Integration:
    - Integrates external APIs for real-time data retrieval, enriching user interactions. Proficient in making HTTP requests, processing JSON responses, and seamlessly integrating external data into the chat bot's responses.
5.	Reminder System and Time Handling:
    - Implements a sophisticated reminder system, efficiently scheduling and delivering reminders at specified times. Proficient in time-related operations, including parsing, formatting, and comparing time values for accurate reminders.

1. **Specify Target Group/Chat:**
    - Select any particular group or chat to deploy the chat bot in in the main function while accessing the `start` method of the class **Auto** to start the bot.

1. **Specify your chrome profile and username**
    - Select your `profile` and `username` so that you don't need to scan the QR code again and again for using WhatsApp Web.
1. **Supports for various commands like:**
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
#### Function of each command:
- `!help`
    - Returns a string or all commands which can be used by user.
- `!quote`
    - Another use of API to fetch a random quote and returns it. I used api ninjas website service to get api.
- `!joke`
    - Fetches a random joke and returns it. I used api ninjas website service to get api.

- `!info`
    - Returns the names of people who are in the group. Using a web element to fetch the text inside it which contains all names separted by ", " and appending them to a list while ignoring any names which are just numbers.
- `!add [numbers]`
    - Tries to add all the numbers provided and returns the sum. User can provide numbers like "1+2+3+4..." it will ignore anything which is not digit and append digits to list, then find sum of that list and return the value as a string. If the user enters only characters, it will return 0 as sum.

- `!multiply [numbers]`
    - Multiplies all the number provided and return the product. If the user enters only characters it will return error saying to enter digits.
- `!yell [message]`
    - Return a string with alternate characters in uppercase and lowercase.

- `!greet [name]`
    - Returns greeting with that name, the greeting is based on what time the user called that command for example in morning, midnight or evening. First we will use split function to split string based on space, at max 2 split will be made, and the 2nd element will be stored in name variable and then pass it as argument another function greet which will return the greeting.
- `!weather [location]`
    - Returns the temperature and visibility of entered location inside a paragraph (to make it sound more natural like human), using openweather API, if location not found returns an error message saying the entered location is not found.
- `!news [category]`
    - Fetches news related to that category using an API and returns news title and description. If user enters wrong category, return error message telling the user to use category from this list only.

- `!define [word]`
    - Another use of API to get definition of entered word, if not found, returns a error message. Using api ninjas service.
- `!reminder [time] [message]`
    - Excepts input of time in 24 hours format and message, calculates in how many minutes to remind, and sends success message to user like "will remind in x minutes", then stores the time in a list, and then before reading new message, a function reminder is called which checks all the times in that list, and if it is equal to current time, if so then return the message to use, else continue.

### Code Explaination:
First I have created 2 classes, class Auto, and class Functions, The function of class Auto is to create driver, using arguments like chat name, profile data and data directory, both of which are required to open web.whatsapp.com in a existing chrome profile, where you have already login on web whatsapp so everytime you run this bot, you don't have to scan the qr code to access whatsapp. Then we open the url using driver.get function from selenium module. This much code is defined in the class Auto, inside the method start() whose job is to just do this, start the driver and get the site.
```python
class Auto:
    def start(self, chat_name, profile, user_name):
        self.user_name = user_name
        self.profile = profile
        self.tame = t(0, 0)
        self.dicta = []
        self.chat_name = chat_name
        self.options = webdriver.ChromeOptions()
        self.options.add_argument(f"--profile-directory={self.profile}")
        self.options.add_argument(
            f"--user-data-dir=C:/Users/{user_name}/AppData/Local/Google/Chrome/User Data"
        )
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get("https://web.whatsapp.com/")
        self.get_group()
```


Next at end of start method, the method get_group() is called, inside this method, we find the element with that group name (which was passed as argument in start() method as chat_name) after finding that element, we click on that also fetch its inner text and store it in a variable self.group_name which will be used later. Then we find the element which has title "Type a message" which basically is our text area where we will enter the message, we find it and click on it and using send_keys function from selenium, we text our welcome message, but since it had \n new line, it would actually send messages in different lines, but we want it in one para, so we use for loop in the string.split("\n) and then type in every line then press shift+enter which creates line break in whatsapp chat, and then finally send some emojis like :robot + enter and so on...
after sending our welcome messsage another method start_reading() is called.

```python

def get_group(self):
    time.sleep(10)
    # for getting group
    group = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, f"span[title = '{self.chat_name}']")
        )
    )
    group.click()
    self.group_name = group.text
    time.sleep(2)
    # send msg in text area
    area = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[title = 'Type a message']")
        )
    )
    area.click()
    first_msg = """
Hello there! I'm *ChatCraft* your friendly WhatsApp bot, here to assist you.
Use the command *!help* to see a list of available commands and learn how to interact with me.
Let's get started!
    """
    for line in first_msg.split("\n"):
        area.send_keys(line + Keys.SHIFT + Keys.ENTER)
    area.send_keys(
        ":robot"
        + Keys.ENTER
        + ":danger"
        + Keys.ENTER
        + ":robot"
        + Keys.ENTER
        + ":danger"
        + Keys.ENTER
    )
    area.send_keys(Keys.ENTER)

    time.sleep(5)
    # start reading chats
    self.start_reading()

```

The start_reading method, is used to read messages and constantly check them if they start with "!" or not if not then contiue, if it starts then another method get_respond() is called, inside which there are many elif condtions which check what command user has typed, once that command is found, the code inside that elif condition is exceuted, usually inside elif another function is called which is form another class Function, which generates the appropriate respond and returns it to the elif return statement where this function was called.

```python
def start_reading(self):
    while True:
        self.reminder()
        time.sleep(5)
        msg = self.get_chat()
        if msg.startswith("!"):
            # now we preapre a proper respond to send based on what !... is
            send_msg = self.get_respond(msg.lower())
            if send_msg == None:
                continue
            # send msg in text area
            self.send_input(send_msg)
        else:
            continue
```

To get the lates message I used the function get_chat everytime, which find the all the elements with a particular tag, and returns them in a form of list, where the latest message is at index -1, then we just fetch the inner text of that element at index -1 then return it.

```python
def get_chat(self):
    # for getting latest msg
    msgs = WebDriverWait(self.driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "_21Ahp"))
    )
    msg = msgs[-1].text
    return str(msg)
```
If the command starts with "!" but is not in our get_respond method, the loop will continue as usual, here I have added 5 seconds delay before reading the lates message, to avoide spams etc...
#### Reminder function()
Actually there is on function reminder() which I want to explain, rest are easy. So when the user enters command "!reminder [time] [message]" in the elif conditions a code is run, not a function because there were some variables which were presend in the same class, and I did not wanted to paas it it another class since it would create confusion. So the code is like this.

first we split the message at max 2 times which will give us 3 elements, we only want to store the last 2 elements which are time and the message. Then we take the time and split it using (":") and store the hour and minute in there respective variables after converting them into integer, then we conver into time format using time module imported from datetime.
Then we create a dictionary self.dicta where we store the msg as key and its value and time as another key and tis value and append to a list remdict, then we get the current time using datetime.now() and covert it into strftime format and then split it to get hour and minute and then create 2 timedelta objects t1 and t2 using the variable of current time and our time, which are in hour and minute variable, and the find the difference between which is in hh:mm format, we then split it again to get hour and minutes, and if hour is 0 we create a variable diff, which is a string, having minutes + "minutes", and if hour is nonzero then our diff is hour + "hours and " + minutes + "minutes"
this diff is basically our string which we will send to user, sayiing, will remind you to {msg} in {diff}.
where diff is just in how many minutes the user will be reminded.


Then in our start_reading method, before reading new message the function reminder is called which checks in our list which contained dict of msg and time. For every element in that list, it compares the time key's value to presenet time, and if they are equal then the user is reminded whatever message they had given. This would have continued nonstop till the current time is becomes different, to fix this issue, i added 5 second delay after sending first reminder, so the user can be kept getting reminder every 5 seconds for 1 whole minute.

```python
elif msg.startswith("!reminder"):
    try:
        re, tim, mesg = msg.split(" ", 2)
    except Exception:
        return "Please enter in following format !reminder [time] [message] separated with space, no quotation or brackets \n time in format (Hour:Minute),format 24 hours"
    hou, minu = tim.split(":")
    hou = int(hou)
    minu = int(minu)
    tame = t(hou, minu)
    tame = tame.strftime("%H:%M")
    self.tame = tame
    self.rem = mesg
    remdict = {"msg": self.rem, "time": self.tame}
    self.dicta.append(remdict)
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    ch, cm = current_time.split(":")

    t2 = timedelta(hours=hou, minutes=minu)
    t1 = timedelta(hours=int(ch), minutes=int(cm))

    diff = str(t2 - t1)
    hour, minute, sec = diff.split(":")
    if hour == "0":
        diff = minute + " minutes"
    else:
        diff = hour + " hour and " + minute + " minutes"
    res = f"Sure! Will remind you to {self.rem.upper()} in {diff}"
    return res

```
