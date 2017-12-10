#!/bin/bash

# build jekyll site
jekyll build

# test site with htmlproofer
htmlproofer --check-html \
            --check-favicon \
            --check-opengraph \
            --empty-alt-ignore \
            --url-ignore 'https://scholar.google.com/citations?user=OqC2Vc8AAAAJ&hl=en' \
            --url-swap "https?\:\/\/(localhost\:4000|smparker\.github\.io):" \
            _site
