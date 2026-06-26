from django.db import models


class Reservation(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.date} {self.time}"


class Review(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=3)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    date_label = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.date_label}"


class MenuItem(models.Model):
    TAB_CHOICES = [
        ('smoke',     'Hookah / Smoke'),
        ('mocktails', 'Mocktails'),
        ('cocktails', 'Cocktails'),
        ('bar',       'Bar'),
        ('cafe',      'Café'),
        ('food',      'Food'),
    ]

    SUBCATEGORY_CHOICES = [
        # Bar sub-sections
        ('spirits',      'Spirits'),
        ('wine',         'Wine'),
        ('shots',        'Shots'),
        ('beers',        'Beer'),
        # Café sub-sections
        ('espresso',     'Espresso Based'),
        ('ice_espresso', 'Ice Espresso'),
        ('frappes',      'Frappes'),
        ('alternatives', 'Hot & Cold Alternatives'),
        ('milkshakes',   'Milkshakes'),
        ('lassi',        'Lassi'),
        ('matcha',       'Matcha'),
        ('juices',       'Fresh Juices'),
        ('tea',          'Tea'),
        # Food sub-sections
        ('salads',       'Salads'),
        ('gravy',        'Gravy with Rice'),
        ('rice_bowl',    'Rice Bowl'),
        ('veg_snacks',   'Veg Snacks'),
        ('nonveg_snacks','Non-Veg Snacks'),
        ('specials',     "Chef's Specials"),
        ('sizzler',      'Sizzler'),
        ('burgers',      'Burgers & Sandwiches'),
        ('chowmien',     'Chowmien'),
        ('noodles',      'Noodles'),
        ('pizza',        'Pizza'),
        ('pasta',        'Pasta'),
        ('momo',         'MO:MO'),
    ]

    BADGE_CHOICES = [
        ('', 'None'),
        ('POPULAR',    'Popular'),
        ('BESTSELLER', 'Bestseller'),
        ('PREMIUM',    'Premium'),
        ('NEW',        'New'),
        ('SPECIAL',    'Special'),
    ]

    tab         = models.CharField(max_length=20, choices=TAB_CHOICES, default='smoke')
    subcategory = models.CharField(max_length=20, choices=SUBCATEGORY_CHOICES, blank=True, default='',
                                   help_text='Required for Bar, Café, and Food items to place them in the right section.')
    name        = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    icon        = models.CharField(max_length=10, blank=True, default='',
                                   help_text='Emoji (e.g. 🍸) or leave blank.')
    badge       = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True, default='')
    quote       = models.CharField(max_length=200, blank=True, default='',
                                   help_text='Italic tagline shown under the name (mocktails / cocktails).')

    # Flexible pricing — use whichever columns apply to the item type:
    #   Hookah/Drinks/Café/simple food → price only
    #   Spirits → price = 30ml,  price2 = 750ml
    #   Wine    → price = Glass, price2 = Bottle
    #   Pizza   → price = Small, price2 = Large
    #   MO:MO   → price = Steam, price2 = Kothey, price3 = Jhol, price4 = Chilly
    price  = models.CharField(max_length=30, help_text='Main price (or 30ml / Glass / Steam / Small).')
    price2 = models.CharField(max_length=30, blank=True, default='',
                              help_text='Second price (750ml / Bottle / Kothey / Large).')
    price3 = models.CharField(max_length=30, blank=True, default='', help_text='Jhol price (MO:MO only).')
    price4 = models.CharField(max_length=30, blank=True, default='', help_text='Chilly price (MO:MO only).')

    sort_order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first.')
    is_active  = models.BooleanField(default=True, help_text='Uncheck to hide from menu without deleting.')

    class Meta:
        ordering = ['tab', 'subcategory', 'sort_order', 'name']

    def __str__(self):
        label = self.get_tab_display()
        if self.subcategory:
            label += f' › {self.get_subcategory_display()}'
        return f"{self.name} ({label})  Rs.{self.price}"

    def as_dict(self):  # noqa: keep for view usage
        return {
            'name':        self.name,
            'desc':        self.description,
            'icon':        self.icon,
            'badge':       self.badge,
            'quote':       self.quote,
            'price':       self.price,
            'price2':      self.price2,
            'price3':      self.price3,
            'price4':      self.price4,
            # bar/momo convenience aliases
            'price30':     self.price,
            'price750':    self.price2,
            'glass':       self.price,
            'bottle':      self.price2,
            'steam':       self.price,
            'kothey':      self.price2,
            'jhol':        self.price3,
            'chilly':      self.price4,
        }


class GalleryImage(models.Model):
    CATEGORY_CHOICES = [
        ('lounge',  'Lounge'),
        ('hookah',  'Hookah'),
        ('drinks',  'Drinks'),
        ('events',  'Events'),
        ('food',    'Food'),
        ('cafe',    'Café'),
    ]

    title      = models.CharField(max_length=150)
    image      = models.ImageField(
        upload_to='gallery/',
        blank=True, null=True,
        help_text='Upload an image from your computer.'
    )
    image_url  = models.URLField(
        max_length=500, blank=True, default='',
        help_text='Or paste an external URL. If both are set, the uploaded image takes priority.'
    )
    category   = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='lounge')
    is_large   = models.BooleanField(
        default=False,
        help_text='Makes this image span two columns in the grid (featured/wide layout).'
    )
    sort_order = models.PositiveIntegerField(default=0, help_text='Lower numbers appear first.')
    is_active  = models.BooleanField(default=True, help_text='Uncheck to hide from gallery without deleting.')

    class Meta:
        ordering = ['sort_order', 'id']

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    @property
    def src(self):
        """Returns the URL to display — uploaded file takes priority over external URL."""
        if self.image:
            return self.image.url
        return self.image_url
