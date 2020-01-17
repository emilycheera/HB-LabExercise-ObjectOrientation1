############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    cren = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yelwater = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yelwater.add_pairing('ice cream')
    all_melon_types.append(yelwater)


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_lookups = {}

    for melon in melon_types:
        melon_lookups[melon.code] = melon


    return melon_lookups
    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvest_field_number,
                 harvester_name):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field_number = harvest_field_number
        self.harvester_name = harvester_name

    def is_sellable(self, shape_rating, color_rating):   
        return self.shape_rating > 5 and self.color_rating > 5


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    harvested_melons = []

    melon_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melon_by_id['yw'], 8, 7, 2, 'Sheila')
    harvested_melons.append(melon_1)

    melon_2 = Melon(melon_by_id['yw'], 3, 4, 2, 'Sheila')
    harvested_melons.append(melon_2)

    melon_3 = Melon(melon_by_id['yw'], 9, 8, 3, 'Sheila')
    harvested_melons.append(melon_3)

    melon_4 = Melon(melon_by_id['cas'], 10, 6, 35, 'Sheila')
    harvested_melons.append(melon_4)

    melon_5 = Melon(melon_by_id['cren'], 8, 9, 35, 'Michael')
    harvested_melons.append(melon_5)

    melon_6 = Melon(melon_by_id['cren'], 8, 2, 35, 'Michael')
    harvested_melons.append(melon_6)

    melon_7 = Melon(melon_by_id['cren'], 2, 3, 4, 'Michael')
    harvested_melons.append(melon_7)

    melon_8 = Melon(melon_by_id['musk'], 6, 7, 4, 'Michael')
    harvested_melons.append(melon_8)

    melon_9 = Melon(melon_by_id['yw'], 7, 10, 3, 'Sheila')
    harvested_melons.append(melon_9)

    return harvested_melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    for melon in melons: 
        if melon.is_sellable(melon.shape_rating, melon.color_rating):
            sellable = '(CAN BE SOLD)'
        else:
            sellable = '(NOT SELLABLE)'
        print(f'Harvested by {melon.harvester_name} from Field {melon.harvest_field_number} {sellable}')
 