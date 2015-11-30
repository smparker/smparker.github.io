#!/usr/bin/env python

import yaml
import re

def pull_data(name):
    return yaml.load(open("_data/" + name + ".yml"))

# search-replace pairs to convert html special characters to latex
de_html_impl = [ ("--", re.compile(r"&ndash;")),
                 ("\\\"{a}", re.compile(r"&auml;")),
                 ("\\\"{o}", re.compile(r"&ouml;")),
                 ("\\\"{u}", re.compile(r"&uuml;")),
                 ("\\\"{A}", re.compile(r"&Auml;")),
                 ("\\\"{O}", re.compile(r"&Ouml;")),
                 ("\\\"{U}", re.compile(r"&Uuml;")) ]

def de_html(inp):
    out = str(inp)
    try:
        for dh in de_html_impl:
            out = dh[1].sub(dh[0], out)
    except:
        print out
    return out

def header(to_print = True):
    option = "print" if to_print else ""
    print r'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    print r'% Friggeri Resume/CV'
    print r'% XeLaTeX Template'
    print r'% Version 1.2 (3/5/15)'
    print r'%'
    print r'% This template has been downloaded from:'
    print r'% http://www.LaTeXTemplates.com'
    print r'%'
    print r'% Original author:'
    print r'% Adrien Friggeri (adrien@friggeri.net)'
    print r'% https://github.com/afriggeri/CV'
    print r'%'
    print r'% Edited by:'
    print r'% Shane Parker'
    print r'%'
    print r'% License:'
    print r'% CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)'
    print r'%'
    print r'% Important notes:'
    print r'% This template needs to be compiled with XeLaTeX and the bibliography, if used,'
    print r'% needs to be compiled with biber rather than bibtex.'
    print r'%'
    print r'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
    print r''
    print r'\documentclass[%s]{parker-cv}' % (option)
    print
    print r'\begin{document}'
    print
    print r'\header{Shane M.}{Parker}{}'
    print
    print r'%----------------------------------------------------------------------------------------'

def footer():
    print r'%----------------------------------------------------------------------------------------'
    print r'\end{document}'

def section_header(name, env = "entrylist"):
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print "%% %54s %%" % (name)
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"

    print "\\section{%s}" % (name)
    print ""
    print "\\begin{%s}" % (env)

def section_footer(env = "entrylist"):
    print "\end{%s}" % (env)
    print

if __name__ == "__main__":
    header()

    positions = pull_data("positions")
    section_header("positions")

    for p in positions:
        print "\\entry"
        print "{%s}" % (de_html(p["time"]))
        print "{%s}" % (de_html(p["title"]))
        print "{%s}" % (de_html(p["location"]))
        print "{"
        print "%s \\\\" % (de_html(p["institution"]))
        print "\emph{Advisor}: %s \\\\" % (de_html(p["advisor"]))
        print "\emph{Interest}: %s \\\\" % (de_html(p["interest"]))
        print "}"
        print

    section_footer()

    # papers are kind of special so will use a raw enumerate
    papers = pull_data("papers")
    section_header("publications", "enumerate")

    for i, pub in enumerate(papers):
        ir = len(papers) - i
        authors = de_html(", ".join([ "\\underline{S. M. Parker}" if x=="me" else x for x in pub["authors"] ]))
        journal = "\\textit{%s}" % (de_html(pub["journal"]))
        volume = "\\textbf{%s}" % (de_html(pub["volume"]))
        page = de_html(pub["page"])
        year = de_html(pub["year"])
        title = de_html(pub["title"])
        print "\\item[%d] %s \\\\" % (ir, authors)
        print "%s, %s, %s (%s) \\\\" % (journal, volume, page, year)
        print "\href{%s}{%s}" % (pub["url"], title)
        print

    section_footer("enumerate")

    awards = pull_data("awards")
    section_header("awards")

    for a in awards:
        print "\\entry"
        print "{%s}" % (de_html(a["year"]))
        print "{{\\normalfont %s}}" % (de_html(a["name"]))
        print "{}"
        print "{}"
        print

    section_footer()

    lectures = pull_data("lectures")
    section_header("lectures")

    for lec in lectures:
        print "\\entry"
        print "{%s}" % (de_html(lec["time"]))
        print "{%s}" % (de_html(lec["title"]))
        print "{%s}" % (de_html(lec["location"]))
        print "{"
        print "%s" % (de_html(lec["institution"]))
        print "}"
        print

    section_footer()

    posters = pull_data("posters")
    section_header("posters")

    for p in posters:
        print "\\entry"
        print "{%s}" % (de_html(p["time"]))
        print "{%s}" % (de_html(p["title"]))
        print "{%s}" % (de_html(p["location"]))
        print "{"
        print "%s \\\\" % (de_html(p["authors"]))
        print "presented at %s" % (de_html(p["event"]))
        print "}"
        print

    section_footer()

    teaching = pull_data("teaching")
    section_header("selected teaching")

    for t in teaching:
        print "\\entry"
        print "{%s}" % (de_html(t["time"]))
        print "{{\\normalfont %s for} %s}" % (de_html(t["role"]), de_html(t["title"]))
        print "{}"
        print "{"
        print "%s, %s \\\\" % (de_html(t["level"]), de_html(t["location"]))
        print "}"
        print

    section_footer()

    footer()
