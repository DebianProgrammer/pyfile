import os
import os.path

everything = os.listdir(os.getcwd())
fulleverything = [os.path.abspath(x) for x in os.listdir()]
path = "."

def list():
	everything = os.listdir(os.getcwd())

	for thing in everything:
		if(os.path.isdir(thing)):
			print(f"{thing} {everything.index(thing)} <DIR>")
		if(os.path.isfile(thing)):
			print(f"{thing} {everything.index(thing)}")
list()

while True:
	print(" ")
	print(os.getcwd())
	print(" ")
	newpath = input("Enter a number or use -1 to go back: ")
	if(newpath == "-1"):
		print(" ")
		os.chdir("..")
		list()
		everything = os.listdir(os.getcwd())
		continue
	newpath = int(newpath)
	newpath = everything[newpath]
	if(os.path.isfile(newpath)):
		os.system("more " + newpath)
		print(" ")
		continue
	print(" ")
	os.chdir(newpath)
	list()
	everything = os.listdir(os.getcwd())
