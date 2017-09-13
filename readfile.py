import urllib

def read_file():
    f = open(r"C:\Users\ramesh\Downloads\movie_quotes.txt")
    c = f.read()
    print(c)
    f.close()
def read_url():
    u = urllib.urlopen("http://www.wdyl.com/profanity?q=shot")
    c = u.read()
    print (c)
    u.close()
read_file()
read_url()
