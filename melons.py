"""This file should have our melon-type classes in it."""

class WatermelonOrder:
    species = "Watermelon"
    color = "green"
    imported = False
    shape = "natural"
    seasons = ["Fall", "Summer"]

    def get_price(self, qty):
        if qty >= 3:
            return float(((qty * 5) * .75))
        elif qty < 3:
            return float(qty * 5)

class CantaloupeOrder:
    species = "Cantaloupe"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        if qty >= 5:
            return float(((qty * 5) * .5))
        elif qty < 5:
            return float(qty * 5)


class CasabaOrder:
    species = "Casaba"
    color = "green"
    imported = True
    shape = "natural"
    seasons = ["Spring", "Summer", "Fall", "Winter"]

    def get_price(self, qty):
        return ((qty * 6) * 1.5)

class HornedMelonOrder:
    species = "Horned Melon"
    color = "yellow"
    imported = True
    shape = "natural"
    seasons = ["Summer"]
    
    def get_price(self, qty):
        return (qty * 5 * 1.5)

class XiguaOrder:
    species = "Xiqua"
    color = "black"
    imported = True
    shape = "square"
    seasons = ["Summer"]

    def get_price(self, qty):
        return qty*10

class OgenOrder:
    species = "Ogen"
    color = "tan"
    imported = False
    shape = "natural"
    seasons = ["Spring", "Summer"]

    def get_price(self, qty):
        return ((qty * 6) * 1.5)