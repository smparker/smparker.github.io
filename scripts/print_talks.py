#!/usr/bin/env python

from __future__ import print_function

import yaml

data = yaml.safe_load(open("lectures.yml"))

print(data)
for x in data:
    talktype = "invited talk" if x["invited"] else "talk"
    print("@Misc{")
    print("    OPTkey =   {},")
    print("    author =   { \\underline{Shane M. Parker} and Filipp Furche },")
    print("    title =   {{{{ {0} }}}},".format(x["title"]))
    print("    howpublished =   {{{0}, {1}, {2}}},".format(talktype, x["institution"], x["location"]))
    print("    OPTmonth = {},")
    print("    year = {{{0}}},".format(x["time"]))
    print("    OPTnote = {},")
    print("    OPTannote = {}")
    print("}")
