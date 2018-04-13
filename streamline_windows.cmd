echo "---------------------------"
echo "Debloat Windows10"
echo "---------------------------"
cd ~
git clone https://github.com/Sycnex/Windows10Debloater.git

cd Windows10Debloater
powershell -executionpolicy bypass -file Windows10Debloater.ps1
