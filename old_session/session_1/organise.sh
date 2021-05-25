#!/bin/bash
# Program:
#       This program organises the folder: put the file under the folder with it's ID.
# History:
# 2016/01/18 YJ

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

# check the file having the #ID
# if fit, move it into desired folder
# else, skip into next file.

# get the path of current directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR

for entry in $DIR/*
do
    if [[ $entry =~ ^$DIR\/\_[0-9]{1,3}\_ ]]; then
        # echo "HIT"
        # get its #ID
        FLD=$(echo $entry | grep -o -P \_[0-9]+\_+)
        FLDID=$(echo $FLD | grep -o -P [0-9]+)
        echo "$FLDID"
        # put it into the folder
        if [ ! -d "$DIR/$FLDID/" ]; then
            mkdir $DIR/$FLDID
        fi
        mv $entry $DIR/$FLDID/
        
    else
        echo "$entry"
    fi
done

exit 0