# Modules
import tweepy
import re
import math
from time import sleep
from mycsv import Mycsv

# Twitter account keys
keys = {
    'bt': 'AAAAAAAAAAAAAAAAAAAAACpTgwEAAAAA3zWPK57M%2Bxcz1kxAzxWSbu1GGpY%3DnsoSrk8etDb8udFQipKvi1okoAqXHebRO06C4ctW43Rufyptbp',
    'ck': 'dCKKAsDw1KOWG6KajS92oPa6m',
    'cs': 'z7n07OGupHTf19BW1n6V1NZbTo8DjhwH5WQVKmNoHPbqKu25Wf',
    'at': '1567583209273040896-9XgTXfERKH9yXBI4mZXLX5Yv6GzQMU',
    'ats': 'XzruPITZRwhQLHR0gEdHw7CiRXS1tHTPqOBcWpf21MBmP'
}


def main():
    on = tweet(connect(), "I'm online 🟩")
    print('\033[1;32mOnline\033[m')  # Terminal
    while True:
        try:
            online(5)
        except KeyboardInterrupt:
            break
    del_tweet(connect(), tweet_id(on))
    print('\n\033[1;31mOffline\033[m')  # Terminal


def online(checks):
    """
    loop structure to check mentions and reply them
    :param checks: number of mentions checks. A LOT OF CHECKS FREEZES THE FUNCTION.
    """
    calculator = connect()
    n = 0
    while True:
        # Searching new mentions
        mentions = search('@calculatorbot_')
        new_mentions = []
        n += 1
        # Checking new mentions
        try:
            file = 'mentions.csv'
            c = Mycsv()
            csv_file = c.read(file)
            for mention in mentions:
                if [str(mention['id'])] not in csv_file:
                    new_mentions.append(mention)
                    c.write(mention['id'], file)
        except TypeError:
            pass
        # Answering
        if new_mentions != None and new_mentions != []:
            print(f'\033[1m[{len(new_mentions)} new mentions found]\033[m')  # Terminal
            for mention in new_mentions:
                answer = calculate(mention['text'])
                if answer != False:
                    reply(calculator, f'Answer = {answer}', mention['id'])
                else:
                    reply(calculator, 'Wrong format 😟 look in my profile for accepted formats', mention['id'])
                print(f"\033[1m[{mention['id']}, '{mention['text']}' answered]\n[answer: '{answer}']\033[m")  # Terminal
        else:
            print(f'\033[1m[No new mentions found]\033[m')  # Terminal
        if n == checks:
            break
        sleep(5)


def connect():
    """
    creates and returns a tweepy.Client() object with the keys from the keys dict object
    """
    client = tweepy.Client(
        consumer_key=keys['ck'],
        consumer_secret=keys['cs'],
        access_token=keys['at'],
        access_token_secret=keys['ats']
    )
    return client


def user_id(client):
    """
    gets a twitter account id
    :param client: the tweepy.Client() object
    :return: int value of the twitter account id
    """
    if id := re.search(r'id=([0-9]+)', str(client.get_me())):
        return int(id.group(1))


def tweet_id(tweet):
    """
    gets a tweet id
    :param tweet: a tweet object
    :return: int value of the tweet id
    """
    if id := re.search(r"'id': '([0-9]+)'", str(tweet)):
        return int(id.group(1))


def tweet(client, string):
    """
    tweet a text
    :param client: the tweepy.Client() object that will tweet
    :param string: the text of the tweet
    :return: response and json() with the tweet data
    """
    try:
        return client.create_tweet(text=string)
    except:
        raise Exception('\033[1;91m[Something went wrong with the tweet :(]\033[m')


def del_tweet(client, id):
    """
    deletes a tweet
    :param client: the tweepy.Client() object that will have a tweet deleted
    :param id: tweet's id of the tweet that'll be deleted
    :return: response
    """
    try:
        return client.delete_tweet(id)
    except:
        raise Exception('\033[1;91m[Something went wrong with the tweet deletion :(]\033[m')


def reply(client, string, id):
    """
    reply some tweet
    :param client: the tweepy.Client() object that will reply
    :param string: the text of the reply
    :param id: the tweet id that will be replied
    :return: json() with the reply data
    """
    try:
        return client.create_tweet(text=string, in_reply_to_tweet_id=id)
    except:
        raise Exception('\033[1;91m[Something went wrong with the reply:(]\033[m')


def search(q):
    """
    search a maximum amount of 10 tweets using a string query
    :param q: string query
    :return: (list of dicts with the id and the text of the tweets) or (string value '')
    """
    client = tweepy.Client(bearer_token=keys['bt'])
    tweets = client.search_recent_tweets(query=q, max_results=10)
    data = tweets.data
    results = []
    if not data is None and len(data) > 0:
        for item in data:
            results.append({'id': item.id, 'text': item.text})
        return results
    else:
        return None


def calculate(string):
    """
    returns the answer to a math problem in a tweet's string
    :param string: string with math operations
    :return: Answer | False
    """
    # Constants
    pi = math.pi
    e = math.e
    # String
    string = re.sub(r'@calculatorbot_', '', string)
    string = re.sub(r'e|E', str(e), string)
    string = re.sub(r'pi|PI|pI|Pi|π', str(pi), string)
    # Math
    try:
        answer = eval(string)
        if answer == int(string):
            return False
    except ZeroDivisionError:
        return 'Never divide by zero please 😵💫'
    except OverflowError:
        return 'The result is so big that it is out of my limits 🤖💫'
    except ValueError:
        return answer
    except Exception:
        return False


if __name__ == '__main__':
    main()