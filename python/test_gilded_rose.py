# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_quality_never_negative((self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, app.items[0].quality)

    def test_sulfuras_could_not_be_sold():
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(10, app.items[0].sellIn)

    def test_sulfuras_could_not_decrease_quality():
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(10, app.items[0].quality)
    
    def test_quality_could_not_be_more_than_fifty():
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(50, app.items[0].quality)

    def test_item_with_date_passed_quality_decrease_by_twice():
        items = [Item("foo", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(38, app.items[0].quality)
    
    def test_aged_brie_increase_quality_when_it_gets_older():
        items = [Item("Aged Brie", 1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(41, app.items[0].quality)
    
    def test_aged_brie_increase_by_two_quality_when_date_passed():
        items = [Item("Aged Brie", -1, 40))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(42, app.items[0].quality)

    def test_aged_brie_increase_by_two_quality_when_date_passed_and_not_more_than_fifty():
        items = [Item("Aged Brie", -1, 50))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(50, app.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_two_when_sellin_less_than_ten():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(42, app.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_two_when_sellin_less_than_six():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 40))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(42, app.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_three_when_sellin_less_than_five():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 40))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(43, app.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_two_when_sellin_less_than_six_and_not_more_than_fifty():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 49))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(50, app.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_three_when_sellin_less_than_five_and_not_more_than_fifty():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(50, app.items[0].quality)

    def test_backstage_passes_quality_drops_to_zero_after_concert():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(0, app.items[0].quality)

    def test_backstage_passes_quality_increase_quality_by_one_when_date_is_more_than_10():
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 40))]
        gilded_rose = GildedRose(items)
        gilded_rose.updateQuality()
        self.assertEquals(41, app.items[0].quality)
        
if __name__ == '__main__':
    unittest.main()
