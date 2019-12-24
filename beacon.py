#!/usr/bin/python3
# Python code to print International Beacon Project beacons as they occur.
# You will need to set the PC clock accurately or lock to NTP.
# License: Free to use and modify but please retain the credit.

print (" ")
print (" International Beacon Project announcement utility")
print (" Dan Garley WH6A V.9 (python 3) Nov. 2019")
print (' functionally similar to (and based on) V1.11 (bash) By Tim Howe G0ETP May-Dec 2014')
print ("  ")
print (" Comand line argument 1 is the band offset:")
print (" 0=14.100 1=18.110 2=21.150 3=24.930 4=28.200")
print (" ")

import sys
from datetime import datetime, timezone
import time

band_list = ['14.100','18.110','21.150','24.930','28.200']
starttime=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

# Get the command line parameter and enforce a default value of 0
if len(sys.argv)>0:
	band=sys.argv[1]
else:
	band=0


print (' Currently using band offset',band,'; data will be for',band_list[int(band)],' Mhz beacons')
print (" ")
print (" Started at ",starttime,"UTC")
print (" ")

# List of beacon callsigns and information
# The trailing tabs are there so that the 'next' column lines up
# Feel free to edit these strings as required (e.g. to add an indication
# of current beacon status)

callsign_list = [
	'4U1UN\tUnited Nations\t',
	'VE8AT\tCanada\t\t',
	'W6WX\tUSA\t\t',
	'KH6WO\tHawaii\t\t',
	'ZL6B\tNew Zealand\t',
	'VK6RBP\tAustralia\t',
	'JA2IGY\tJapan\t\t',
	'RR9O\tRussia\t\t',
	'VR2B\tHong Kong\t',
	'4S7B\tSri Lanka\t',
	'ZS6DN\tSouth Africa\t',
	'5Z4B\tKenya\t\t',
	'4X6TU\tIsrael\t\t',
	'OH2B\tFinland\t\t',
	'CS3B\tMadeira\t\t',
	'LU4AA\tArgentina\t',
	'OA4B\tPeru\t\t',
	'YV5B\tVenezuela\t',
	]

# Check for 10 sec boundaries (beacons rotate every 10 seconds)
while True:
	now=datetime.now()
	if now.second%10 == 0:
		# Calculate a 1-dimensional 'beacon id' based on the minute and 10 sec interval
		min_mod=now.minute%3
		sec_div=now.second / 10
		b_id=sec_div + min_mod * 6

		# Apply the band offset and re-apply modulo
		b_id_shifted=(float(b_id) + 18 - float(band)) % 18
		b_id_shifted_next=(float(b_id) + 19 - float(band)) % 18
		print(callsign_list[int(b_id_shifted)],'Next: ',callsign_list[int(b_id_shifted_next)])
		time.sleep(9.6)

	time.sleep(.1)





