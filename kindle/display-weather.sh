#!/bin/sh

cd "$(dirname "$0")"

sleep 1

rm /tmp/grisedale.png

eips -d l=0,w=600,h=800
sleep 1
eips -c

if wget -O /tmp/grisedale.png http://grisedalepike.herokuapp.com/kindleimage; then
	eips -g /tmp/grisedale.png
else
	eips -g fail-no-image.png
fi

sleep 1
