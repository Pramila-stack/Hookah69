from django.core.management.base import BaseCommand
from core.models import MenuItem


class Command(BaseCommand):
    help = 'Seed database with default menu items'

    def handle(self, *args, **kwargs):
        hookah = [
            ('Double Apple', 'hookah', 'Classic anise and apple blend — timeless and smooth', 450),
            ('Mint Lemon Ice', 'hookah', 'Cooling mint with fresh lemon on an ice base', 500),
            ('Blueberry Mint', 'hookah', 'Sweet blueberry balanced with fresh mint leaves', 500),
            ('Watermelon Ice', 'hookah', 'Juicy watermelon flavor with a cool icy finish', 480),
            ('Peach Mango', 'hookah', 'Tropical blend of ripe peach and mango', 500),
            ('Grape Berry', 'hookah', 'Rich grape mixed with mixed berry sweetness', 470),
        ]
        drinks = [
            ('Hookah69 Signature', 'drinks', 'House blend cocktail with local spirits and fresh herbs', 650),
            ('Mountain Mule', 'drinks', 'Ginger beer, vodka, lime, and Himalayan mint', 550),
            ('Jungle Juice', 'drinks', 'Tropical fruit punch with premium rum', 500),
            ('Premium Beers', 'drinks', 'Selection of local and imported craft beers', 350),
            ('Whiskey Selection', 'drinks', 'Single malt, blended Scotch, and bourbon options', 800),
            ('Mocktails', 'drinks', 'Refreshing non-alcoholic blends for every palate', 350),
        ]
        food = [
            ('Mezze Platter', 'food', 'Hummus, pita, olives, falafel, and seasonal dips', 750),
            ('Crispy Calamari', 'food', 'Golden fried squid with lemon aioli dipping sauce', 600),
            ('Chicken Wings', 'food', 'Glazed with our secret house sauce, served with ranch', 650),
            ('Truffle Fries', 'food', 'Crispy fries with truffle oil, parmesan, and fresh herbs', 450),
            ('Sliders Board', 'food', 'Mini beef and chicken sliders with gourmet toppings', 850),
            ('Bruschetta', 'food', 'Toasted sourdough with fresh tomato, basil, and mozzarella', 400),
        ]

        created = 0
        for name, cat, desc, price in hookah + drinks + food:
            _, c = MenuItem.objects.get_or_create(
                name=name, category=cat,
                defaults={'description': desc, 'price': price}
            )
            if c:
                created += 1

        self.stdout.write(self.style.SUCCESS(f'Seeded {created} menu items.'))
