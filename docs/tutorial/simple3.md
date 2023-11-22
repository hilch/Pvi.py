## Change Line

Download [simple3.py](https://github.com/hilch/Pvi.py/tree/main/examples/simple3.py) (INA2000)
This is similar to simple2.py but we use a control running AR 3.x. ANSL is not available here and we change to good old INA2000.

INA2000 line needs slightly different parameters for itself:
```
line = Line( pviConnection.root, 'LNINA', CD='LNINA2')
```
and for its device, too:
```
device = Device( line, 'TCP', CD='/IF=TcpIp /SA=113' )
```
all members in an INA2000 based network must follow the 'Highlander principle' [^1] e,g, all node numbers must be unique.

Even the PC acting as PVI client needs an unique node number which is determined by the '/SA' parameter.

Why on earth do I need a node number for TcpIp ? Well, you're right. But INA2000 has a long history starting with CAN based network.

But even if you opt for a modern Ethernet-based network using IP addresses, you still have to specify this node parameter for the CPU and node number '1' is usually already occupied by the connected CPU [^2] .

The further effects of this protocol then also affect the CPU itself.
With INA2000 we can now choose between addressing by node number ('/DA') or addressing by IP address ('/DAIP'):
```
cpu = Cpu( device, 'myPP65', CD='/DAIP=10.49.40.222' )
```

Everything else requires no change compared to the ANSL example. Since we are working with a real CPU and not with a simulation, a lot can go wrong, which is not due to this example :-)

The other examples that use INA2000 can also be very different from the examples based on ANSL. Read the documentation to understand which parameters you can use and what possibilities INA2000 offers.



[^1]: If you do not grew up in the eighties: 'there can be only one', https://en.wikipedia.org/wiki/Highlander_(film).

[^2]: https://en.wikipedia.org/wiki/Murphy%27s_law

