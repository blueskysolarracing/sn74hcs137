==========
SN74HCS137
==========

SN74HCS137 is a Python driver for Texas instruments SN74HCS137 3- to 8-Line
Decoder/Demultiplexer with Address Latches and SchmittTrigger Inputs.

Features
--------

- High-level hardware usage.
- Low-level hardware usage.

Installation
------------

.. code-block:: bash

   pip install sn78hcs137

Usage
-----

Below shows a sample usage of SN74HCS137.

.. code-block:: python

   from time import sleep
   from unittest.mock import MagicMock

   from periphery import GPIO
   from sn78hcs137 import SN74HCS137
   
   latch_enable_gpio = GPIO('/dev/gpiochip0', 0, 'out', inverted=True)
   strobe_input_gpio = GPIO('/dev/gpiochip0', 1, 'out', inverted=True)
   address_select_0_gpio = GPIO('/dev/gpiochip0', 2, 'out', inverted=False)
   address_select_1_gpio = GPIO('/dev/gpiochip0', 3, 'out', inverted=False)
   address_select_2_gpio = GPIO('/dev/gpiochip0', 4, 'out', inverted=False)
   sn78hcs137 = SN74HCS137(
       latch_enable_gpio,
       MagicMock(),
       strobe_input_gpio,
       address_select_0_gpio,
       address_select_1_gpio,
       address_select_2_gpio,
   )

   sn78hcs137.select(SN74HCS137.Address.Y3)
   sleep(1)
   sn78hcs137.deselect()

Testing and Validation
----------------------

SN74HCS137 has extensive test coverage, passes mypy static type checking with
strict parameter, and has been validated through extensive use in real-life
scenarios.

Contributing
------------

Contributions are welcome! Please read our Contributing Guide for more
information.

License
-------

SN74HCS137 is distributed under the MIT license.
