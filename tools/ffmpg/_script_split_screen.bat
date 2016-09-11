c:\bin\ffmpeg -i out_in_skategirl01_30fps.mp4 -i out_in_skategirl01_60fps.mp4 -filter_complex "[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]" -map [vid] -c:v libx264 -crf 23 -s 1600x400 -preset veryfast output_split.mp4
pause

REM works with ZUNE Player but not Media Player
REM c:\bin\ffmpeg -i out00.mp4 -i out01.mp4 -i out02.mp4 -i out03.mp4 -filter_complex "[0:0]pad=iw*2:ih*2[a];[1:0]negate[b];[2:0]hflip[c];[3:0]edgedetect[d];[a][b]overlay=w[x];[x][c]overlay=0:h[y];[y][d]overlay=w:h" -y -c:v libx264 -crf 23 -s 640x480 -preset veryfast output_split_overlay_grid.mp4
REM pause

 