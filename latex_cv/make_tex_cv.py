#!/usr/bin/env python

from __future__ import print_function

import yaml
import re
import datetime

SIMPLE = False
SPLIT_AT_CWRU = False
CWRU_PAPERS = 11
CWRU_CHAPTERS = 0
SHOW_CORRESPONDING = True

def pull_data(name):
    return yaml.safe_load(open("../_data/" + name + ".yml"))

# search-replace pairs to convert html special characters to latex
de_html_impl = [ ("--", re.compile(r"&ndash;")),
                 ("\\\&", re.compile(r"&amp;")),
                 ("\\%", re.compile(r"%")),
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
                 ("\\$", re.compile(r"\$")),
                 ("$_{\\\\text{", re.compile(r"<sub>")),
                 ("}}$", re.compile(r"<\/sub>")) ]

def print_date(date):
    return date.strftime("%B %d, %Y")
prepared = datetime.date.today()

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
    print(r'\usepackage{enumitem}')
    print(r'\usepackage{fancyhdr}')
    print(r'\usepackage{lastpage}')
    print(r'\renewcommand{\headrulewidth}{0pt}')
    print()
    print(r'\pagestyle{fancy}')
    print(r'\fancyhf{}')
    print()
    print(r'\rfoot{Page \thepage \hspace{1pt} of \pageref{LastPage}}')
    print()
    print(r'\begin{document}')
    print()
    print(r'\header{Shane M.}{Parker}{shane.parker@case.edu}{quantumparker.com}{(216) 368-3697}{%s}' % (print_date(prepared)))
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
        if not SIMPLE: print("\\entry[-0.5em]")
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

def memberships():
    mem = pull_data("memberships")

    print(r"\section{professional affiliations}")
    print(r"\begin{itemize}[noitemsep]")
    for m in mem:
        print(r"\item %s" % (de_html(m)))
    print(r"\end{itemize}")

def papers():
    # papers are kind of special so will use a raw enumerate
    pubs = pull_data("papers")
    print(r"\section{publications}")

    smp = "\\underline{S. M. Parker}" if not SIMPLE else "S. M. Parker"

    if SHOW_CORRESPONDING:
        print("corresponding authorship denoted with $^*$")

    def print_paper(i, pub):
        ir = len(pubs) - i
        smp_co = smp
        if pub.get("corresponding", False):
            smp_co = smp + "$^*$" if SHOW_CORRESPONDING else smp
        authors = ", ".join(
            [smp_co if x=="S. M. Parker" else de_html(x) for x in pub["authors"]
        ])
        has_notes = "note" in pub

        journal = de_html(pub.get("journal",""))
        journal_str = "\\textit{%s}" % (journal) if journal else ""
        year = de_html(pub["year"])
        year_str = f"\\textbf{{{year}}}"
        title_str = de_html(pub["title"])
        url = pub.get("url","")
        if not url and "doi" in pub:
            url = "https://dx.doi.org/{}".format(pub["doi"])
        if url and not SIMPLE:
            title_str = "\href{%s}{%s}" % (url, title_str)

        gets_index = (not has_notes) or (has_notes and pub["note"] == "in print")
        index_str = f"{ir:d}" if gets_index else "---"

        print("\\item[%s] %s, \\\\" % (index_str, authors))
        print(f"{title_str:s}, ")
        if url and SIMPLE:
            print(url)

        volume = de_html(pub.get("volume", ""))
        volume_str = f"\\textit{{{volume}}}" if volume else ""
        page_str = de_html(pub.get("page", ""))
        if journal_str:
            print(f"{journal_str}")
        print(f"{year_str}", end="")

        vp_list = list(filter(None, [volume_str, page_str]))
        #print("vp_list: ", vp_list)
        if vp_list:
            vp = ", ".join(vp_list)
            print(f", {vp}", end="")

        if has_notes:
            notes = de_html(pub["note"])
            print(f", {notes:s}", end="")

        if "preprint" in pub:
            preprint = de_html(pub["preprint"])
            preprint_url = pub.get("preprint_url", "")
            if preprint_url:
                preprint = "\href{%s}{%s}" % (preprint_url, preprint)
            print(f", {preprint:s}")

        print()

    if SPLIT_AT_CWRU:
        print()
        print(r"\subsection{Case Western Reserve University}")
        print(r"\begin{enumerate}")
        for i, pub in enumerate(pubs[:CWRU_PAPERS]):
            print_paper(i, pub)
        print(r"\end{enumerate}")

        print(r"\subsection{Before Case Western Reserve University}")
        print(r"\begin{enumerate}")
        for j, pub in enumerate(pubs[CWRU_PAPERS:]):
            i = j + CWRU_PAPERS
            print_paper(i, pub)
        print(r"\end{enumerate}")
    else:
        print(r"\begin{enumerate}")
        for i, pub in enumerate(pubs):
            print_paper(i, pub)
        print(r"\end{enumerate}")

    print("\\vspace{0.25cm}")

