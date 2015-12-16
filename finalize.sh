#/bin/bash

print_usage () {
	echo "usage: $0 file.tex"
}

CURR_DATE=`date +%F`
DATE_PATTERN="s/\\\\date{\\\\today}/\\\\date{$CURR_DATE}/"

OUT_DIR="./Final"
FNAME_PATTERN="s/.tex/_${CURR_DATE}.tex/g"
FINAL_NAME=`echo "$1" | sed -e $FNAME_PATTERN`

if [ "$1" = "" ] ; then
	print_usage
	exit 1
fi

if [ ! -d "$OUT_DIR" ] ; then
	echo "Creating directory '$OUT_DIR'..."
	mkdir -p $OUT_DIR
fi

echo "Changing '\\date' to '$CURR_DATE'..."
sed "$DATE_PATTERN" $1 > $OUT_DIR/$FINAL_NAME

