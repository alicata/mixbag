# traj tools
tools for timestamp data stream processing

## plot_file_timestamped_data
plot two synched data channels (channels' data points share same timestamps)

timestamp | channel 1 | channel 2
--------- | --------- | ---------
10000.1   | 10        | 44
10000.2   | 23        | 10
...       | ..        | ..

example usage,
```
python plot_file_timestamped_data.py data0.txt
```

## plot_score_matrix
plot labeled 2d data matrix

example usage,
```
python plot_score_matrix.py data0.csv
```

## traj_logger
utility to log a in-memory timestamped trajectory and image data stream to text and image files 

timestamp trajectory format is,
millisec  | x | y | w  | h  |
--------- | - | - | -- | -- |
10000.1   | 0 | 4 | 10 | 9  | 
10000.2   | 0 | 1 | 11 | 11 |
...       |.. |.. | .. | .. |

example usage,
```
python traj_logger.py
```
this test generate a fake trajectory with fake image frames and then logs them to: 
  * text file (test.traj.txt) 
  * combined as well as individual jpg image files

