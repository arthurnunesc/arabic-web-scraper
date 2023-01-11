# anki-web-scraper

Python web-scraper written for the [Arabic.fi](https://arabic.fi/) website. It fetches information from words through the [random word link](https://arabic.fi/random-word) provided by the website.

## Information fetched

- Word in arabic script without diacritics
- Word in arabic script with diacricts
- Pronunciation(Romanized)
- Meaning
- Declension
- Pronunciation audio example(As a link)
- Part of speech
- Pattern
- Word link(ex: https://arabic.fi/words/3559)

## Features and caveats

- It also stores the inverted words in arabic, as not all terminals support RTL text.
- Because its main purpose was to compile the information to make the flashcards and not to show them in the terminal, most terminals will not show the words in the arabic script properly even when using the UTF-8 variable. The way I made them show up as they should on my terminal was using Gnome Terminal and the Kawkab Mono font. It should also be noted that I do not having BiDi installed in my terminal as that may alter your results.

## Libraries used

- BeautifulSoup4
  - Used to fetch all the information from the page's HTML.
- Bidi Algorithm
  - Changes string encoding to UTF-8, inverting the text as needed.
- PyArabic
  - Used to strip diacritics from the arabic words.
  

## To-do

- Add context sentence fetch
- Add context meaning fetch
- Add context audio fetch
- Add image to match with words
