## ciscoconfdict

A Python 3 package for parsing and analysing Cisco-style configurations.

**THIS PROJECT IS CURRENTLY IN ITS PLANNING STAGE**

**ciscoconfdict** is an abstraction layer on top of the excellent [ciscoconfparse](https://github.com/mpenning/ciscoconfparse) Python package. 
It aims to make analysing existing network configurations as easy as possible by providing a filtering mechanism that emulates Python
dictionaries. 

**ciscoconfdict** is not a replacement for [ciscoconfparse](https://github.com/mpenning/ciscoconfparse) as it implements 
only a small subset of [ciscoconfparse's](https://github.com/mpenning/ciscoconfparse) features.

### Example

The `ciscoconfdict.CiscoConfDict` class accepts the same arguments as `ciscoconfparse.CiscoConfParse`, either a file object or a *list*
of configuration lines.

```python
config = """
! Cisco IOS configuration fragment
!
clock timezone GMT 0
ntp server 192.0.2.34
ntp server 192.0.2.35
!
interface null0
 no ip unreachables
!
interface Ethernet2/0
 description Internet
 ip address 192.0.2.14 255.255.255.240
!
interface Ethernet2/1
 description DMZ
 ip address 192.0.2.17 255.255.255.240
""".split('\n')

import ciscoconfdict

confdict = ciscoconfdict.CiscoConfDict(config)
```

The configuration can now be filtered by passing *regular expressions* as dictionary keys. For example, all Ethernet interface 
sections can be selected as shown below. The result of any dictionary-style filter operation is an instance of
`ciscoconfdict.CiscoConfLines`.

```python
ethernet_interfaces = confdict['^interface Ethernet']
assert len(ethernet_interfaces) == 2
```

The string representation of `ciscoconfdict.CiscoConfLines` are the matched configuration sections as text whereas 
its `.ioscfg` attribute returns the *list* of configuration lines.

```python
print(ethernet_interfaces)
# interface Ethernet2/0
#  description Internet
#  ip address 192.0.2.14 255.255.255.240
# interface Ethernet2/1
#  description DMZ
#  ip address 192.0.2.17 255.255.255.240

ethernet_interfaces.ioscfg
# ['interface Ethernet2/0', ' description Internet', ' ip address 192.0.2.14 255.255.255.240', ...]
```

The individual matched configuration sections can also be accessed by index or iterated over. Both approaches
return instances of `ciscoconfdict.CiscoConfLines`.

```python
for ethernet_interface in ethernet_interfaces:
    assert isinstance(ethernet_interface, ciscoconfdict.CiscoConfLines)
    
assert isinstance(ethernet_interfaces[1], ciscoconfdict.CiscoConfLines)
```

Nested dictionary access allows for 'chaining' multiple filters together. The code below filters for the Ethernet interface 
towards the Internet.

```python
internet_interface = confdict['^interface Ethernet']['Internet']
assert len(internet_interface) == 1

print(internet_interface)
# interface Ethernet2/0
#  description Internet
#  ip address 192.0.2.14 255.255.255.240
```


