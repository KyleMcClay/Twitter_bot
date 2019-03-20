import json
import random

array_quotes_json = ["albert_camus_quotes.json", "friedrich_nietzsche_quotes.json", "fyodor_dostoevsky_quotes.json",
                    "jean_paul_sartre_quotes.json", "martin_heidegger_quotes.json", "soren_kierkegaard_quotes.json"]

# random number from len of array above
random_philosopher = array_quotes_json[random.randrange(len(array_quotes_json))]


# opens quotes from quotes in quote_scraper that is a .json
with open(f"C:\\Users\ksmcc\PycharmProjects\\twitter_bot\quote_scraper\{random_philosopher}", "r") as read_file:
    data = json.load(read_file)


# pick random quote
length_string = 300
while length_string >= 280:
    random_i = random.randrange(len(data))
    string = f"{data[random_i]['quote']}\n- {data[random_i]['author'].title()}"
    length_string = len(string)
