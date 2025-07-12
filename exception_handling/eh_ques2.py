def read(document):
    try:
        with open(document) as file1:
            filecontent = file1.read()
            return filecontent
    except Exception as e:
        print("file not found")
        return None
read("myfile.txt")
        
    
    