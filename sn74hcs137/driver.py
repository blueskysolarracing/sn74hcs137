from dataclasses import dataclass
from enum import IntEnum
from typing import ClassVar

from periphery import GPIO


@dataclass
class SN74HCS137:
    """A Python driver for Texas instruments SN74HCS137 3- to 8-Line
    Decoder/Demultiplexer with Address Latches and SchmittTrigger Inputs
    """

    class Address(IntEnum):
        """The enum class for addresses."""

        Y0: int = 0
        """Output 0."""
        Y1: int = 1
        """Output 1."""
        Y2: int = 2
        """Output 2."""
        Y3: int = 3
        """Output 3."""
        Y4: int = 4
        """Output 4."""
        Y5: int = 5
        """Output 5."""
        Y6: int = 6
        """Output 6."""
        Y7: int = 7
        """Output 7."""

    ADDRESS_SELECT_0_GPIO_DIRECTION: ClassVar[str] = 'out'
    """The address select 0 GPIO direction."""
    ADDRESS_SELECT_1_GPIO_DIRECTION: ClassVar[str] = 'out'
    """The address select 1 GPIO direction."""
    ADDRESS_SELECT_2_GPIO_DIRECTION: ClassVar[str] = 'out'
    """The address select 2 GPIO direction."""
    LATCH_ENABLE_GPIO_DIRECTION: ClassVar[str] = 'out'
    """The latch enable GPIO direction."""
    ADDRESS_SELECT_0_GPIO_INVERTED: ClassVar[bool] = False
    """The address select 0 GPIO inverted status."""
    ADDRESS_SELECT_1_GPIO_INVERTED: ClassVar[bool] = False
    """The address select 1 GPIO inverted status."""
    ADDRESS_SELECT_2_GPIO_INVERTED: ClassVar[bool] = False
    """The address select 2 GPIO inverted status."""
    LATCH_ENABLE_GPIO_INVERTED: ClassVar[bool] = True
    """The latch enable GPIO inverted status."""
    address_select_0_gpio: GPIO
    """The address select 0 GPIO."""
    address_select_1_gpio: GPIO
    """The address select 1 GPIO."""
    address_select_2_gpio: GPIO
    """The address select 2 GPIO."""
    latch_enable_gpio: GPIO
    """The latch enable 2 GPIO."""

    def __post_init__(self) -> None:
        if (
                (
                    self.address_select_0_gpio.direction
                    != self.ADDRESS_SELECT_0_GPIO_DIRECTION
                )
                or (
                    self.address_select_1_gpio.direction
                    != self.ADDRESS_SELECT_1_GPIO_DIRECTION
                )
                or (
                    self.address_select_2_gpio.direction
                    != self.ADDRESS_SELECT_2_GPIO_DIRECTION
                )
                or (
                    self.latch_enable_gpio.direction
                    != self.LATCH_ENABLE_GPIO_DIRECTION
                )
        ):
            raise ValueError('all GPIO not output')
        elif (
                (
                    self.address_select_0_gpio.inverted
                    != self.ADDRESS_SELECT_0_GPIO_INVERTED
                )
                or (
                    self.address_select_1_gpio.inverted
                    != self.ADDRESS_SELECT_1_GPIO_INVERTED
                )
                or (
                    self.address_select_2_gpio.inverted
                    != self.ADDRESS_SELECT_2_GPIO_INVERTED
                )
        ):
            raise ValueError('address selects not active high')
        elif (
            self.latch_enable_gpio.inverted != self.LATCH_ENABLE_GPIO_INVERTED
        ):
            raise ValueError('latch enable GPIO not active low')

    def enable(self) -> None:
        """Enable the line decoder.

        :return: ``None``.
        """
        self.latch_enable_gpio.write(True)

    def disable(self) -> None:
        """Disable the line decoder.

        :return: ``None``.
        """
        self.latch_enable_gpio.write(False)

    def select(self, address: Address) -> None:
        """Select the address.

        :param: The selected address.
        :return: ``None``.
        """
        self.address_select_0_gpio.write(bool(address & (1 << 0)))
        self.address_select_1_gpio.write(bool(address & (1 << 1)))
        self.address_select_2_gpio.write(bool(address & (1 << 2)))
