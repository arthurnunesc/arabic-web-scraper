from bs4 import BeautifulSoup
import requests
from bidi.algorithm import get_display
import pyarabic.araby as araby


url_word = "https://arabic.fi/words/322"
url_verb = "https://arabic.fi/words/1027"
url_random = "https://arabic.fi/random-word"


def get_word_info(url_number, invert_strings=False):
    url_base = "https://arabic.fi/words/"
    url = url_base + str(url_number)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    if "Sorry" in soup.find("h1").get_text():
        return False
    else:
        word_in_arabic_with_diacritics = soup.select_one("span").get_text()

        word_in_arabic_without_diacritics = araby.strip_diacritics(
            word_in_arabic_with_diacritics
        )
        word_in_arabic_with_diacritics_inverted = get_display(
            word_in_arabic_with_diacritics
        )
        word_in_arabic_without_diacritics_inverted = get_display(
            (word_in_arabic_without_diacritics)
        )
        word_pronunciation = soup.select_one("div.word-phonetic.phonetic").get_text()

        # Fetches word meaning and declension and separates them in two variables
        word_meaning_and_declension = soup.select_one(
            "div.word-declension-info-text"
        ).small.get_text()
        word_meaning_and_declension = word_meaning_and_declension.split(" – ")
        word_meaning = word_meaning_and_declension[0]
        if word_meaning_and_declension[1] == " ":
            word_declension = "no declension"
        else:
            word_declension = word_meaning_and_declension[1]

        # Check if there is an audio for the word, if not assigns "no word audio" to its variable
        if soup.find("div", class_="word-sound") != None:
            word_audio = soup.find("div", class_="word-sound").find("amp-audio")["src"]
        else:
            word_audio = "no word audio"

        # Fetches word part of speech and pattern
        word_part_of_speech_and_pattern = soup.select("div.similar-info")

        # Checks if we really have the right information and not the "Category" part of the word
        if len(word_part_of_speech_and_pattern) > 1:
            if (
                "Part of speech: " in word_part_of_speech_and_pattern[1].get_text()
                or "Pattern: " in word_part_of_speech_and_pattern[1].get_text()
            ):
                word_part_of_speech_and_pattern = word_part_of_speech_and_pattern[1]
            elif (
                "Part of speech: " in word_part_of_speech_and_pattern[0].get_text()
                or "Pattern: " in word_part_of_speech_and_pattern[0].get_text()
            ):
                word_part_of_speech_and_pattern = word_part_of_speech_and_pattern[0]
        elif word_part_of_speech_and_pattern == []:
            word_part_of_speech_and_pattern = False
        else:
            word_part_of_speech_and_pattern = word_part_of_speech_and_pattern[0]

        # Checks if there is any word_part_of_speech_and_pattern
        if word_part_of_speech_and_pattern:
            # Parses part of speech from the variable containing it and the pattern
            if "Part of speech: " in word_part_of_speech_and_pattern.get_text():
                word_part_of_speech = word_part_of_speech_and_pattern.get_text().split(
                    ". "
                )
                word_part_of_speech = word_part_of_speech[0].split(": ")
                word_part_of_speech = word_part_of_speech[1].strip()
            else:
                word_part_of_speech = "no part of speech"
            # Checks if word pattern was fetched, if not, assigns "no pattern" to its variable
            if "Pattern: " in word_part_of_speech_and_pattern.get_text():
                word_pattern = (
                    word_part_of_speech_and_pattern.select_one("a").get_text().strip()
                )
            else:
                word_pattern = "no pattern"
        else:
            word_pattern = "no pattern"
            word_part_of_speech = "no part of speech"

        # Gets word link
        word_arabicfi_link = soup.find("link")["href"]

        # Checks if the word has a context sentence
        if "Using the word" in str(soup.find("h2")):
            has_context_sentence = True
        else:
            has_context_sentence = False

        result = [
            url_number,
        ]
        if invert_strings:
            result += [
                word_in_arabic_without_diacritics_inverted,
                word_in_arabic_with_diacritics_inverted,
            ]
        else:
            result += [
                word_in_arabic_without_diacritics,
                word_in_arabic_with_diacritics,
            ]

        result += [
            word_pronunciation,
            word_meaning,
            word_declension,
            word_audio,
            word_part_of_speech,
            word_pattern,
            word_arabicfi_link,
        ]

        return result


def print_from_scraper(list):
    print("arabic without diacritics:            ", list[1])
    print("arabic with diacritics:               ", list[2])
    print("pronunciation:                        ", list[3])
    print("meaning:                              ", list[4])
    print("declension:                           ", list[5])
    print("audio link:                           ", list[6])
    print("part of speech:                       ", list[7])
    print("pattern:                              ", list[8])
    print("arabic.fi link:                       ", list[9])
