import sqlite3

connection = sqlite3.connect("arabicfi_words.db")
cursor = connection.cursor()

cursor.execute(
    """--sql
CREATE TABLE IF NOT EXISTS words (
    in_arabic text,
    in_arabic_wo_diacritics text,
    pronunciation text,
    meaning text,
    declension text,
    audio text,
    part_of_speech text,
    pattern text,
    arabicfi_link text
);"""
)

connection.commit()
connection.close()


def print_full_table_per_row():
    connection = sqlite3.connect("arabicfi_words.db")
    c = connection.cursor()

    c.execute("SELECT rowid, * FROM words")
    items = c.fetchall()

    for item in items:
        print(item)

    connection.commit()
    connection.close()


def add_one_record(word_info):
    connection = sqlite3.connect("arabicfi_words.db")
    c = connection.cursor()

    c.execute(
        "INSERT OR IGNORE INTO words(rowid,in_arabic,in_arabic_wo_diacritics,pronunciation,meaning,declension,audio,part_of_speech,pattern,arabicfi_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        word_info,
    )

    connection.commit()
    connection.close()


def add_many_records(list):
    connection = sqlite3.connect("arabicfi_words.db")
    c = connection.cursor()

    c.executemany(
        "INSERT OR IGNORE INTO words(rowid,in_arabic,in_arabic_wo_diacritics,pronunciation,meaning,declension,audio,part_of_speech,pattern,arabicfi_link) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (list),
    )

    connection.commit()
    connection.close()


# Deletes the records using rowid as String
def delete_record(id):
    connection = sqlite3.connect("arabicfi_words.db")
    c = connection.cursor()

    c.execute("DELETE FROM words WHERE rowid = (?)", (id,))

    connection.commit()
    connection.close()
