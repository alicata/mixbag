
REM ffmpeg -i frame00001.png -i frame00002.png -vcodec mpeg4 atestpng.avi

ffmpeg -f image2 -i frame%%05d.png -r 12 -s 1280x720 atest2png.avi

pause