def chapters():
    # chapters are modeled off of papers
    pubs = pull_data("chapters")
    print(r"\section{book chapters}")

    def print_book(i, pub):
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

    if SPLIT_AT_CWRU:
        if CWRU_CHAPTERS > 0:
            print()
            print(r"\subsection{Case Western Reserve University}")
            print(r"\begin{enumerate}")
            for i, pub in enumerate(pubs[:CWRU_CHAPTERS]):
                print_book(i, pub)
            print(r"\end{enumerate}")

        print()
        print(r"\subsection{Before Case Western Reserve University}")
        print(r"\begin{enumerate}")
        for j, pub in enumerate(pubs[CWRU_CHAPTERS:]):
            i = j + CWRU_CHAPTERS
            print_book(i, pub)
        print(r"\end{enumerate}")
    else:
        print(r"\begin{enumerate}")
        for i, pub in enumerate(pubs):
            print_book(i, pub)
        print(r"\end{enumerate}")

    print("\\vspace{0.25cm}")

def media():
    media = pull_data("media")
    section_header("reports in media and professional journals")
    print()

    for rep in media:
        des = de_html(rep["description"])
        year = de_html(rep["year"])
        name = de_html(rep["name"])
        url = de_html(rep.get("url", ""))

        if not SIMPLE: print("\\entry[-1em]")
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
        if not SIMPLE: print("\\entry[-1em]")
        print("{%s}" % (year))
        print("{%s {\\normalfont %s}}" % (name, des))
        print("{}")
        print("{}")
        print()

    section_footer()

def student_awards():
    awards = pull_data("student_awards")
    section_header("student awards")

    for a in awards:
        student = de_html(a["student"])
        award = de_html(a["award"])
        des = de_html(a.get("description", ""))
        year = de_html(a["year"])
        if not SIMPLE: print("\\entry[-1em]")
        print("{%s}" % (year))
        print("{%s {\\normalfont %s}}" % (student, award))
        print("{}")
        print("{}")
        print()

    section_footer()

def support(include_support="public"):
    supp = pull_data("support")

    print(r"\section{support}")

    include = ["current", "completed"]
    if include_support == "pending":
        include.append("pending")
    elif include_support == "all":
        include.extend( ["declined", "pending", "discouraged"] )

    def check_support(status):
        for inc in include:
            if inc in status:
                return True
        return False

    def print_support(a):
        def from_a(x):
            return de_html(a[x])
        title = de_html(a["title"])
        status = a["status"]
        if not check_support(status):
            return
        print("\\item")
        if "url" in a:
            url = a["url"]
            title = "\\href{%s}{%s}" % (url, title)
        print("\\textbf{{Project Title:}} {} \\\\".format(title))

        if "amount" in a:
            print("\\textbf{{Amount:}} {}".format(from_a("amount")))
            if "share" in a:
                print(" ({} Parker)".format(from_a("share")))
            print(r" \\")
        if "role" in a:
            print("\\textbf{{Role:}} {} \\\\".format(from_a("role")))
        if "source" in a:
            print("\\textbf{{Source:}} {} \\\\".format(from_a("source")))
        print("\\textbf{{Status:}} {} \\\\".format(status))
        if status == "current" or status == "completed":
            if "start" in a:
                print("\\textbf{{Start Date:}} {}".format(from_a("start")))
            if "end" in a:
                print("\\textbf{{End Date:}} {}".format(from_a("end")))
            if "start" in a or "end" in a:
                print("\\\\")
        if "ID" in a:
            print("\\textbf{{Award ID:}} {} \\\\".format(from_a("ID")))
        print(r"\vspace{-1em}")
        print()

    print()
    print(r"\subsection{funded support}")
    current = [a for a in supp if a["status"] == "current" or a["status"] == "completed"]
    print(r"\begin{itemize}[noitemsep]")
    for a in current:
        print_support(a)
    print(r"\end{itemize}")

    if "pending" in include:
        print()
        print(r"\subsection{pending support}")
        pending = [a for a in supp if a["status"] == "pending"]
        print(r"\begin{itemize}[noitemsep]")
        for a in pending:
            print_support(a)
        print(r"\end{itemize}")

    if "declined" in include:
        # also include discouraged in here
        print()
        print(r"\subsection{declined support}")
        declined = [a for a in supp if ("declined" in a["status"] or "discouraged" in a["status"])]
        print(r"\begin{itemize}[noitemsep]")
        for a in declined:
            print_support(a)
        print(r"\end{itemize}")

