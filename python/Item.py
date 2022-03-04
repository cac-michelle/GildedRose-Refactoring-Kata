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