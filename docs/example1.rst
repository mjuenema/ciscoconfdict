
Example 1: Basics
-----------------

The ``ciscoconfdict.CiscoConfDict`` class accepts the same arguments as
``ciscoconfparse.CiscoConfParse``, either a file object or a list of
configuration lines.

.. code:: ipython3

    config = """
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

The configuration can be searched using Python dictionary-style access.
In contracst to Python dictionaries, the “keys” are actually interpreted
as regular expressions.

.. code:: ipython3

    ntp_servers = confdict['^ntp server']

The result is a ``ciscoconfdict.CiscoConfLines`` object.

.. code:: ipython3

    type(ntp_servers)




.. parsed-literal::

    ciscoconfdict.CiscoConfLines



The length of the ``ciscoconfdict.CiscoConfLines`` object shows how many
``ntp server`` lines were found.

.. code:: ipython3

    len(ntp_servers)




.. parsed-literal::

    2



The found lines can be accessed as the ``.ioscfg`` property or ``.text``
property.

.. code:: ipython3

    ntp_servers.ioscfg




.. parsed-literal::

    ['ntp server 192.0.2.34', 'ntp server 192.0.2.35']



.. code:: ipython3

    print(ntp_servers.text)


.. parsed-literal::

    ntp server 192.0.2.34
    ntp server 192.0.2.35


Indexed access allows selecting individual ``ntp server`` lines. The
returned values are also ``ciscoconfdict.CiscoConfLines`` objects,
albeit with a lenght of one.

.. code:: ipython3

    ntp_servers[0]




.. parsed-literal::

    <ciscoconfdict.CiscoConfLines at 0x7f5ae4167898>



.. code:: ipython3

    len(ntp_servers[0])




.. parsed-literal::

    1



Iterating over the results is also possible.

.. code:: ipython3

    for ntp_server in ntp_servers:
        print(type(ntp_server))


.. parsed-literal::

    <class 'ciscoconfdict.CiscoConfLines'>
    <class 'ciscoconfdict.CiscoConfLines'>

