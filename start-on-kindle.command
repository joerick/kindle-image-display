#!/bin/bash

# First plug in the kindle and configure that interface to be:
#   IP address:  192.168.15.1
#   Subnet mask: 255.255.255.0

ssh root@192.168.15.244 "sh /mnt/us/extensions/grisedale/init-weather.sh"
