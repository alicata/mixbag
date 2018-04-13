choco install -y vim
choco install -y git
git config --system --unset credential.helper

choco install -y miniconda3 /AddToPath:1 /RegisterPython:1 /D=C:\Users\lattepanda\Miniconda3
echo "add to path, "
echo "c:\tools\miniconda3"
echo "c:\tools\miniconda3\scripts"

choco install -y openssh
choco install -y openvpn
