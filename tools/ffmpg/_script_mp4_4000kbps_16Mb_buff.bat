

set INFILE="12_biker_02.mp4"

echo %INFILE%

c:\bin\ffmpeg -v 63 -y -i test_Berkeley.mp4 -pix_fmt yuv420p -codec:v libx264 -vprofile baseline -preset slow -b:v 8000k -maxrate 8000k -bufsize 32000k out_test_Berkeley.mp4 








REM set INFILE="in_skategirl01_60fps.mp4"
REM echo %INFILE%
REM c:\bin\ffmpeg -v 63 -y -i %INFILE% -pix_fmt yuv420p -codec:v libx264 -preset slow -b:v 4000k -maxrate 4000k -bufsize 16000k -r 60 out_%INFILE%
