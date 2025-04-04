class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, 'w')  # Open file in write mode
        print(f"File '{self.filename}' opened for writing.")

    def write_data(self, data):
        self.file.write(data + '\n')
        print(f"Data written to '{self.filename}'.")

    def __del__(self):
        self.file.close()  # Ensure file is closed when the object is deleted
        print(f"File '{self.filename}' closed.")

# Example usage
file_obj = FileHandler("sample.txt")
file_obj.write_data("Hello, this is a test.")

# Explicitly deleting the object (optional, as Python garbage collector will do it)
del file_obj
