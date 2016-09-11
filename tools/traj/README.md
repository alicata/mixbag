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

## trajLogger
utility to plot frames correlatd to a spatio-temporal trajectory 

example usage,
```
python trajLogger.py
```

