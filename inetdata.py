import urllib2

def main():
    webUrl = urllib2.urlopen("https://sumshchenko.gq")

    print "resul code: " + str(webUrl.getcode())

    data = webUrl.read()
    print data

if __name__ == "__main__":
    main()