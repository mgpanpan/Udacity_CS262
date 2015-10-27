import re

url1 = "http://stackoverflow.com/"
url2 = "http://stackoverflow.com/questions/tagged/regex"

regexp1 = "(http|ftp)://([^/\r\n]+)([^\r\n]*)?"
print(re.match(regexp1, url1).groups())
print(re.match(regexp1, url2).groups())

regexp2 = "(?:http|ftp)://([^/\r\n]+)([^\r\n]*)?"
print(re.match(regexp2, url1).groups())
print(re.match(regexp2, url2).groups())
