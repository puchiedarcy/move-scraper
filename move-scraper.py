import urllib
from lxml import html

url = 'http://bulbapedia.bulbagarden.net/wiki/Durant_(Pok%C3%A9mon)'
response = urllib.urlopen(url)
data = response.read()
tree = html.fromstring(data)

learn_by_level_up = tree.xpath('//span[@id="By_leveling_up"]/../following-sibling::table[1]/tr[2]/td[1]/table[1]/tr/td[2]/a/span/text()')

print learn_by_level_up
