#!/bin/zsh

old_IFS=$IFS
IFS=$'\n'

if [[ "$1" == "" ]]
then
	echo "usage: $0 [folder]"
	exit 1
fi

rm $1/*.eps
rm $1/*.pdf

for f in `ls -1 $1 | grep ' '`
do
	fname=`echo $f | sed -e 's/ /_/g'`
	mv "$1/$f" $1/$fname
done

for f in `ls -1 $1 | grep "svg$"`
do
	svg2eps.sh $1/$f
done

IFS=$old_IFS

