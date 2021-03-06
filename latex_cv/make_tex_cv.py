#!/usr/bin/env python

from __future__ import print_function

import yaml
import re

SIMPLE = False

def pull_data(name):
    return yaml.load(open("../_data/" + name + ".yml"))

# search-replace pairs to convert html special characters to latex
de_html_impl = [ ("--", re.compile(r"&ndash;")),
                 ("\\\&", re.compile(r"&amp;")),
                 ("\\\"{a}", re.compile(r"&auml;")),
                 ("\\\"{o}", re.compile(r"&ouml;")),
                 ("\\\"{u}", re.compile(r"&uuml;")),
                 ("\\\"{A}", re.compile(r"&Auml;")),
                 ("\\\"{O}", re.compile(r"&Ouml;")),
                 ("\\\"{U}", re.compile(r"&Uuml;")),
                 ("\\\'{a}", re.compile(r"&aacute;")),
                 ("\\\'{e}", re.compile(r"&eacute;")),
                 ("\\\'{o}", re.compile(r"&oacute;")),
                 ("\\\'{A}", re.compile(r"&Aacute;")),
                 ("\\\'{E}", re.compile(r"&Eacute;")),
                 ("\\\'{O}", re.compile(r"&Oacute;")),
                 ("$_{\\\\text{", re.compile(r"<sub>")),
                 ("}}$", re.compile(r"<\/sub>")) ]

def de_html(inp):
    out = str(inp)
    try:
        for dh in de_html_impl:
            out = dh[1].sub(dh[0], out)
    except:
        print(out)
    return out

