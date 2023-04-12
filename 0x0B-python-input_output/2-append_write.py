def append_write(filename="", text=""):
  """appends text at the beginning of an existing file
  creates the file and writes the text if file does not exist
  returns the number of characters added to the file"""
    with open(filename, mode = "a", encoding="utf-8") as file:
        characters = file.write(text)
        return (characters)
