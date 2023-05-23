#!/bin/bash

cd latex_cv
  ./texify smp_cv
  cp smp_cv.pdf ../assets/smp_cv.pdf
cd ..

echo "date: $(date +"%m/%d/%Y")" > _data/cv.yml
echo "path: assets/smp_cv.pdf" >> _data/cv.yml
