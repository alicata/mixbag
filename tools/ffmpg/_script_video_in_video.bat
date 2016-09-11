c:\bin\ffmpeg -y -i out00.mp4 -s 320x240 out320l.mp4 
c:\bin\ffmpeg -y -i out01.mp4 -s 160x120 out320A.mp4 
c:\bin\ffmpeg -y -i out02.mp4 -s 160x120 out320B.mp4 

REM Expand the left video to the final video dimensions
c:\bin\ffmpeg -y -i out320l.mp4 -vf "pad=640:240:0:0:black" left_wide.mp4

REM Overlay the right video on top of the left one
c:\bin\ffmpeg -y -i left_wide.mp4 -vf "movie=out320A.mp4 [mv]; [in][mv] overlay=320:120" combined_video.mp4
c:\bin\ffmpeg -y -i combined_video.mp4 -vf "movie=out320B.mp4 [mv]; [in][mv] overlay=320:0" combined_video2.mp4

pause

c:\bin\ffplay -i combined_video2.mp4