def fellowships():
    fellows = pull_data("student_fellowships")

    print(r"\subsection{student fellowships}")
    print(r"\begin{itemize}[noitemsep]")
    for f in fellows:
        name = de_html(f["for"])
        title = de_html(f["title"])
        start = de_html(f.get("start", ""))
        end = de_html(f.get("end", ""))
        source = de_html(f.get("source", ""))
        amount = de_html(f.get("amount", ""))
        print(r"\item")
        print(f"\\textbf{{student}}: {name} \\\\")
        print(f"\\textbf{{title}}: {title} \\\\")
        print(f"\\textbf{{fellowship}}: {source} \\\\")
        print(f"\\textbf{{amount}}: {amount} \\\\")
        print(f"\\textbf{{dates}} -- {start} -- {end}")

    print(r"\end{itemize}")

def lectures():
    lect = pull_data("lectures")

    print(r"\section{talks}")
    print()

    def print_lecture(l):
        title = de_html(l["title"])
        if title == "TBD":
            return
        time = de_html(l["time"])
        location = de_html(l["location"])
        institution = de_html(l["institution"])
        invited = l.get("invited", False)
        if invited:
            title += r" \textit{(invited)}"
        if not SIMPLE: print("\\entry")
        print("{%s}" % (time))
        print("{%s}" % (title))
        print("{%s}" % (location))
        print("{")
        print("%s" % (institution))
        print("}")
        print()

    if SPLIT_AT_CWRU:
        print(r"\subsection{Case Western Reserve University}")
        print()
        print(r"\begin{entrylist}")
        for l in lect:
            aff = l.get("affiliation", "")
            if "CWRU" in aff:
                print_lecture(l)
        print(r"\end{entrylist}")
        print()
        print(r"\subsection{Before Case Western Reserve University}")
        print()
        print(r"\begin{entrylist}")
        for l in lect:
            aff = l.get("affiliation", "")
            if not "CWRU" in aff:
                print_lecture(l)
        print(r"\end{entrylist}")
    else:
        print()
        print(r"\begin{entrylist}")
        for l in lect:
            print_lecture(l)
        print(r"\end{entrylist}")

def pedagogy():
    lect = pull_data("pedagogy")

    print(r"\section{pedagogical lectures}")

    def print_ped(l):
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

    if SPLIT_AT_CWRU:
        print()
        print(r"\subsection{Case Western Reserve University}")
        print()
        print(r"\begin{entrylist}")
        for l in lect:
            aff = l.get("affiliation", "")
            if "CWRU" in aff:
                print_ped(l)
        print(r"\end{entrylist}")
        print()
        print(r"\subsection{Before Case Western Reserve University}")
        print()
        print(r"\begin{entrylist}")
        for l in lect:
            aff = l.get("affiliation", "")
            if not "CWRU" in aff:
                print_ped(l)
        print(r"\end{entrylist}")
    else:
        print()
        print(r"\begin{entrylist}")
        for l in lect:
            print_ped(l)
        print(r"\end{entrylist}")


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
    # teach = pull_data("teaching")
    # section_header("select teaching")

    # for t in teach:
    #     time = de_html(t["time"])
    #     title = de_html(t["title"])
    #     role = de_html(t["role"])
    #     code = de_html(t.get("code", ""))
    #     level = de_html(t["level"])
    #     location = de_html(t["location"])
    #     if not SIMPLE: print("\\entry")
    #     print("{%s}" % (time))
    #     print("{%s}" % (title))
    #     print("{%s, %s}" % (level, location))
    #     print("{}")
    #     print()

    teach = pull_data("courses")
    print("\\section{courses taught}")

    print("\\begin{itemize}[noitemsep]")
    for t in teach:
        title = de_html(t["title"])
        when = de_html(t["taught"])
        courseid = de_html(t["id"])
        credits = de_html(t["credits"])
        print("\\item")
        print("%s: \\textbf{%s} (%s credits)" % (courseid, title, credits))
        print("--- %s" % when)
    print("\\end{itemize}")

def service():
    serv = pull_data("service")

    print("\\section{service}")
    print("\\begin{itemize}[noitemsep]")
    for s in serv:
        title = de_html(s["title"])
        role = de_html(s["role"])
        when = de_html(s["when"])
        print("\\item")
        print(f"{role}, {title} ({when})")

    print("\\end{itemize}")

def professional_service():
    print(r"\section{professional service}")
    print()

    peerreview()
    grantreview()

