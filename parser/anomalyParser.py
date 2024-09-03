# Visual Anomaly FOMO-AD Parser
# Roni Bandini @RoniBandini
# September 2024 MIT License
# https://bandini.medium.com
# Details: parse impulse runner and call servo arm


import subprocess
import time
import serial 
import os
from keyboard import press
from art import *

outputFile = open('output.txt', 'w')
arduino = serial.Serial(port='COM26', baudrate=115200, timeout=.1) 
discardLines=40
anomalyThreshold=100

def controlServo(x): 
	   arduino.write(bytes(x, 'utf-8')) 
	   time.sleep(0.05) 
	   data = arduino.readline() 
	   return data 

os.system('cls')

print(text2art("Visual Anomaly", font="small"))
print("Roni Bandini, Argentina, @RoniBandini")
print("")
print("Stop with CTRL-C")
time.sleep(3)

# Impulse runner in a subprocess, sending the output to a file
subprocess.Popen(["edge-impulse-run-impulse", "--debug"], shell=True, stdout=outputFile, bufsize=0)
# Select the first COM port
press('enter') 


with open("output.txt", "r") as f:

	lines_seen = set()

	while True:

		line = f.readline()

		if not line:
			time.sleep(1)
			continue

		if ("Visual anomaly values" in line) and line not in lines_seen:

			#print(line)
			parts = line.split("Max ")
			myAnomalyScore = parts[1].rstrip()
			
			# if you want to use anomaly mean instead
			# parts = line.split("Mean ")
			# parts2 = parts[1].split("Max ")
			# myAnomalyScore = parts2[0].rstrip()

			print("Anomaly score: "+myAnomalyScore)

			if float(myAnomalyScore)>anomalyThreshold:
				print("...removing piece")
				print("")

				value = controlServo("1")

				# discard next inspections to avoid duplicates
				counter=0
				while counter<discardLines:
					line = f.readline()
					lines_seen.add(line)
					counter=counter+1

			else:
				print("...piece ok")
				print("")


		lines_seen.add(line)

                