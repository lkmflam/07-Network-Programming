#Automated to display ifconfig
#!/usr/bin/env python

import subprocess
subprocess.call("ifconfig", shell=True)

