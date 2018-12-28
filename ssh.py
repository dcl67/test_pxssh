#!/usr/bin/env python

from pexpect import pxssh
import getpass
try:
	s = pxssh.pxssh()
	hostname = raw_input('hostname: ')
	username = raw_input('username: ')
	password = getpass.getpass('password: ')
	s.login(hostname, username, password)
	s.sendline('uptime') #run command
	s.prompt() #match the prompt
	print s.before
	s.sendline ('ls -l')
	s.prompt()
	print s.before
	s.sendline ('df')
	s.prompt()
	print s.before
	s.logout()
except pxssh.ExceptionPxssh, e:
	print "pxssh failed on login."
	print str(e)
