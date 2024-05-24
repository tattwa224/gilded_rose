# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items
        self.strategies = {
            "Aged Brie": AgedBrieStrategy(),
            "Sulfuras, Hand of Ragnaros": SulfurasStrategy(),
            "Backstage passes to a TAFKAL80ETC concert": BackStagePassStrategy(),
            "Conjured Mana Cake": ConjuredStrategy(),
        }
        self.default_strategy = NormalStrategy()

    def update_quality(self):
        for item in self.items:
            strategy = self.strategies.get(item.name, self.default_strategy)
            strategy.update_quality(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalStrategy:
    def update_quality(self, item: Item):
        item.sell_in -= 1
        if item.quality > 0:
            item.quality -= 1
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2
        item.quality = max(item.quality, 0)

class AgedBrieStrategy:
    def update_quality(self, item: Item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1
        item.quality = min(item.quality, 50)

class SulfurasStrategy:
    def update_quality(self, item: Item):
        pass  # "Sulfuras" never decreases in quality or sell_in

class BackStagePassStrategy:
    def update_quality(self, item: Item):
        item.sell_in -= 1
        if item.quality < 50:
            item.quality += 1
            if item.sell_in < 10 and item.quality < 50:
                item.quality += 1
            if item.sell_in < 5 and item.quality < 50:
                item.quality += 1
        if item.sell_in < 0:
            item.quality = 0
        item.quality = min(item.quality, 50)

class ConjuredStrategy:
    def update_quality(self, item: Item):
        item.sell_in = item.sell_in - 1
        if item.quality > 0:
            item.quality -= 2
        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 2