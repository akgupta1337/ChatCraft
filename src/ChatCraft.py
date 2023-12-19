import sys
import time as Time
from selenium import webdriver
from src.BotFunctions import BotFunctions
from datetime import datetime, time as T
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChatCraft:
    """
    Class representing a WhatsApp bot named ChatCraft.
    """

    def __init__(self, profile, user_name):
        """
        Initializes ChatCraft with user profile and name.

        Parameters:
            profile (str): User's Chrome profile directory.
            user_name (str): Your Laptop's User name.
        """
        self.user_name = user_name
        self.profile = profile
        self.tame = T(0, 0)
        self.reminders = []
        self.options = self.configure_driver_options()
        self.driver = webdriver.Chrome(options=self.options)

    def configure_driver_options(self):
        """
        Configures Chrome driver options.

        Returns:
            webdriver.ChromeOptions: Configured Chrome options.
        """
        options = webdriver.ChromeOptions()
        options.add_argument(f"--profile-directory={self.profile}")
        options.add_argument(
            f"--user-data-dir=C:/Users/{self.user_name}/AppData/Local/Google/Chrome/User Data"
        )
        return options

    def start(self, chat_name):
        """
        Starts ChatCraft by opening WhatsApp and initializing the chat.

        Parameters:
            chat_name (str): Name of the WhatsApp chat.
        """
        self.chat_name = chat_name
        self.driver.get("https://web.whatsapp.com/")
        self.initialize_whatsapp()

    def initialize_whatsapp(self):
        """
        Initializes WhatsApp chat by selecting the group and sending a welcome message.
        """
        Time.sleep(10)
        group_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"span[title = '{self.chat_name}']")
            )
        )
        group_element.click()
        self.group_name = group_element.text

        group_member_element = self.driver.find_element(
            By.CSS_SELECTOR,
            "span[class = 'ggj6brxn gfz4du6o r7fjleex lhj4utae le5p0ye3 _11JPr selectable-text copyable-text']",
        )
        self.group_members = group_member_element.text
        Time.sleep(2)
        self.send_welcome_message()

    def send_welcome_message(self):
        """
        Sends a welcome message to the WhatsApp chat.
        """
        text_area = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[title = 'Type a message']")
            )
        )
        text_area.click()
        welcome_message = """
Hello there! I'm *ChatCraft* your friendly WhatsApp bot, here to assist you.
Use the command *!help* to see a list of available commands and learn how to interact with me.
Let's get started!
        """
        for line in welcome_message.split("\n"):
            text_area.send_keys(line + Keys.SHIFT + Keys.ENTER)
        text_area.send_keys(
            ":robot"
            + Keys.ENTER
            + ":danger"
            + Keys.ENTER
            + ":robot"
            + Keys.ENTER
            + ":danger"
            + Keys.ENTER
        )
        text_area.send_keys(Keys.ENTER)
        Time.sleep(5)
        self.start_reading_chats()

    def start_reading_chats(self):
        """
        Starts reading incoming messages in the chat.
        """
        while True:
            self.check_and_send_reminder()
            Time.sleep(5)
            latest_msg = self.read_latest_msg()
            if latest_msg.startswith("!"):
                response_msg = self.prepare_response(latest_msg.lower())
                if response_msg == None:
                    continue
                self.send_message(response_msg)
            else:
                continue

    def check_and_send_reminder(self):
        """
        Checks for pending reminders and sends them if it's time.
        """
        now = datetime.now().strftime("%H:%M")
        for reminder in self.reminders:
            if now == reminder["time"]:
                message = f"*[REMINDER]* ==> {reminder['message'].upper()}"
                self.send_message(message)
                Time.sleep(10)

    def send_message(self, message):
        """
        Sends a message to the WhatsApp chat.

        Parameters:
            message (str): Message to be sent.
        """
        text_area = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[title = 'Type a message']")
            )
        )
        text_area.click()
        for line in message.split("\n"):
            text_area.send_keys(line + Keys.SHIFT + Keys.ENTER)
        text_area.send_keys(Keys.ENTER)

    def read_latest_msg(self):
        """
        Reads the latest incoming message in the chat.

        Returns:
            str: Latest incoming message.
        """
        messages = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "_21Ahp"))
        )
        message = messages[-1].text
        return str(message)

    def prepare_response(self, message):
        """
        Prepares a response based on the incoming command.

        Parameters:
            message (str): Incoming command.

        Returns:
            str: Response message.
        """
        functions = BotFunctions()
        if message == "!help":
            return functions.help()

        elif message == "!info":
            Time.sleep(3)
            return functions.info(self.group_members, self.group_name)

        elif message.startswith("!greet"):
            return functions.greet(message)

        elif message.startswith("!weather"):
            return functions.weather(message)

        elif message.startswith("!news"):
            return functions.news(message)

        elif message.startswith("!quote"):
            return functions.quote()

        elif message.startswith("!joke"):
            return functions.joke()

        elif message.startswith("!define"):
            return functions.define(message)

        elif message.startswith("!add"):
            return functions.add(message)

        elif message.startswith("!multiply"):
            return functions.prod(message)

        elif message.startswith("!yell"):
            return functions.yell(message)

        elif message.startswith("!reminder"):
            confirmation_message, reminder_dict = functions.reminder(message)
            self.reminders.append(reminder_dict)
            return confirmation_message

        elif message == "!quit":
            self.send_message("Bot is going to sleep zzzzzz.")
            Time.sleep(3)
            self.driver.close()
            Time.sleep(2)
            self.driver.quit()
            sys.exit("Stopped All Bot Services.")


def main():
    print("You are not supposed to run this file directly")


if __name__ == "__main__":
    main()
