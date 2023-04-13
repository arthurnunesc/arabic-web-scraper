# arabicfi-scraper

Python web-scraper written for the [Arabic.fi](https://arabic.fi/) website. It fetches and compiles the details of Arabic words provided by the website.

## Information fetched

- Word in arabic script without diacritics
- Word in arabic script with diacricts
- Pronunciation(Romanized)
- Meaning
- Declension
- Pronunciation audio(As a link)
- Part of speech
- Pattern
- Word link(ex: https://arabic.fi/words/3559)

## Features and caveats

- It also stores the inverted words in arabic, as not all terminals support RTL text.
- Because its main purpose was to compile the information to make the flashcards and not to show them in the terminal, most terminals will not show the words in the Arabic script properly even when using the inverted variable. The way I made them get displayed as they should on my terminal was using Gnome Terminal and an Monospace font that support Arabic characters(Ex: Kawkab Mono, DejaVu Sans Mono, Thabit, Courier New). It should also be noted that I am not using BiDi/BiCon as that may alter your results.

## Libraries used

- BeautifulSoup4
  - Used to fetch all the information from the page's HTML.
- Bidi Algorithm
  - Changes string encoding to UTF-8, inverting the text as needed.
- PyArabic
  - Used to strip diacritics from the arabic words.
- SQLite3
  - Used to store the data fetched.


## To-do

- Add word conjugations fetch
- Add context sentence fetch
- Add context meaning fetch
- Add context audio fetch
- Add image to match with words
