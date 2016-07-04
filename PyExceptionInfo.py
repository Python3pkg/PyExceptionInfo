import webbrowser

def getInfo(e):
    url = getURL(e)
    webbrowser.open(url)

def makeURLQuery(e):
    url = "https://www.google.com/?gws_rd=ssl#q=python+"
    url += "+".join(str(e).split())
    return url

def getURL(e):
    return makeURLQuery(e)
