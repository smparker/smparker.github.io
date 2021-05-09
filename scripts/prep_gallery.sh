#!/bin/bash

if [ "$1" == "-h" ] || [ "$1" == "--help" ] || [ "$1" == "" ]; then
  echo "usage:"
  echo "$0 img1 [img2 [...]]"
  echo
  echo "prepare image for a gallery by converting to smaller jpg in current directory"
  echo "and placing a thumbnail in ./thumb"
  exit
fi

prep() {
  x="$1"
  imgname=$(basename "$x")
  convert "$x" -auto-orient -scale 50% -quality 90 ${imgname%.*}.jpg
  convert "$x" -auto-orient -thumbnail 200x200^ \
          -gravity center -extent 200x200 -unsharp 0x.5 thumb/${imgname%.*}.jpg
}
export -f prep

for x in "$@"; do
  prep "$@"
done
