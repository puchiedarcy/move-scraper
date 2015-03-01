import urllib
from lxml import html
import MySQLdb

con = MySQLdb.connect('localhost', 'root', 'root', 'pokemon')

cur = con.cursor()
cur.execute("SELECT name FROM pokemon;")
rows = cur.fetchall()

pokemon = [ row[0] for row in rows ]

def get_moves(name, move_name_index = 2):
    url = 'http://bulbapedia.bulbagarden.net/wiki/{}_(Pok%C3%A9mon)'.format(name)
    response = urllib.urlopen(url)
    data = response.read()
    tree = html.fromstring(data)

    learn_by_level_up = tree.xpath('//span[@id="By_leveling_up"]/../following-sibling::table[1]/tr[2]/td[1]/table[1]/tr/td[{}]/a/span/text()'.format(move_name_index))
    return learn_by_level_up



for name in pokemon:

    moves = get_moves(name)
    if len(moves) == 0:
        moves = get_moves(name, 3)

    cur = con.cursor()
    for move in moves:
        print move
        cur.execute("INSERT INTO moves (name) VALUES (%s);", (move))
        cur.execute("INSERT INTO learnset (pokemon, move) VALUES (%s, %s);", (name, move))
        con.commit()

con.close()