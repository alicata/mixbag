# open TPC and icmp port for PING
netsh advfirewall firewall add rule name="ICMP Allow incoming V6 echo request" protocol="icmpv6:8,any" dir=in action=allow
netsh advfirewall firewall add rule name="ICMP Allow incoming V4 echo request" protocol="icmpv4:8,any" dir=in action=allow
netsh advfirewall add rule name=sshd dir=in action=allow protocol=TCP localport=22

# OPENSSH
# Disable Devloper-mode SSH Proxy/Borker because they block port 22
Set-Service SshBroker -StartupType Disabled
Set-Service SshProxy -StartupType Disabled

# OPENSSH as SERVER 
# Start sshd and generate host keys uner %programdata%\ssh
#
net start sshd
Set-Service sshd -StartupType Automatic
Set-Service ssh-agent -StartupType Automatic
