import scraper
import database_connector
import time


# word_322 = arabicfi_scraper.get_word_info(322)
# word_512 = arabicfi_scraper.get_word_info(512)


# for each in list:
#     print(each)

# word_23 = arabicfi_scraper.get_word_info(23)
# print(word_23)
# arabicfi_database.add_one_record(word_23)

# arabicfi_scraper.print_from_scraper(word_322)
# arabicfi_database.delete_record(23)
# arabicfi_database.delete_record(24)
# arabicfi_database.add_one_record(word_322)
# arabicfi_database.add_one_record(word_512)

# # get the start time
# st = time.time()

# list = []

# for number in range(2599, 3338):
#     print(f"Finding word number {number}")
#     if arabicfi_scraper.get_word_info(number):
#         print("Word found")
#         list.append(arabicfi_scraper.get_word_info(number))

# arabicfi_database.add_many_records(list)
# arabicfi_database.print_full_table_per_row()

# # get the end time
# et = time.time()

# # get the execution time
# elapsed_time = et - st
# print("Execution time:", elapsed_time, "seconds")

# For DEBUGGING
word = scraper.get_word_info(3338)
print(word)

# # Deleting everything
# for number in range(0, 151):
#     arabicfi_database.delete_record(number)
