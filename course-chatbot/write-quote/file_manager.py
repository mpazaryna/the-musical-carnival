"""
file_manager.py

This module contains a simple file manager for reading and writing files.

Classes:
- FileManager

"""


class FileManager:
  """
    A simple file manager for reading and writing files.

    Attributes:
    - filename (str): The name of the file to read from or write to.

    """

  def __init__(self, filename):
    """
        Create a new FileManager object with the specified filename.

        Parameters:
        - filename (str): The name of the file to read from or write to.

        """
    self.filename = filename

  def write_to_file(self, content):
    """
        Write the specified content to the file.

        Parameters:
        - content (str): The string to write to the file.

        """
    # Open the file for writing
    with open(self.filename, "w") as file:
      # Write the string to the file
      file.write(content)

  def read_from_file(self):
    """
        Read the content of the file and print it to the console.

        """
    # Open the file for reading
    with open(self.filename, "r") as file:
      # Read the content of the file
      content = file.read()
      # Print the content to the console
      print(content)
