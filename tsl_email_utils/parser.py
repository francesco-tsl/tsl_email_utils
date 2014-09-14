__doc__ = """
contact request parser
written by Francesco Pischedda <francesco@pischedda.info>

LICENSE
===
See README.txt for license details
"""
import re
from collections import defaultdict


def parse(text):

    contact = defaultdict(str)
    if text == '':
        return contact

    # first match group excludes characters : and new line so it caches
    # all text before the FIRST character : this way the second group can
    # contain the character :
    r = re.compile("^([^\n:]+): (.+)", re.M)

    matches = r.finditer(text)
    for m in matches:
        contact[m.group(1).lower()] = m.group(2)

    if 'email' in contact:
        contact['email'] = contact['email'].replace("<", "").replace(">", "")
    else:
        contact['email'] = ''

    try:
        details = text[text.rindex("Ulteriori Dettagli: "):]
    except ValueError:
        details = ''

    contact['details'] = details

    if 'nome della compagnia' not in contact:
        contact['nome della compagnia'] = ''

    return contact
