from random import betavariate
from time import clock_settime
from bs4 import BeautifulSoup
import requests
import os
import sys
import arabic_reshaper
from bidi.algorithm import get_display
import pyarabic.araby as araby


def formatArabicSentences(sentences):
   formatedSentences = arabic_reshaper.reshape(sentences)
   return get_display(formatedSentences)

url_word = 'https://arabic.fi/words/322'
url_verb = 'https://arabic.fi/words/1027'
url_random = 'https://arabic.fi/random-word'

result = requests.get(url_random)

soup = BeautifulSoup(result.text, 'html.parser')

soup.find_all("div", class_="quote")

word = soup.find("div", class_="word").find("p").find_all("span")

# if verb
if str(soup.find("p"))[33:37] == "verb":
   word_in_arabic_without_diacritics = formatArabicSentences(word[0].string)
   word_in_arabic_with_diacritics = word[0].string [::-1]
   word_in_arabic_with_diacritics_utf8 = word[0].string
   word_in_arabic_without_diacritics_utf8 = araby.strip_diacritics(word[0].string)
   word_pronunciation = word[1].string
# if word
elif str(soup.find("p"))[14:18] == "word":
   word_in_arabic_without_diacritics = formatArabicSentences(word[1].string)
   word_in_arabic_with_diacritics = word[1].string [::-1]
   word_in_arabic_with_diacritics_utf8 = word[1].string
   word_in_arabic_without_diacritics_utf8 = araby.strip_diacritics(word[1].string)
   word_pronunciation = word[0].string 

print("")
# print("arabic without diacritics:         ", word_in_arabic_without_diacritics)
# print("arabic with diacritics:            ", word_in_arabic_with_diacritics)
print("arabic with diacritics(utf-8):     ", word_in_arabic_with_diacritics_utf8)
print("arabic without diacritics(utf-8):  ", word_in_arabic_without_diacritics_utf8)
print("pronunciation:                     ", word_pronunciation)


word_meaning_and_declension = soup.find("div", class_="word-declension-info-text").find("small").string
word_meaning_and_declension = word_meaning_and_declension.split(" – ")
word_meaning = word_meaning_and_declension[0]
word_declension = word_meaning_and_declension[1]

print("meaning:                           ", word_meaning)
print("declension:                        ", word_declension)


if soup.find("div", class_="word-sound") != None:
   word_audio = soup.find("div", class_="word-sound").find("amp-audio")['src']
else:
   word_audio = "no word audio"

print("audio link:                        ", word_audio)


if "Part of speech: " in str(soup.find("div", class_="relation")):
   word_part_of_speech_and_pattern = soup.find("div", class_="relation").find("div")
elif "Part of speech: " in str(soup.find("div", class_="relation").next_sibling):
   word_part_of_speech_and_pattern = soup.find("div", class_="relation").next_sibling.find("div")

word_part_of_speech = word_part_of_speech_and_pattern.contents[0]
word_part_of_speech = word_part_of_speech.split(". ")
word_part_of_speech = word_part_of_speech[0].split(": ")
word_part_of_speech = word_part_of_speech[1]

if "Pattern: " in  str(word_part_of_speech_and_pattern):
   word_pattern = word_part_of_speech_and_pattern.find("a").contents[0]
else:
   word_pattern = "no pattern"

print("part of speech:                    ", word_part_of_speech)
print("pattern:                           ", word_pattern)


# word_conjugations

word_arabicfi_link = soup.find("link")["href"]

print("arabic.fi link:                    ", word_arabicfi_link)
print("")

if "Using the word" in str(soup.find("h2")):
   has_context_sentence = True
else:
   has_context_sentence = False


# context_sentences
# context_meanings
# context_audios
# image
