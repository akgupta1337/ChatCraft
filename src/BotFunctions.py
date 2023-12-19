from datetime import datetime, time as T, timedelta
import requests
import random


class BotFunctions:
    """
    Class containing various functions for the ChatCraft bot.
    """

    def help(self):
        """
        Returns a help message with a list of available commands.
        """
        help_message = """
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
        return help_message

    def info(self, group_member_names, group_name):
        """
        Generates a message introducing group members.

        Parameters:
            group_member_names (str): Names of group members.
            group_name (str): Name of the group.

        Returns:
            str: Group Name and Member names.
        """
        info = [
            "Discover the exceptional members of our community. Here are their names:",
            "Meet the stellar individuals who contribute to our group. Here is the list of names:",
            "Explore the distinguished members within our community. Here are their names:",
            "Get to know the preeminent contributors to our group. Here is the list of names:",
            "Introducing the outstanding individuals who shape our community. Here are their names:",
            "Learn about the remarkable members in our group. Here is the list of names:",
            "Meet the champions who make up our community. Here are their names:",
        ]
        group_info_message = (
            "Group Name: " + group_name + "\n" + random.choice(info) + "\n"
        )
        for member_name in group_member_names.split(", "):
            if "1" in member_name:
                continue
            group_info_message += "• " + member_name + "\n"

        return group_info_message.strip()

    def greet(self, message):
        """
        Generates a greeting message based on the time of day and user's name.

        Parameters:
            message (str): Input message with the user's name.

        Returns:
            str: Greeting message.
        """

        try:
            name = message.split(" ")[1].title()
        except IndexError:
            return "Please provide name with space."

        current_time = datetime.now()
        hour = int(current_time.strftime("%I"))
        am_or_pm = current_time.strftime("%p")

        if am_or_pm == "AM":
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

    def weather(self, message):
        """
        Retrieves and formats current weather information for a specified location.

        Parameters:
            message (str): Input message with the location.

        Returns:
            str: Weather information message.
        """
        try:
            location = message.split(" ")[1]
        except IndexError:
            return "Please provide location with space."

        api_key = "531aaa0d8fa4ea05b72c38b2e641d698"
        weather_data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&APPID={api_key}"
        )
        weather_data = weather_data.json()
        if (weather_data["cod"]) == 200:
            temp_farheniet = weather_data["main"]["feels_like"]
            temp_celsius = (temp_farheniet - 32) * 5 / 9
            visibility = weather_data["visibility"]
            weather = weather_data["weather"][0]["main"]
            desc = weather_data["weather"][0]["description"]
            place = weather_data["name"]

            weather_description = (
                f"The current weather at {place} is {weather} and it feels like {temp_celsius:.2f}°C. "
                f"The conditions are {desc.lower()} with a visibility of {visibility} meters."
            )
            return weather_description
        else:
            return "The entered city is not found."

    def news(self, message):
        """
        Retrieves and formats top news headlines for a specified category.

        Parameters:
            message (str): Input message with the news category.

        Returns:
            str: News information message.
        """
        try:
            category = message.split(" ")[1]
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

        url = f"https://newsapi.org/v2/top-headlines?country=in&category={category}&apiKey=c47fd280ef5f4a74b6071ea70660e37a"
        response = requests.get(url)
        response = response.json()
        news = []
        for item in response["articles"]:
            headline_desc = f"Headline: {(item['title'].split(':')[0])}\nDescription: {(item['description'])}"
            news.append(headline_desc)
        return random.choice(news)

    def quote(self):
        """
        Retrieves and formats a random quote.

        Returns:
            str: Formatted quote.
        """
        api_url = "https://api.api-ninjas.com/v1/quotes?category="
        response = requests.get(
            api_url,
            headers={"X-Api-Key": "D/9erABklSFyhWs9tQZtiA==jcdhINw8w6lWgguH"},
        )
        response = response.json()
        quote = f'{response[0]["quote"]}\n-{response[0]["author"]}'
        return quote

    def joke(self):
        """
        Retrieves and formats a random joke.

        Returns:
            str: Formatted joke.
        """
        api_url = "https://api.api-ninjas.com/v1/jokes?limit="
        response = requests.get(
            api_url,
            headers={"X-Api-Key": "D/9erABklSFyhWs9tQZtiA==jcdhINw8w6lWgguH"},
        )
        joke = response.json()
        return joke[0]["joke"]

    def define(self, message):
        """
        Retrieves and formats the definition of a specified word.

        Parameters:
            message (str): Input message with the word.

        Returns:
            str: Definition of the word.
        """
        try:
            word = message.split(" ")[1]
        except Exception:
            return "Please a word separted by space."

        api_url = "https://api.api-ninjas.com/v1/dictionary?word={}".format(word)
        response = requests.get(
            api_url,
            headers={"X-Api-Key": "D/9erABklSFyhWs9tQZtiA==jcdhINw8w6lWgguH"},
        )
        response = response.json()
        if response["valid"] == True:
            definition = response["definition"]
            definition = definition[3:].split(";")[0]
            return str(definition)
        else:
            return "The entered word was not found. Please try a new word."

    def add(self, msg):
        """
        Performs addition on a list of numbers provided in the message.

        Parameters:
            msg (str): Input message with numbers.

        Returns:
            str: Formatted addition result.
        """
        numbers = msg.split(" ", 1)[1]
        num = []
        for i in numbers:
            if i.isdigit():
                num.append(int(i))

        return str(f"{numbers} = {sum(num)}")

    def prod(self, msg):
        """
        Performs multiplication on a list of numbers provided in the message.

        Parameters:
            msg (str): Input message with numbers.

        Returns:
            str: Formatted multiplication result.
        """
        numbers = msg.split(" ", 1)[1]
        product = 1
        for i in numbers:
            if i.isdigit():
                product *= int(i)
        if product == 1:
            return "Please enter integers only."
        return str(f"{numbers} = {product}")

    def yell(self, msg):
        """
        Changes the case of characters in a message to create a 'yelling' effect.

        Parameters:
            msg (str): Input message.

        Returns:
            str: 'Yelled' message.
        """
        sentence = msg.split(" ", 1)[1]
        yelled_message = ""
        for i in range(len(sentence)):
            if i % 2 == 0:
                yelled_message += sentence[i].upper()
            else:
                yelled_message += sentence[i].lower()
        return str(yelled_message)

    def reminder(self, message):
        """
        Parses a reminder message and schedules it for future delivery.

        Parameters:
            message (str): Input message with reminder details.

        Returns:
            tuple: Confirmation message and reminder dictionary.
        """
        try:
            _, time, message = message.split(" ", 2)

        except Exception:
            return "Please enter in following format !reminder [time] [message] separated with space, no quotation or brackets \n time in format (Hour:Minute),format 24 hours"

        user_hour, user_minute = map(int, (time.split(":")))
        time_var = T(user_hour, user_minute).strftime("%H:%M")
        time_var = time_var
        reminder_message = message
        reminder_dict = {"message": reminder_message, "time": time_var}
        current_hour, current_minute = datetime.now().strftime("%H:%M").split(":")
        user_time = timedelta(hours=user_hour, minutes=user_minute)
        current_time = timedelta(hours=int(current_hour), minutes=int(current_minute))

        minute_difference = str(user_time - current_time)
        hour, minute, _ = minute_difference.split(":")

        if hour == "0":
            remind_in_message = str(int(minute)) + " minutes"
        else:
            remind_in_message = (
                str(int(hour)) + " hour and " + str(int(minute)) + " minutes"
            )

        confirmation_message = f"Sure! Will remind you to *{reminder_message.upper()}* in {remind_in_message}"
        return (confirmation_message, reminder_dict)


def main():
    print("You are not supposed to run this file directly")


if __name__ == "__main__":
    main()
