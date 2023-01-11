from bs4 import BeautifulSoup
import requests
import arabic_reshaper
from bidi.algorithm import get_display
import pyarabic.araby as araby


def formatArabicSentences(sentences):
   return sentences

url_word = 'https://arabic.fi/words/322'
url_verb = 'https://arabic.fi/words/1027'
url_random = 'https://arabic.fi/random-word'

resp = requests.get(url_word)
soup = BeautifulSoup(resp.text, 'html.parser')

word = soup.select_one("div.word-arabic.arabic.arabic-large").get_text()
word_pronunciation = soup.select_one("div.word-phonetic.phonetic").get_text()

word_in_arabic_with_diacritics = word
word_in_arabic_without_diacritics = araby.strip_diacritics(word)
word_in_arabic_with_diacritics_inverted = get_display(word)
word_in_arabic_without_diacritics_inverted = arabic_reshaper.reshape(get_display((word_in_arabic_without_diacritics)))

# LEGACY CODE LMAO
# word = soup.find("div", class_="word").find("p").find_all("span")

# if str(soup.find("p"))[33:37] == "verb":
#    word_in_arabic_without_diacritics = formatArabicSentences(word[0].string)
#    word_in_arabic_with_diacritics = word[0].string [::-1]
#    word_in_arabic_with_diacritics_inverted = word[0].string
#    word_in_arabic_without_diacritics_inverted = araby.strip_diacritics(word[0].string)
#    word_pronunciation = word[1].string
# elif str(soup.find("p"))[14:18] == "word":
#    word_in_arabic_without_diacritics = formatArabicSentences(word[1].string)
#    word_in_arabic_with_diacritics = word[1].string [::-1]
#    word_in_arabic_with_diacritics_inverted = word[1].string
#    word_in_arabic_without_diacritics_inverted = araby.strip_diacritics(word[1].string)
#    word_pronunciation = word[0].string 

# Fetches word meaning and declension and separates them in two variables
word_meaning_and_declension = soup.select_one("div.word-declension-info-text").small.get_text()
word_meaning_and_declension = word_meaning_and_declension.split(" – ")
word_meaning = word_meaning_and_declension[0]
word_declension = word_meaning_and_declension[1]

# Check if there is an audio for the word, if not assigns "no word audio" to its variable
if soup.find("div", class_="word-sound") != None:
   word_audio = soup.find("div", class_="word-sound").find("amp-audio")['src']
else:
   word_audio = "no word audio"

# LEGACY CODE LMAO
# if "Part of speech: " in str(soup.find("div", class_="relation")):
#    word_part_of_speech_and_pattern = soup.find("div", class_="relation").find("div")
# elif "Part of speech: " in str(soup.find("div", class_="relation").next_sibling):
#    word_part_of_speech_and_pattern = soup.find("div", class_="relation").next_sibling.find("div")

# Fetches word part of speech and pattern
word_part_of_speech_and_pattern = soup.select_one("div.similar-info")
print(word_part_of_speech_and_pattern)
# Parses part of speech from the variable containing it and the pattern
word_part_of_speech = word_part_of_speech_and_pattern.get_text().split(". ")
word_part_of_speech = word_part_of_speech[0].split(": ")
word_part_of_speech = word_part_of_speech[1]
print(word_part_of_speech)

# Checks if word pattern was fetched, if not, assigns "no pattern" to its variable
if "Pattern: " in  str(word_part_of_speech_and_pattern):
   word_pattern = word_part_of_speech_and_pattern.select_one("a").get_text()
else:
   word_pattern = "no pattern"

print(word_pattern)

# Gets word link
word_arabicfi_link = soup.find("link")["href"]

# word_conjugations

# Checks if the word has a context sentence
if "Using the word" in str(soup.find("h2")):
   has_context_sentence = True
else:
   has_context_sentence = False

# context_meanings

# context_audios

# image

# Printing everything on the terminal
# print("arabic without diacritics:            ", word_in_arabic_without_diacritics)
# print("arabic with diacritics:               ", word_in_arabic_with_diacritics)
# print("arabic without diacritics(inverted):  ", word_in_arabic_without_diacritics_inverted)
# print("arabic with diacritics(inverted):     ", word_in_arabic_with_diacritics_inverted)
# print("pronunciation:                        ", word_pronunciation)
# print("meaning:                              ", word_meaning)
# print("declension:                           ", word_declension)
# print("audio link:                           ", word_audio)
# print("part of speech:                       ", word_part_of_speech)
# print("pattern:                              ", word_pattern)
# print("arabic.fi link:                       ", word_arabicfi_link)