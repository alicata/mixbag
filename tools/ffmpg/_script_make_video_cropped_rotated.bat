REM c:\bin\ffmpeg -f image2 -i frame%%05d.png -r 120 -s 640x360 -vf "transpose=3" -y foo.avi


c:\bin\ffmpeg -f image2 -i frame%%05d.png -r 120 -s 640x360 -vf "transpose=1" -y rotated.avi

c:\bin\ffmpeg -f image2 -i frame%%05d.png -r 240 -vf crop=640:360:160:160  -y cropped.avi


pause