def header(style, to_print = True):
    opts = [ style ]
    if to_print: opts.append("print")
    options = ",".join(opts)
    print(r'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(r'% Friggeri Resume/CV')
    print(r'% XeLaTeX Template')
    print(r'% Version 1.2 (3/5/15)')
    print(r'%')
    print(r'% This template has been downloaded from:')
    print(r'% http://www.LaTeXTemplates.com')
    print(r'%')
    print(r'% Original author:')
    print(r'% Adrien Friggeri (adrien@friggeri.net)')
    print(r'% https://github.com/afriggeri/CV')
    print(r'%')
    print(r'% Edited by:')
    print(r'% Shane Parker')
    print(r'%')
    print(r'% License:')
    print(r'% CC BY-NC-SA 3.0 (http://creativecommons.org/licenses/by-nc-sa/3.0/)')
    print(r'%')
    print(r'% Important notes:')
    print(r'% This template needs to be compiled with XeLaTeX and the bibliography, if used,')
    print(r'% needs to be compiled with biber rather than bibtex.')
    print(r'%')
    print(r'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print(r'')
    print(r'\documentclass[%s]{parker-cv}' % (options))
    print()
    print(r'\renewcommand{\normalsize}{\fontsize{10}{12}\selectfont}')
    print(r'\renewcommand{\LARGE}{\fontsize{14}{16}\selectfont}')
    print()
    print(r'\begin{document}')
    print()
    print(r'\header{Shane M.}{Parker}{shane.parker@case.edu}{quantumparker.com}{(216) 368-3697}')
    print()
    print(r'%----------------------------------------------------------------------------------------')

def aside():
    print(r'\begin{aside}')
    print(r'\section{programming}')
    for lang in ['C/C++', 'Fortran', 'Python', 'bash']:
        print(r'%s' % (lang))

    print(r'\section{languages}')
    for lang in ['English (native)', 'German (conversational)']:
        print(r'%s' % (lang))
    print(r'\end{aside}')

def footer():
    print(r'%----------------------------------------------------------------------------------------')
    print(r'\end{document}')

def section_header(name, env = "entrylist"):
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print("%% %54s %%" % (name))
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")

    print("\\section{%s}" % (name))
    print("")
    print("\\begin{%s}" % (env))

def section_footer(env = "entrylist"):
    print("\end{%s}" % (env))
    print()

def positions():
    pos = pull_data("positions")
    section_header("positions")

    for p in pos:
        time = de_html(p["time"])
        title = de_html(p["title"])
        location = de_html(p["location"])
        institution = de_html(p["institution"])
        advisor = de_html(p["advisor"]) if "advisor" in p else None
        interest = de_html(p["interest"]) if "interest" in p else None
        if not SIMPLE: print("\\entry")
        print("{%s}" % (time))
        print("{%s}" % (title))
        print("{%s}" % (location))
        print("{")
        print("%s \\\\" % (institution))
        if advisor:
            print("\emph{Advisor}: %s \\\\" % (advisor))
        #if interest:
        #    print("\emph{Interest}: %s \\\\" % (interest))
        print("}")
        print()

    section_footer()

def papers():
    # papers are kind of special so will use a raw enumerate
    pubs = pull_data("papers")
    section_header("publications", "enumerate")
    smp = "\\underline{S. M. Parker}" if not SIMPLE else "S. M. Parker"

    for i, pub in enumerate(pubs):
        ir = len(pubs) - i
        authors = de_html(", ".join(
            [smp if x=="me" else x for x in pub["authors"]
        ]))
        has_notes = "note" in pub

        journal = de_html(pub.get("journal",""))
        if journal:
            journal = "\\textit{%s}" % (journal)
        year = "(%s)" % de_html(pub["year"])
        title = de_html(pub["title"])
        url = pub.get("url","")
        if not url and "doi" in pub:
            url = "https://dx.doi.org/{}".format(pub["doi"])
        if url and not SIMPLE:
            title = "\href{%s}{%s}" % (url, title)

        if not has_notes:
            volume = "\\textbf{%s}" % (de_html(pub["volume"]))
            page = de_html(pub["page"])
            print("\\item[%d] %s \\\\" % (ir, authors))
            jvpy = ", ".join(filter(None, [journal, volume, page])) + " " + year
            print("%s \\\\" % (jvpy))
            print(title)
            if url and SIMPLE:
                print(url)
            print()
        else:
            notes = de_html(pub["note"])
            print("\\item[---] %s \\\\" % (authors))
            jyn = ", ".join(filter(None, [ journal, year, notes ]))
            print("%s \\\\" % (jyn))
            print(title)
            if url and SIMPLE:
                print(url)
            print()

    section_footer("enumerate")

    print("\\vspace{0.25cm}")

def chapters():
    # chapters are modeled off of papers
    pubs = pull_data("chapters")
    section_header("book chapters", "enumerate")

    for i, pub in enumerate(pubs):
        ir = len(pubs) - i
        authors = de_html(", ".join(
            ["\\underline{S. M. Parker}" if x=="me" else x for x in pub["authors"]
        ]))
        has_notes = "note" in pub

        book = de_html(pub["book"])
        if book:
            book = "\\textit{%s}" % book
        editor = de_html(pub["editor"])
        if editor:
            editor = "edited by %s" % editor
        publisher = de_html(pub["publisher"])
        year = "(%s)" % de_html(pub["year"])
        title = de_html(pub["title"])
        url = pub.get("url","")
        if url:
            title = "\href{%s}{%s}" % (url, title)

        print("\\item[%d] %s \\\\" % (ir, authors))
        bepy = ", ".join(filter(None, [book, editor, publisher])) + " " + year
        print("%s \\\\" % (bepy))
        print(title)
        print()

    section_footer("enumerate")

    print("\\vspace{0.25cm}")

def media():
    media = pull_data("media")
    section_header("reports in media and professional journals")

    for rep in media:
        des = de_html(rep["description"])
        year = de_html(rep["year"])
        name = de_html(rep["name"])
        url = de_html(rep.get("url", ""))

        if not SIMPLE: print("\\entry")
        print("{%s}" % year)
        if url == "":
            print("{%s} {\\normalfont %s}" % (name, des))
        else:
            print("{\href{%s}{%s}} {\\normalfont %s}" % (url, name, des))
        print("{}")
        print("{}")
        print()

    section_footer()

def awards():
    award = pull_data("awards")
    section_header("awards")

    for a in award:
        des = de_html(a.get("description", ""))
        name = de_html(a["name"])
        year = de_html(a["year"])
        if not SIMPLE: print("\\entry")
        print("{%s}" % (year))
        print("{%s {\\normalfont %s}}" % (name, des))
        print("{}")
        print("{}")
        print()

    section_footer()

def lectures():
    lect = pull_data("lectures")
    section_header("invited lectures")

    for l in lect:
        time = de_html(l["time"])
        title = de_html(l["title"])
        location = de_html(l["location"])
        institution = de_html(l["institution"])
        invited = l["invited"]
        if not invited:
            continue
        #if invited:
        #    title += r" \textit{(invited)}"
        if not SIMPLE: print("\\entry")
        print("{%s}" % (time))
        print("{%s}" % (title))
        print("{%s}" % (location))
        print("{")
        print("%s" % (institution))
        print("}")
        print()

    section_footer()

def pedagogy():
    lect = pull_data("pedagogy")
    section_header("pedagogical lectures")

    for l in lect:
        time = de_html(l["time"])
        topic = de_html(l["topic"])
        location = de_html(l["location"])
        institution = de_html(l["institution"])
        if not SIMPLE: print("\\entry")
        print("{%s}" % (time))
        print("{%s}" % (topic))
        print("{%s}" % (location))
        print("{")
        print("%s" % (institution))
        print("}")
        print()

    section_footer()

def posters():
    post = pull_data("posters")
    section_header("posters")

    for p in post:
        time = de_html(p["time"])
        title = de_html(p["title"])
        location = de_html(p["location"])
        authors = de_html(p["authors"])
        event = de_html(p["event"])
        if not SIMPLE: print("\\entry")
        print("{%s}" % (time))
        print("{%s}" % (title))
        print("{%s}" % (location))
        print("{")
        print("%s \\\\" % (authors))
        print("presented at %s" % (event))
        print("}")
        print()

    section_footer()

def teaching():
    teach = pull_data("teaching")
    section_header("select teaching")

    for t in teach:
        time = de_html(t["time"])
        title = de_html(t["title"])
        role = de_html(t["role"])
        code = de_html(t.get("code", ""))
        level = de_html(t["level"])
        location = de_html(t["location"])
        if not SIMPLE: print("\\entry")
        print("{%s}" % (time))
        print("{%s}" % (title))
        print("{%s, %s}" % (level, location))
        print("{}")
        print()

    section_footer()

def make_tex(style, printcolors):
    header(style, printcolors)
    if (style == "resume"):
        aside()
    positions()
    papers()
    chapters()
    media()
    awards()
    lectures()
    pedagogy()
    #posters()
    teaching()
    footer()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Script to auto-generate a CV or a Resume from collected yaml files")
    parser.add_argument("-t", "--type", type=str, dest="style", choices=("cv", "resume"), default="cv")
    parser.add_argument("-p", "--print", dest="printcolors", action="store_true")
    parser.add_argument("--simple", "-s", dest="simple", action="store_true")

    args = parser.parse_args()

    style = args.style
    printcolors = args.printcolors
    SIMPLE = args.simple

    make_tex(style, printcolors)
