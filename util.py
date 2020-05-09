#
# util functions for web dash
#

import re

def youtube_link(url):
    """ Sanitize youtube link (prob missed some formats)

        input:  raw youtube link
        output: youtube-nocookie link
    """
    try:
        video_id = re.search(r"^http[s]?:\/\/www\.youtube.*\.com\/(watch\?v=|embed\/)(.+)$", url)[2]
        link = "https://www.youtube-nocookie.com/embed/" + video_id
    except TypeError:
        raise ValueError("Error: couldn't parse youtube link: " + url)
    return(link)
