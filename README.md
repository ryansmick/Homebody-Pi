# Homebody-Pi
Python application to track users on a wifi network

Big Picture
-----------

This repository is part of a larger project that I will refer to as Homebody. This purpose of this project is to inform members of a household whether or not other members of the household are home at any given time. This repository plays a role in that goal by running a device scan over a network to determine which devices are present at a given time.

Setup
-----

The included code is meant to run indefinitely on a raspberry pi that is connected to the user's home network, but can theoretically be run on any UNIX machine connected to the network. Once you've decided on a machine, follow the directions below to get the code up and running.

```
$ wget https://github.com/ryansmick/Homebody-Pi/archive/master.zip
$ unzip master.zip
$ cd Homebody-Pi-master
$ pip install requirements.txt
```

NOTE: This repository is meant to run on Python 3, and may not work with Python 2.

Execution
---------

Before execution the script, you must determine the name of the network interface on which you would like to scan. In order to do this, simply run the `ifconfig` command.

```
$ ifconfig
lo        Link encap:Local Loopback  
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:16436  Metric:1
          RX packets:8 errors:0 dropped:0 overruns:0 frame:0
          TX packets:8 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0 
          RX bytes:480 (480.0 b)  TX bytes:480 (480.0 b)

p2p1      Link encap:Ethernet  HWaddr 00:1C:C0:AE:B5:E6  
          inet addr:192.168.0.1  Bcast:192.168.0.255  Mask:255.255.255.0
          inet6 addr: fe80::21c:c0ff:feae:b5e6/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:41620 errors:0 dropped:0 overruns:0 frame:0
          TX packets:40231 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000 
          RX bytes:21601203 (20.6 MiB)  TX bytes:6145876 (5.8 MiB)
          Interrupt:21 Base address:0xe000 
```
In the above case, the user only has one option (p2p1), which appears to be a wired connection. The user can then run the command `python start_service.py` and enter `p2p1` when prompted for the network interface. If multiple interfaces appear, choose the one that is connected to your home network. If you aren't sure which to choose, try one and look at the devices listed.

Issues
------

* The script doesn't work perfectly on every scan, and it seems to have trouble with Android phones in particular. I believe this is because Android turns off wifi while the phone is asleep, causing pings to go unanswered.
