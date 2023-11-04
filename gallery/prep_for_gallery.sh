#!/bin/bash

# This script is used to prepare the images for the gallery.

# Input should be some sort of file format
input=$1
output=$2

# check that the input is a file
if [ ! -f $input ]; then
    echo "Input is not a file"
    exit 1
fi

#check that output is provided
if [ -z $output ]; then
    echo "Output not provided"
    exit 1
fi

# strip ending and path from input to make output
#make sure output has a .jpg ending
output=${output%.*}.jpg

convert $input -scale 50% -quality 85 $output
convert $input -resize 200 -quality 60 thumb/$output

echo Add the following to the gallery yaml
echo
echo "  - name: $output"
echo "    alt: ${output%.*}"
