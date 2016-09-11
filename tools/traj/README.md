# traj tools
tools for timestamp data stream processing

## plot_file_timestamped_data
plot two synched data channels (channels' data points share same timestamps)

![plot_file_timestamped_data](https://github.com/alicata/mixbag/blob/master/tools/traj/img/img_plot_file_timestamped_data.png)

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
plot data matrix with row and column labels

![plot_score_matrix](https://github.com/alicata/mixbag/blob/master/tools/traj/img/img_plot_score_matrix.png)
example usage,
```
python plot_score_matrix.py data0.csv
```

## traj_logger
utility to log a in-memory timestamped trajectory and image data stream to text and image files 

timestamp trajectory format is,

timestamp | x         | y         | width     | y
--------- | --------- | --------- | --------- | --------- 
10000.1   | 10        | 44        | 144       | 120
10000.2   | 23        | 10        | 154       | 100
...       | ..        | ..        | ..        | ..

example usage,
```
python traj_logger.py
```
this test generate a fake trajectory with fake image frames and then logs them to: 
  * text file (test.traj.txt) 
  * combined as well as individual jpg image files

