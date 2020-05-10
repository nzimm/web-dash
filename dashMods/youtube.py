from dashMods import modules
import re

def youtube_link(url):
    """ Sanitize youtube link ()

        input: raw youtube links
        output: youtube-nocookie link
    """

    try:
        video_id = re.search(r"^http[s]?:\/\/www\.youtube.*\.com\/(watch\?v=|embed\/)(.+)$", url)[2]
        link = "https://www.youtube-nocookie.com/embed/" + video_id
    except TypeError:
        raise ValueError("Error could't parse youtube link: " + url)
    return(link)

class Youtube(modules.BaseModule):
    def __init__(self, pName, pDescription, pRequests):
        modules.BaseModule.__init__(self, pName, pDescription, pRequests)
        self.url = ''
        #self.name = pName
        #self.description = pDescription
        #self.parseRequest(pRequests)

    def parseRequest(self, request):
        if not "url" in request.form:
            exit
        try:
            self.url = youtube_link(request.form["url"])
        except:
            raise error("test")
