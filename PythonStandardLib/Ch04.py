# Datetime module
from datetime import datetime, timedelta
from html.parser import HTMLParser

now = datetime.now()

print(now.date())

# Formating dates and times
print(now.strftime("%a %A %d"))
print(now.strftime("%b %B %m"))

print(now.strftime("%H : %M : %S %p"))

testDate =  now +timedelta(days=2)
print(testDate.date())

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str]]) :
        print("Start tag: ", tag)
        for attr in attrs:
            print("Attribute: ", attr)
    def handle_endtag(self, tag: str) -> None:
        print("End tag: ", tag)
    def handle_comment(self, data: str) -> None:
        print("Comment: ", data)
    def handle_data(self, data: str) -> None:
       print("Data: ", data)

parser_html = HTMLParser()

parser_html.feed("""<html lang="en">
<head>
    <meta charset="utf-8">
    <title>My Lovely Family</title>
    <link rel="stylesheet" href="styles/about.css">
    <script src="scripts/test.js"></script>
</head>
<body>
    <div>
        <h1>
            My son and my wife!
        </h1>
    </div>
    <img src="images/Screenshot2022-06-07225256.jpg"/>
</body>
</html>""")

print()