def grantreview():
    serv = pull_data("grant_review_summary")

    print(r"\subsection{grant review panels}")
    print(r"\begin{itemize}[noitemsep]")
    for s in serv:
        agency = de_html(s["agency"])
        print("\\item")
        print(f"{agency}")

    print("\\end{itemize}")

def peerreview():
    serv = pull_data("peer_review_summary")

    print(r"\subsection{peer review}")
    print(r"\begin{itemize}[noitemsep]")
    for s in serv:
        journal = de_html(s["journal"])
        number = de_html(s["number"])
        print("\\item")
        print(f"{journal} ({number})")

    print("\\end{itemize}")

def collaborators():
    collabs = pull_data("collaborators")

    print(r"\section{collaborators}")
    print()
    print(r"\subsection{Case Western Reserve University}")
    print(r"\begin{itemize}[noitemsep]")
    for c in collabs:
        if "CWRU" in c["affiliation"]:
            print(f"\\item {c['name']} ({c['affiliation']})")
    print(r"\end{itemize}")
    print()
    print(r"\subsection{External}")
    print(r"\begin{itemize}[noitemsep]")
    for c in collabs:
        if "CWRU" not in c["affiliation"]:
            print(f"\\item {c['name']} ({c['affiliation']})")
    print(r"\end{itemize}")

def advisees():
    gs = pull_data("grad_students")
    pd = pull_data("postdocs")
    ug = pull_data("undergrad_students")
    alumni = pull_data("alumni")

    current = set()
    for g in gs:
        current.add(g["name"])
    for p in pd:
        current.add(p["name"])
    for u in ug:
        current.add(u["name"])

    for alum in alumni:
        if alum["was"] == "undergraduate":
            ug.append(alum)
        elif alum["was"] == "Ph.D.":
            gs.append(alum)
        elif alum["was"] == "postdoc":
            pd.append(alum)

    # TODO: sort by start dates


    print(r"\section{advisees}")
    print()
    print(r"\subsection{postdoctoral researchers}")
    print(r"\begin{itemize}[noitemsep]")
    for p in pd:
        name = de_html(p['name'])
        start = de_html(p['start'])
        end = de_html(p.get('left', ""))
        where = de_html(p.get('where', ""))
        if p['name'] in current:
            print(f"\\item Dr. {name} ({start} -- )")
        else:
            print(f"\\item Dr. {name} ({start} -- {end}) --- now at {where}")
        print()
    print(r"\end{itemize}")

    print(r"\subsection{Ph.D. students}")
    print(r"\begin{itemize}[noitemsep]")
    for g in gs:
        name = de_html(g['name'])
        start = de_html(g['start'])
        end = de_html(g.get('left', ""))
        where = de_html(g.get('where', ""))
        if g['name'] in current:
            print(f"\\item {name} ({start} -- )")
        else:
            print(f"\\item {name} ({start} -- {end}) --- now at {where}")
        print()
    print(r"\end{itemize}")

    print(r"\subsection{undergraduate students}")
    print(r"\begin{itemize}[noitemsep]")
    for u in ug:
        name = de_html(u['name'])
        start = de_html(u['start'])
        end = de_html(u.get('left', ""))
        where = de_html(u.get('where', ""))
        if u['name'] in current:
            print(f"\\item {name} ({start} -- )")
        else:
            print(f"\\item {name} ({start} -- {end}) --- now at {where}")
        print()
    print(r"\end{itemize}")

def make_tex(style, printcolors, do_support=False, include_support="public"):
    header(style, printcolors)
    if (style == "resume"):
        aside()
    positions()
    memberships()
    awards()
    papers()
    chapters()
    media()
    lectures()
    pedagogy()
    if do_support:
        support(include_support=include_support)
        fellowships()
    collaborators()
    service()
    professional_service()
    teaching()
    advisees()
    student_awards()
    footer()

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Script to auto-generate a CV or a Resume from collected yaml files")
    parser.add_argument("-t", "--type", type=str, dest="style", choices=("cv", "resume"), default="cv")
    parser.add_argument("-s", "--support", dest="support", action="store_true")
    parser.add_argument("-S", "--support-type", choices=("all", "public", "pending"), default="public",
                        help="type of support to include")
    parser.add_argument("-p", "--print", dest="printcolors", action="store_true")
    parser.add_argument("-c", "--condensed", dest="condensed", action="store_true")
    parser.add_argument("--cwru", dest="cwru", action="store_true")

    args = parser.parse_args()

    style = args.style
    printcolors = args.printcolors
    SIMPLE = args.condensed
    SPLIT_AT_CWRU = args.cwru

    make_tex(style, printcolors, do_support=args.support, include_support=args.support_type)
