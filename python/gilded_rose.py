# -*- coding: utf-8 -*-

from inspect import _void


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
                item.sell_in = item.sell_in - 1
                item.increase_quality()
                if item.sell_in < 10:
                    item.increase_quality()
                    if item.sell_in < 5:
                        item.increase_quality()
                if item.sell_in < 0:
                    item.quality = 0
            else:
                item.sell_in = item.sell_in - 1
                item.decrease_quality()
                if item.sell_in < 0:
                    item.decrease_quality()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
    
    def decrease_quality(self):
        if self.quality > 0:
            self.quality = self.quality - 1

    def increase_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
    
    def update_quality(self):
        print("update quality")

class AgedBrieItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_quality(self):
        self.sell_in = self.sell_in - 1
        super().increase_quality()
        if self.sell_in < 0:
            super().increase_quality()