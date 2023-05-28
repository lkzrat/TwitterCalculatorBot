import project as pr
import pytest

# !!! tweepy module warning !!!
# Twitter tests


def test_connect():
    assert 'tweepy.client.Client object' in str(pr.connect())


def test_user_id():
    assert pr.user_id(pr.connect()) == 1567583209273040896


def test_tweet_id():
    tweet_object = """Response(data={'id': '1571921625167052801', 'text': "I'm online 🟩"}, includes={}, errors=[], meta={})"""
    assert pr.tweet_id(tweet_object) == 1571921625167052801


def test_tweet():
    with pytest.raises(Exception):
        wrong_client = 1
        pr.tweet(wrong_client, 'tweet')


def test_del_tweet():
    with pytest.raises(Exception):
        wrong_client = 1
        wrong_id = 1
        pr.del_tweet(wrong_client, wrong_id)


def test_reply():
    with pytest.raises(Exception):
        wrong_client = 1
        wrong_id = 1
        pr.reply(wrong_client, 'tweet', wrong_id)


def test_search():
    assert pr.search('Freddie Mercury') != None
    assert pr.search('Nobody will ever tweet ADNOWIJdialkdjwoaçIASODJW29034u') == None

# Calculate tests


def test_calculate_rightformat():
    for test, answer in zip(('@calculatorbot_ 1 + 1', '@calculatorbot_ (2 * 4) + 2', '@calculatorbot_ '), (2, 10, 1)):
        assert pr.calculate(test) == answer


def test_calculate_wrongformat():
    for test in ['@calculatorbot_ cat', '@calculatorbot_ -3 plus 2', '@calculatorbot_', '@calculatorbot_ 123']:
        assert pr.calculate(test) == False


def test_calculator_exceptions():
    assert pr.calculate('@calculatorbot_ 1/0') == 'Never divide by zero please 😵💫'
    assert pr.calculate('@calculatorbot_ 0**-1') == 'Never divide by zero please 😵💫'
    assert pr.calculate('@calculatorbot_ e**777666') == 'The result is so big that it is out of my limits 🤖💫'