#!/usr/bin/env python

from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase
import yaml
import html
from html.parser import HTMLParser

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser("Convert yaml bibliography to bibtex bibliography")
    parser.add_argument("yaml", type=str, help="input yaml file")

    args = parser.parse_args()

    data = yaml.safe_load(open(args.yaml))

    htmlparser = HTMLParser()

    db = BibDatabase()

    entries = []
    for paper in data:
        authors = [ html.unescape(auth) for auth in paper["authors"] ]
        authors = [ u"S. M. Parker" if a=="me" else a for a in authors ]
        auth_str = u" and ".join(authors)

        firstauthor = authors[0].split()[-1]
        citekey = u"{author}{year}{journal}".format(author=firstauthor, year=paper.get("year", ""), journal=paper.get("journal",""))

        pap = { "ENTRYTYPE" : u"article", "ID" : citekey, "author" : auth_str }
        for key in [ "journal", "page", "title", "volume", "year", "note", "doi" ]:
            if key in paper:
                pap[key] = html.unescape(str(paper[key]))

        entries.append(pap)

    db.entries = entries


    writer = BibTexWriter()
    writer.indent = '  '
    writer.comma_first = True

    with open('smparker.bib', 'w') as bibfile:
        bibfile.write(writer.write(db))
