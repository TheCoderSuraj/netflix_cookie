import os
class CookieRead:
    def fetch_cookie( path):
        try:
            with open(path) as f:
                # print(f.read())
                return f.read()
        except:
            print("We got error on reading file")

        return None

    def getFilePathList( dirPath):
        try:
            return os.listdir(dirPath)
        except:
            print("Unexpected Error")
        return []

    # fetch_cookie('text/txt.txt')
    # getListPaths('data2')