REM overlay text
c:\bin\ffmpeg -y -i out00.mp4 -vf drawtext="fontfile=/Windows/Fonts/arial.ttf:text='Test':fontsize=64:fontcolor=red:x=100:y=100" _text.mp4

REM overlay frame timecode
c:\bin\ffmpeg -y -i out00.mp4 -vf drawtext="fontfile=/Windows/Fonts/arial.ttf:timecode='00\:00\:00\:00':r=30:fontsize=64:fontcolor=red:x=100:y=100:box=1: boxcolor=0x00000099" _text.mp4



pause
c:\bin\ffplay -i _text.mp4
