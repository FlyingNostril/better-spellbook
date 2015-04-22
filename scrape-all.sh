#! /bin/bash
#A nice shell grandma to scrape every spell from a sourcebook
#this is mostly for me and me alone, although it may work for others that have a POSIX-compliant OS

#Expects a full path to the sourcebook and the name of the sourcebook from command line args
SOURCEBOOK_PATH=$1
SOURCEBOOK_NAME=$2
SPELL_LIST=($SOURCEBOOK_PATH/*)
#echo ${#SPELL_LIST[$@]}
mkdir spell-text
cd spell-text
touch "$SOURCEBOOK_NAME".txt
for ITEM in $SOURCEBOOK_PATH/* ; do
	if [[ -d $ITEM ]] ; then
		echo "Scraping $ITEM"
		../dndtools-scraper.py $ITEM/index.html >> "$SOURCEBOOK_NAME".txt
	fi
done
#mkdir spell-text
#cd spell-text

