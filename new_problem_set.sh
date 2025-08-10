#!/bin/bash

if [[ $# -ne 4 ]]; then
    echo "usage: new.sh <debugsOrassignments> <problemsetname> <problemname> <basename>"
    exit 2
fi

# doc
mkdir -p $1/$2/$3/doc
touch $1/$2/$3/doc/doc.md

# starter
mkdir $1/$2/$3/_starter
touch $1/$2/$3/_starter/$4.py

# solution
touch $1/$2/$3/$4.py

# setup problem test script from template
mkdir $1/$2/$3/tests
#touch $1/$2/$3/tests/test_$4.py
#topics=$(echo "$2" | cut -c14-)
classname=$(sed -r 's/(^|_)([a-z])/\U\2/g' <<< $4)
sed -e "s/\${filename}/$4.py/" -e "s/\${classname}/$classname/" test.py.template > $1/$2/$3/tests/test_$4.py
