Usage
=====

The :meth:`sn74hcs137.driver.SN74HCS137.select` internally latches to carry out
selection smoothly.

Selection
---------

The selection and deselection examples are shown below.

.. code-block:: pycon

   >>> from time import sleep
   >>> from unittest.mock import MagicMock
   >>> from periphery import GPIO
   >>> from sn78hcs137 import SN74HCS137
   >>> latch_enable_gpio = GPIO('/dev/gpiochip0', 0, 'out', inverted=True)
   >>> strobe_input_gpio = GPIO('/dev/gpiochip0', 1, 'out', inverted=True)
   >>> address_select_0_gpio = GPIO('/dev/gpiochip0', 2, 'out', inverted=False)
   >>> address_select_1_gpio = GPIO('/dev/gpiochip0', 3, 'out', inverted=False)
   >>> address_select_2_gpio = GPIO('/dev/gpiochip0', 4, 'out', inverted=False)
   >>> sn78hcs137 = SN74HCS137(
   ...     latch_enable_gpio,
   ...     MagicMock(),
   ...     strobe_input_gpio,
   ...     address_select_0_gpio,
   ...     address_select_1_gpio,
   ...     address_select_2_gpio,
   ... )
   >>> sn78hcs137.select(SN74HCS137.Address.Y3)
   >>> sleep(1)
   >>> sn78hcs137.select(SN74HCS137.Address.Y0)
   >>> sleep(1)
   >>> sn78hcs137.deselect()

Latching
--------

The latching examples are shown below.

.. code-block:: pycon

   >>> from time import sleep
   >>> from unittest.mock import MagicMock
   >>> from periphery import GPIO
   >>> from sn78hcs137 import SN74HCS137
   >>> latch_enable_gpio = GPIO('/dev/gpiochip0', 0, 'out', inverted=True)
   >>> strobe_input_gpio = GPIO('/dev/gpiochip0', 1, 'out', inverted=True)
   >>> address_select_0_gpio = GPIO('/dev/gpiochip0', 2, 'out', inverted=False)
   >>> address_select_1_gpio = GPIO('/dev/gpiochip0', 3, 'out', inverted=False)
   >>> address_select_2_gpio = GPIO('/dev/gpiochip0', 4, 'out', inverted=False)
   >>> sn78hcs137 = SN74HCS137(
   ...     latch_enable_gpio,
   ...     MagicMock(),
   ...     strobe_input_gpio,
   ...     address_select_0_gpio,
   ...     address_select_1_gpio,
   ...     address_select_2_gpio,
   ... )
   >>> sn78hcs137.enable_latch()
   >>> sleep(1)
   >>> sn78hcs137.disable_latch()
