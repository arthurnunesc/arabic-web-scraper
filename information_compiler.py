import arabicfi_scraper
import arabicfi_database

word_322 = arabicfi_scraper.get_word_info(322)
word_512 = arabicfi_scraper.get_word_info(512)

# arabicfi_scraper.print_from_scraper(word_322)
arabicfi_database.add_one_record(word_322)
arabicfi_database.add_one_record(word_512)

arabicfi_database.print_full_table_per_row()


list = []

# for number in range(0, 500):
#     list.append(arabicfi_scraper.get_word_info(number))
