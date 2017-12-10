#!/bin/bash

# build jekyll site
jekyll build

# test site with htmlproofer
htmlproofer --check-html \
            --check-favicon \
            --check-opengraph \
            --empty-alt-ignore \
            --url-swap "https?\:\/\/(localhost\:4000|smparker\.github\.io):" \
            _site
