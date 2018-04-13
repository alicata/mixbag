# open TPC and icmp port for PING
netsh advfirewall firewall add rule name="ICMP Allow incoming V6 echo request" protocol="icmpv6:8,any" dir=in action=allow
netsh advfirewall firewall add rule name="ICMP Allow incoming V4 echo request" protocol="icmpv4:8,any" dir=in action=allow
netsh advfirewall add rule name=sshd dir=in action=allow protocol=TCP localport=22
