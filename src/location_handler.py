import sys

from urllib.request import urlopen, URLError
from urllib.parse import urlparse


def validate_web_url(url: str):
    # let's define a function to validate a url
    try:
        urlopen(url)
        return True
    except URLError as e:
        # on fail, we'll write to logs and exit
        error = "Web-scraper error at line 29... error reason is: {errreason}\n".format(
            errreason=e.reason)
        with open("./web-scraper-logs/error.txt", "a+") as error_file:

            error_file.write(error)

        sys.exit("invalid url passed! shutting down...")


def format_path(link: str):
    # let's parse the url and grab the path
    parsed_url = urlparse(link)
    file_path = parsed_url.path

    # let's check to see if there is a path, or if the path is a backslash and rename it index
    if file_path == "/" or not file_path:
        file_path = "index"

    # next we need to strip away any leading or trailing slashes
    if file_path[0] == "/":
        file_path = file_path[1:]

    if file_path[-1] == "/":
        file_path = file_path[:-1]

    # if there is a slash anywhere in the path, let's split the string by the slashes and take the final pathname
    if "/" in file_path:
        file_pathList = file_path.split("/")
        file_path = file_pathList[-1]

    return file_path
