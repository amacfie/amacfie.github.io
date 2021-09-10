#!/usr/bin/env bash
if [ "$#" -ne 1 ]; then
  echo "Pass the post name filename suffix"
  exit 1
fi
fn="`dirname $0`/_posts/`date +\%Y-\%m-\%d-`$1.md"

touch $fn
echo "---" > $fn
echo "layout: post" >> $fn
echo "title: <ENTER TITLE HERE>" >> $fn
echo "---" >> $fn
printf "\n" >> $fn
nvim $fn -c "normal zR3ggf<vf>"

