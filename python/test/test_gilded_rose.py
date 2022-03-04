# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from Item import *


class GildedRoseTest(unittest.TestCase):
    def test_quality_never_negative(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_sulfuras_could_not_be_sold(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, gilded_rose.items[0].sell_in)

    def test_sulfuras_could_not_decrease_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(10, gilded_rose.items[0].quality)
    
    def test_quality_could_not_be_more_than_fifty(self):
        items = [AgedBrieItem("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_item_with_date_passed_quality_decrease_by_twice(self):
        items = [Item("foo", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(38, gilded_rose.items[0].quality)
    
    def test_aged_brie_increase_quality_when_it_gets_older(self):
        items = [AgedBrieItem("Aged Brie", 1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, gilded_rose.items[0].quality)
    
    def test_aged_brie_increase_by_two_quality_when_date_passed(self):
        items = [AgedBrieItem("Aged Brie", -1, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, gilded_rose.items[0].quality)

    def test_aged_brie_increase_by_two_quality_when_date_passed_and_not_more_than_fifty(self):
        items = [AgedBrieItem("Aged Brie", -1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_two_when_sellin_less_than_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, gilded_rose.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_two_when_sellin_less_than_six(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(42, gilded_rose.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_three_when_sellin_less_than_five(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(43, gilded_rose.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_two_when_sellin_less_than_six_and_not_more_than_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 6, 49)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)
    
    def test_backstage_passes_increase_quality_by_three_when_sellin_less_than_five_and_not_more_than_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 48)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50, gilded_rose.items[0].quality)

    def test_backstage_passes_quality_drops_to_zero_after_concert(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, gilded_rose.items[0].quality)

    def test_backstage_passes_quality_increase_quality_by_one_when_date_is_more_than_10(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 40)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(41, gilded_rose.items[0].quality)
        
if __name__ == '__main__':
    unittest.main()
