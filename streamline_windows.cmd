echo "---------------------------"
echo "Debloat Windows10"
echo "---------------------------"
cd ~
git clone https://github.com/Sycnex/Windows10Debloater.git

cd Windows10Debloater
powershell -executionpolicy bypass -file Windows10Debloater.ps1


echo "---------------------"
echo "stop windows updates "
echo "---------------------"
stop-service wuauserv
set-service wuauserv -startuptype disabled


echo "---------------------"
echo "power settings for continous operation "
echo "---------------------"
powercfg.exe -change -monitor-timeout-ac 0
powercfg.exe -change -monitor-timeout-dc 0
powercfg.exe -change -disk-timeout-ac 0
powercfg.exe -change -disk-timeout-dc 0
powercfg.exe -change -standby-timeout-ac 0
powercfg.exe -change -standby-timeout-dc 0
powercfg.exe -change -hibernate-timeout-ac 0
powercfg.exe -change -hibernate-timeout-dc 0

