import zipfile

with zipfile.ZipFile('datasets/example.zip') as myzip:
    all_file = myzip.namelist()
    print("all file")
    print(all_file)
    with myzip.open('example.txt') as myfile:
        content = myfile.read()
        print("content")
        print(content)

