class FileReader:
    def __init__(self, data):
        self.data = data

    def read(self):
        try:
            with open(self.data, 'r') as f:
                return f.read() 
        except OSError:
            return ""

if __name__ == "__main__":
    reader = FileReader(data)
    print(reader.read())
