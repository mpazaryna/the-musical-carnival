# importing the FileManager class from the file_manager module
from file_manager import FileManager

# create a new instance of the FileManager class with the "quote.txt" file name
file_manager = FileManager("quote.txt")

# write the Frankl quote to the "quote.txt" file
file_manager.write_to_file(
    """Ultimately, man should not ask what the meaning of his life is, but rather must recognize that it is he who is asked. In a word, each man is questioned by life; and he can only answer to life by answering for his own life; to life he can only respond by being responsible. — Victor Frankl"""
)

# read the content of the "quote.txt" file and print it to the console
file_manager.read_from_file()
