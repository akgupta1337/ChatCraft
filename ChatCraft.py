from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from datetime import time as t
from datetime import timedelta
import sys
import requests
import time
import random


def main():
    chat = Auto()
    group_name = "Your group name"
    profile = "Profile x"
    user_name = "your user name"
    chat.start(chat_name=group_name, profile=profile, user_name=user_name)


def add(msg):
    numbers = msg.split(" ", 1)[1]
    num = []
    for i in numbers:
        if i.isdigit():
            num.append(int(i))

    return str(sum(num))


def prod(msg):
    numbers = msg.split(" ", 1)[1]
    product = 1
    for i in numbers:
        if i.isdigit():
            product *= int(i)
    if product == 1:
        return "Please enter integers only."
    return str(product)


def yell(msg):
    sentence = msg.split(" ", 1)[1]
    yelled = ""
    for i in range(len(sentence)):
        if i % 2 == 0:
            yelled += sentence[i].upper()
        else:
            yelled += sentence[i].lower()
    return str(yelled)


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

    def reminder(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        for time1 in self.dicta:
            if current_time == time1["time"]:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, "div[title = 'Type a message']")
                    )
                ).send_keys(f"*[REMINDER]*  {time1['msg']}", Keys.ENTER)
                time.sleep(5)

    def send_input(self, msg):
        area = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[title = 'Type a message']")
            )
        )
        area.click()
        for line in msg.split("\n"):
            area.send_keys(line + Keys.SHIFT + Keys.ENTER)
        area.send_keys(Keys.ENTER)

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

    def get_respond(self, msg):
        if msg == "!help":
            return Functions().help()

        elif msg == "!info":
            names = self.driver.find_element(
                By.CSS_SELECTOR,
                "span[class = 'ggj6brxn gfz4du6o r7fjleex lhj4utae le5p0ye3 _11JPr selectable-text copyable-text']",
            )
            names = names.text
            return Functions().info(names, self.group_name)

        elif msg.startswith("!greet"):
            try:
                name = msg.split(" ")[1].title()
            except IndexError:
                return "Please provide name with space."
            return Functions.greet(name)

        elif msg.startswith("!weather"):
            try:
                locations = msg.split(" ")[1]
            except IndexError:
                return "Please provide location with space."

            return Functions.weather(locations)

        elif msg.startswith("!news"):
            try:
                category = msg.split(" ")[1]
                if category not in [
                    "business",
                    "entertainment",
                    "general",
                    "health",
                    "science",
                    "sports",
                    "technology",
                ]:
                    return "Please provide a valid category ('business, entertainment, general, health, science, sports, technology')"
            except Exception:
                return "Please provide a category ('business, entertainment, general, health, science, sports, technology')"

            return Functions.news(category)

        elif msg.startswith("!quote"):
            return Functions.quote()

        elif msg.startswith("!joke"):
            return Functions.joke()

        elif msg.startswith("!define"):
            try:
                word = msg.split(" ")[1]
            except Exception:
                return "Please a word separted by space."
            return Functions.define(word)

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

        elif msg.startswith("!add"):
            return add(msg)

        elif msg.startswith("!multiply"):
            return prod(msg)

        elif msg.startswith("!yell"):
            return yell(msg)

        elif msg == "!quit":
            self.send_input("Bot is going to sleep zzzzzz.")
            time.sleep(3)
            self.driver.close()
            time.sleep(2)
            self.driver.quit()
            sys.exit("Stopped All Bot Services.")

    def get_chat(self):
        # for getting latest msg
        msgs = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "_21Ahp"))
        )
        msg = msgs[-1].text
        return str(msg)


