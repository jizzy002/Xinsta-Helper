import subprocess
import requests
import os
from bs4 import BeautifulSoup
from time import sleep
import os.path


def decompileInstagram():
	os.system("jadx0.9.0/bin/jadx input/*.apk -d output");



def Find(cmd):
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	(out, err) = proc.communicate()

	out = out.replace(";", "")
	out = out.replace("import ", "")
	out = out.replace(".java", "")
	out = out.replace("output/", "")
	out = out.replace("/", ".")
	out = out.replace("\n", "")
	out = out.replace("\r", "")
	out = out.rstrip()	

	return out

def main():
	try:
		decompileInstagram()
	except BaseException as error:
		print("Failed Decompiling Instagram ", error)

main()
