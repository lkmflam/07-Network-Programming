# Examples

## Python get IP address
With gethostbyname(), we get the IP address of the host.

### File: get_ip.py
```python
#!/usr/bin/env python

import socket

ip = socket.gethostbyname('example.com')
print(ip)
```
The example prints the IP address of example.com.
```
$ ./get_ip.py
93.184.216.34
```
This is the output.