class Functions:
    def help(self):
        send = """
Here are few commmands you can try:
• `!help`
• `!add [numbers]`
• `!multiply [numbers]`
• `!yell [message]`
• `!info`
• `!greet [name]`
• `!weather [location]`
• `!news [category]`
• `!quote`
• `!joke`
• `!define [word]`
• `!reminder [time(24-hour)] [message]`
                    """
        return send

    def info(self, names, group):
        info = [
            "Discover the exceptional members of our community. Here are their names:",
            "Meet the stellar individuals who contribute to our group. Here is the list of names:",
            "Explore the distinguished members within our community. Here are their names:",
            "Get to know the preeminent contributors to our group. Here is the list of names:",
            "Introducing the outstanding individuals who shape our community. Here are their names:",
            "Learn about the remarkable members in our group. Here is the list of names:",
            "Meet the champions who make up our community. Here are their names:",
        ]
        res = "Group Name: " + group + "\n" + random.choice(info) + "\n"
        for name in names.split(", "):
            if name == "You":
                name = "agupta1337(Bot_Tester)"
            if "1" in name:
                continue
            res += "• " + name + "\n"

        return res.strip()

    def greet(name):
        current_time = datetime.now()
        hour = int(current_time.strftime("%I"))
        ampm = current_time.strftime("%p")

        if ampm == "AM":
            if hour in [12, 1, 2, 3]:
                midnight_greetings = [
                    f"Hello, night owl {name}! It's a peaceful midnight.",
                    f"Greetings {name}! Burning the midnight oil?",
                    f"Hey there {name}, it's the calm of midnight.",
                    f"Good midnight, {name}! Hope you're having a serene night.",
                    f"Welcome to the quiet hours, {name}! It's midnight.",
                    f"Hello {name}! Midnight musings await.",
                    f"Hey night owl {name}, ready for a quiet night?",
                    f"Midnight vibes, {name}! What's on your mind?",
                    f"Hello night wanderer {name}, it's the magical midnight.",
                    f"Good midnight, {name}! Time for some deep thoughts.",
                ]
                return random.choice(midnight_greetings)
            elif 4 <= hour <= 6:
                early_morning_greetings = [
                    f"Good morning {name}! Rise and shine—it's the early hours of a new day.",
                    f"Hello early bird {name}! Wishing you a wonderful morning.",
                    f"Greetings {name}! The morning sun welcomes you.",
                    f"Morning, {name}! Early risers catch the best moments.",
                    f"Good morning {name}! Seize the day with enthusiasm.",
                    f"Hello {name}, it's a brand new morning. Make it count!",
                    f"Rise and shine, {name}! The world awaits your presence.",
                    f"Good morning {name}! A new day, a new opportunity.",
                    f"Hello early riser {name}, embrace the morning glow.",
                    f"Morning vibes, {name}! Let the day unfold beautifully.",
                ]
                return random.choice(early_morning_greetings)

            elif 7 <= hour <= 11:
                early_morning_greetings = [
                    f"Good morning {name}! Rise and shine—it's the early hours of a new day.",
                    f"Hello early bird {name}! Wishing you a wonderful morning.",
                    f"Greetings {name}! The morning sun welcomes you.",
                    f"Morning, {name}! Early risers catch the best moments.",
                    f"Good morning {name}! Seize the day with enthusiasm.",
                    f"Hello {name}, it's a brand new morning. Make it count!",
                    f"Rise and shine, {name}! The world awaits your presence.",
                    f"Good morning {name}! A new day, a new opportunity.",
                    f"Hello early riser {name}, embrace the morning glow.",
                    f"Morning vibes, {name}! Let the day unfold beautifully.",
                ]
                return random.choice(early_morning_greetings)

        else:
            if hour in [12, 1, 2]:
                noon_greetings = [
                    f"Good afternoon {name}! How is your day going so far?",
                    f"Hello {name}! It's midday; hope you're having a productive time.",
                    f"Greetings {name}! The sun is at its peak—enjoy the moment.",
                    f"Hello there {name}, it's lunchtime! What's on your plate?",
                    f"Good noon, {name}! The day is halfway through; keep going!",
                    f"Hey {name}! Time for a brief break in the noon sunshine.",
                    f"Hello {name}, the clock strikes noon! Make it a good one.",
                    f"Greetings {name}! Hope your day is as bright as the noon sun.",
                    f"Hello {name}! Midday vibes—stay energized!",
                    f"Good afternoon, {name}! Halfway there; make it remarkable.",
                ]
                return random.choice(noon_greetings)

            elif 3 <= hour <= 5:
                afternoon_greetings = [
                    f"Hello, sunshine {name}! Afternoon vibes are in the air.",
                    f"Good afternoon {name}! How's your day shaping up?",
                    f"Greetings {name}! The afternoon brings a burst of energy.",
                    f"Hey there {name}, it's the lively afternoon hours.",
                    f"Good afternoon {name}! Make the most of this vibrant time.",
                    f"Hello {name}! Afternoon adventures await; are you ready?",
                    f"Hey {name}, it's the lively part of the day—enjoy!",
                    f"Good afternoon {name}! May your day be as bright as the sun.",
                    f"Greetings {name}! Afternoon moments are meant to be cherished.",
                    f"Hello {name}! Embrace the positive vibes of the afternoon.",
                ]
                return random.choice(afternoon_greetings)

            elif 6 <= hour <= 8:
                evening_greetings = [
                    f"Good evening {name}! Time to unwind and relax.",
                    f"Hello {name}! The evening beckons with tranquility.",
                    f"Greetings {name}! As the sun sets, enjoy the calm evening.",
                    f"Hey there {name}, it's the serene evening hours.",
                    f"Good evening {name}! Reflect on the day's accomplishments.",
                    f"Hello {name}! Evening magic is in the air; savor the moment.",
                    f"Hey {name}, it's the tranquil part of the day—enjoy!",
                    f"Greetings {name}! As the day winds down, find peace.",
                    f"Hello {name}! Evening vibes—relax and rejuvenate.",
                    f"Good evening, {name}! The night is young; make it memorable.",
                ]
                return random.choice(evening_greetings)

            elif 9 <= hour <= 11:
                night_greetings = [
                    f"Good night {name}! Wishing you a peaceful and restful night.",
                    f"Hello {name}, it's time to bid the day farewell. Good night!",
                    f"Greetings {name}! As the night falls, find serenity.",
                    f"Hey there {name}, the stars are out. Good night!",
                    f"Good night {name}! May your dreams be as bright as the stars.",
                    f"Hello {name}! Nighttime is here; embrace the quietude.",
                    f"Hey {name}, it's the calm of the night. Sleep well!",
                    f"Greetings {name}! Nighttime magic awaits. Sweet dreams!",
                    f"Hello {name}, it's time to recharge. Good night!",
                    f"Good night, {name}! Rest well and dream sweetly.",
                ]
                return random.choice(night_greetings)

    def weather(location):
        api_key = "your api key"
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={api_key}"
        )
        weather_data = weather_data.json()
        if (weather_data["cod"]) == 200:
            f = weather_data["main"]["feels_like"]
            c = (f - 32) * 5 / 9
            visibility = weather_data["visibility"]
            weather = weather_data["weather"][0]["main"]
            desc = weather_data["weather"][0]["description"]
            place = weather_data["name"]

            sunny1 = (
                f"Step outside in {place} and bask in the warmth of a delightful day with a temperature of {c:.2f}°C. "
                f"The sky is adorned with {desc}, making it a perfect moment to soak in the sunshine. "
                f"Visibility is at a stunning {visibility} meters. Enjoy the radiant weather!"
            )

            sunny2 = (
                f"Greet the day in {place} with a temperature of {c:.2f}°C, where the weather is displaying a canvas of {desc}. "
                f"As you venture out, revel in the clear skies and a visibility of {visibility} meters. "
                f"It's a picture-perfect day waiting for your exploration!"
            )

            sunny3 = (
                f"Embrace the weather in {place} with a current temperature of {c:.2f}°C. "
                f"The weather presents a stunning panorama of {desc}, creating a cheerful atmosphere. "
                f"With visibility reaching {visibility} meters, it's a splendid day to enjoy the outdoors!"
            )

            sunny4 = (
                f"In {place}, the thermometer reads {c:.2f}°C, inviting you to experience a day filled with {desc}. "
                f"As the sun shines brightly, revel in the clear skies and a visibility of {visibility} meters. "
                f"Make the most of this radiant weather!"
            )

            sunny5 = (
                f"Step into the weather of {place} where the temperature stands at {c:.2f}°C. "
                f"The weather boasts a charming display of {desc}, creating a picturesque scene. "
                f"With a visibility of {visibility} meters, it's a splendid time to enjoy the outdoors!"
            )

            # Collect the paragraphs in a list
            sunny = [sunny1, sunny2, sunny3, sunny4, sunny5]
            return random.choice(sunny)
        else:
            return "The entered city is not found."

    def news(category):
        url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=your api key"
        response = requests.get(url)
        response = response.json()
        news = []
        for item in response["articles"]:
            headline_desc = f"Headline: {(item['title'].split(':')[0])}\nDescription: {(item['description'])}"
            news.append(headline_desc)
        return random.choice(news)

    def quote():
        api_url = "https://api.api-ninjas.com/v1/quotes?category="
        response = requests.get(
            api_url,
            headers={"X-Api-Key": "your api key"},
        )
        response = response.json()
        res = f'{response[0]["quote"]}\n-{response[0]["author"]}'
        return res

    def joke():
        api_url = "https://api.api-ninjas.com/v1/jokes?limit="
        response = requests.get(
            api_url,
            headers={"X-Api-Key": "your api key"},
        )
        response = response.json()
        return response[0]["joke"]

    def define(word):
        api_url = "https://api.api-ninjas.com/v1/dictionary?word={}".format(word)
        response = requests.get(
            api_url,
            headers={"X-Api-Key": "your api key"},
        )
        response = response.json()
        if response["valid"] == True:
            defi = response["definition"]
            defi = defi[3:].split(";")[0]
            return str(defi)
        else:
            return "The entered word was not found. Please try a new word."


if __name__ == "__main__":
    main()
