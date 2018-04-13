# open administrative prompt
# change UAC prompt to silent
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

invoke-webrequest -uri "https://www.tightvnc.com/download/2.8.8/tightvnc-2.8.8-gpl-setup-64bit.msi" -outfile "tvnc.msi" -usebasicparsing

