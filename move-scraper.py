import urllib
from lxml import html

pokemon = ['Mew', 'Skitty', 'Durant', 'Lapras', 'Rhyhorn']

def get_moves(name, move_name_index = 2):
    url = 'http://bulbapedia.bulbagarden.net/wiki/{}_(Pok%C3%A9mon)'.format(name)
    response = urllib.urlopen(url)
    data = response.read()
    tree = html.fromstring(data)

    learn_by_level_up = tree.xpath('//span[@id="By_leveling_up"]/../following-sibling::table[1]/tr[2]/td[1]/table[1]/tr/td[{}]/a/span/text()'.format(move_name_index))
    return learn_by_level_up



for i in pokemon:

    moves = get_moves(i)
    if len(moves) == 0:
        moves = get_moves(i, 3)

    print moves
~                  