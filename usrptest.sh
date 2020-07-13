   /usr/local/lib/uhd/examples/benchmark_rate  \
   --args "type=n3xx,mgmt_addr=192.168.10.2,addr=192.168.10.2,master_clock_rate=125e6" \
   --duration 60 \
   --channels "0,1,2,3" \
   --rx_rate 1.25e6 \
   --rx_subdev "A:0 A:1 B:0 B:1" \
   --tx_rate 1.25e6 \
   --tx_subdev "A:0 A:1 B:0 B:1"

