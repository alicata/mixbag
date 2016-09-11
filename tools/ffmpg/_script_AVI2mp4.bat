set INFILE="in_skategirl01_30fps.mp4"
set INFILEAVI = %INFILE%.avi
echo %INFILEAVI%
pause

c:\bin\ffmpeg -v 63 -y -f avi -i IN02.mp4.avi -pix_fmt yuv420p -codec:v libx264 -r 30 -preset slow -b:v 4000k -maxrate 4000k -bufsize 16000k -f mp4 out_02.mp4
c:\bin\ffmpeg -v 63 -y -f avi -i IN03.mp4.avi -pix_fmt yuv420p -codec:v libx264 -r 30 -preset slow -b:v 4000k -maxrate 4000k -bufsize 16000k -f mp4 out_03.mp4
c:\bin\ffmpeg -v 63 -y -f avi -i IN04.mp4.avi -pix_fmt yuv420p -codec:v libx264 -r 30 -preset slow -b:v 4000k -maxrate 4000k -bufsize 16000k -f mp4 out_04.mp4


pause