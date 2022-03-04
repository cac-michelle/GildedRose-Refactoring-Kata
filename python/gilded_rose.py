# -*- coding: utf-8 -*-

from inspect import _void
from Item import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                return
            if item.name == "Aged Brie":
                item.update_quality()
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                item.update_quality()
            else:
                item.sell_in = item.sell_in - 1
                item.decrease_quality()
                if item.sell_in < 0:
                    item.decrease_quality()


