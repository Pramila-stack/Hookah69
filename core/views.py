from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation, Review, MenuItem, GalleryImage
from .forms import ReservationForm


REVIEWS = [
    {'name': 'Alex Johnson', 'initials': 'AJ', 'text': "Absolutely incredible experience! The hookah flavors were unlike anything I've tried before. The ambience is just perfect for a night out.", 'likes': 24, 'date_label': '2 days ago'},
    {'name': 'Sarah Miller', 'initials': 'SM', 'text': "Best hookah lounge in Kathmandu! The staff is super friendly and the cocktails are amazing. Will definitely be coming back!", 'likes': 18, 'date_label': '1 week ago'},
    {'name': 'Raj Sharma', 'initials': 'RS', 'text': "The VIP lounge experience is totally worth it. Live music on weekends makes it even better. Highly recommend the mint-lemon flavor!", 'likes': 31, 'date_label': '3 days ago'},
    {'name': 'Emily Chen', 'initials': 'EC', 'text': "Such a vibe! The lighting, the music, the hookah — everything was on point. This has become our go-to spot every weekend.", 'likes': 15, 'date_label': '5 days ago'},
    {'name': 'Mike Wilson', 'initials': 'MW', 'text': "Five stars without question. The premium hookah setup and the signature cocktails are absolutely top-notch. Premium quality all the way.", 'likes': 42, 'date_label': '1 day ago'},
]

# ─── FULL MENU DATA ────────────────────────────────────────────────────────────

SMOKE_ITEMS = [
    {'name': '69 Premium Hookah', 'desc': 'Mint / Lady Killer / Blueberry / Paan', 'price': '750', 'icon': '🌿', 'badge': 'POPULAR'},
    {'name': 'Luxury Pot Hookah', 'desc': 'Al Fakhir Mint / Lady Killer', 'price': '1,111', 'icon': '🪄', 'badge': 'PREMIUM'},
    {'name': 'Cigarettes', 'desc': 'Per piece', 'price': '30/pcs', 'icon': '🚬', 'badge': ''},
]

MOCKTAIL_ITEMS = [
    {'name': 'Raspberry Paradise', 'desc': 'Raspberry purée, pineapple juice, coconut syrup, fresh cream & whipped cream', 'price': '450', 'icon': '🍓', 'badge': 'BESTSELLER', 'quote': 'Escape to tropical bliss with every sip'},
    {'name': 'Berry Bonanza', 'desc': 'Dried blueberries, cranberries, apple juice, vanilla syrup & zesty lime', 'price': '399', 'icon': '🫐', 'badge': '', 'quote': ''},
    {'name': 'Wild Cat Cooler', 'desc': 'Blueberry crush, sour mix & sparkling soda — electric blue beauty', 'price': '399', 'icon': '💙', 'badge': '', 'quote': 'No rules. Just blue.'},
    {'name': 'King Alfonso', 'desc': 'Mango nectar, lemon juice, grenadine, black salt, crushed pepper & chaat masala', 'price': '399', 'icon': '🥭', 'badge': '', 'quote': 'Long live the king of kick.'},
    {'name': 'Sunset Strip', 'desc': 'Orange juice, cranberry, lemon juice, apple chunks & orange dices', 'price': '399', 'icon': '🌅', 'badge': '', 'quote': 'Taste the twilight, sip the vibe.'},
]

COCKTAIL_ITEMS = [
    {'name': 'Titaura Martini', 'desc': 'Vodka, titaura syrup, lime juice & cranberry — sweet, sour & spicy', 'price': '749', 'icon': '🍸', 'badge': 'BESTSELLER', 'quote': 'Escape to tropical bliss with every sip'},
    {'name': 'Dream of Roses', 'desc': 'Botanical gin, triple sec, lime juice, cucumber syrup, rose & egg white foam', 'price': '749', 'icon': '🌹', 'badge': '', 'quote': ''},
    {'name': 'Cherry Kiss', 'desc': 'Vodka, peach schnapps, fresh lime juice, finished with plump cherries', 'price': '749', 'icon': '🍒', 'badge': '', 'quote': 'Poured with passion, sealed with a kiss.'},
    {'name': 'Litchi Blossom', 'desc': 'Velvety gin, litchi, lime juice, Blue Lagoon & Sprite top-up', 'price': '749', 'icon': '🌸', 'badge': '', 'quote': 'Sip into something blossomful.'},
    {'name': 'Refreshing Cucumber', 'desc': 'Premium vodka, pineapple juice, lime, cucumber syrup & Angostura bitters', 'price': '749', 'icon': '🥒', 'badge': '', 'quote': 'Where freshness flirts with fine spirits.'},
]

SPIRITS = [
    {'name': 'Old Durbar', 'price30': '199', 'price750': '4,499'},
    {'name': 'Black Chimney', 'price30': '219', 'price750': '4,999'},
    {'name': 'G&G', 'price30': '199', 'price750': '4,499'},
    {'name': 'Khukuri Rum', 'price30': '169', 'price750': '3,499'},
    {'name': '8848', 'price30': '169', 'price750': '3,499'},
    {'name': 'Snowman', 'price30': '169', 'price750': '3,499'},
    {'name': 'Black Lable', 'price30': '549', 'price750': '11,999'},
    {'name': 'Double Black', 'price30': '599', 'price750': '12,999'},
    {'name': 'Chivas', 'price30': '549', 'price750': '11,999'},
    {'name': 'Jameson', 'price30': '449', 'price750': '9,999'},
    {'name': 'Jack Daniels', 'price30': '499', 'price750': '10,999'},
]

WINES = [
    {'name': 'Bigmaster', 'glass': '319', 'bottle': '1,499'},
    {'name': 'Manang Valley', 'glass': '349', 'bottle': '1,699'},
    {'name': 'Jp Chenet', 'glass': '699', 'bottle': '3,399'},
    {'name': 'Porto', 'glass': '999', 'bottle': '4,799'},
]

SHOTS = [
    {'name': 'Taquila Gold', 'price': '599'},
    {'name': 'Taquila Silver', 'price': '599'},
    {'name': 'Jägermeister', 'price': '499'},
    {'name': 'Baileys', 'price': '599'},
]

BEERS = [
    {'name': 'Gorkha', 'price': '599'},
    {'name': 'Tuborg', 'price': '599'},
    {'name': 'Barasinghe', 'price': '599'},
]

CAFE_ESPRESSO = [
    {'name': 'Espresso', 'price': '149'},
    {'name': 'Espresso Afagato', 'price': '199'},
    {'name': 'Americano', 'price': '169'},
    {'name': 'Cafe Latte', 'price': '199'},
    {'name': 'Cafe Mocha', 'price': '199'},
    {'name': 'Honey Latte', 'price': '199'},
    {'name': 'Cappuccino', 'price': '199'},
]

CAFE_ICE_ESPRESSO = [
    {'name': 'Ice Latte', 'price': '219'},
    {'name': 'Ice Cappuccino', 'price': '219'},
    {'name': 'Ice Blended Mocha', 'price': '249'},
]

CAFE_ALTERNATIVES = [
    {'name': 'Hot Chocolate', 'price': '199'},
    {'name': 'Hot Lemon Honey', 'price': '149'},
    {'name': 'Hot Lemon with Ginger Honey', 'price': '179'},
    {'name': 'Fresh Mint Lemonade', 'price': '249'},
    {'name': 'Ice Lemonade', 'price': '199'},
    {'name': 'Peach Ice Tea', 'price': '169'},
    {'name': 'Apple Ice Tea', 'price': '169'},
    {'name': 'Lemon Ice Tea', 'price': '169'},
]

FRAPPES = [
    {'name': 'Blended Oreo Frappe', 'price': '349'},
    {'name': 'Blended Strawberry Frappe', 'price': '349'},
    {'name': 'Blended Mocha Frappe', 'price': '349'},
]

MILKSHAKES = [
    {'name': 'Chocolate Shake', 'price': '199'},
    {'name': 'Strawberry Shake', 'price': '199'},
    {'name': 'Oreo Shake', 'price': '219'},
    {'name': 'Vanilla Shake', 'price': '219'},
]

LASSI = [
    {'name': 'Plain Lassi', 'price': '169'},
    {'name': 'Sweet Lassi', 'price': '169'},
    {'name': 'Banana Lassi', 'price': '199'},
    {'name': 'Mix Fruit Lassi', 'price': '249'},
]

JUICES = [
    {'name': 'Watermelon', 'price': '219'},
    {'name': 'Apple', 'price': '249'},
    {'name': 'Carrots', 'price': '199'},
    {'name': 'ABC', 'price': '299'},
]

MATCHA = [
    {'name': 'Matcha Latte', 'price': '249'},
    {'name': 'Ice Matcha', 'price': '249'},
    {'name': 'Strawberry Matcha Latte', 'price': '299'},
    {'name': 'Blueberry Matcha Latte', 'price': '299'},
    {'name': 'Dirty Matcha', 'price': '299'},
    {'name': 'Matcha Lemonade', 'price': '249'},
    {'name': 'Matcha Shake', 'price': '299'},
]

TEA = [
    {'name': 'Green Tea', 'price': '99'},
    {'name': 'Milk Tea', 'price': '69'},
    {'name': 'Lemon Tea', 'price': '69'},
    {'name': 'Black Tea', 'price': '59'},
    {'name': 'Ginger Black Tea', 'price': '69'},
    {'name': 'Lemon Grass Black Tea', 'price': '99'},
    {'name': 'Lemon Grass Green Tea', 'price': '99'},
    {'name': 'Peach Tea', 'price': '119'},
]

FOOD_SALADS = [
    {'name': 'American Salad', 'price': '399'},
    {'name': 'Green Salad', 'price': '199'},
    {'name': 'Fruits Salad', 'price': '249'},
]

FOOD_GRAVY = [
    {'name': 'Chicken Gravy with Rice', 'price': '399'},
    {'name': 'Pork Gravy with Rice', 'price': '449'},
]

FOOD_RICE_BOWL = [
    {'name': 'Teriyaki Chicken Rice Bowl', 'price': '399'},
    {'name': 'Spicy Pork Rice Bowl', 'price': '399'},
]

FOOD_VEG_SNACKS = [
    {'name': 'Mustang Aalu', 'price': '249'},
    {'name': 'Paneer Chilly', 'price': '299'},
    {'name': 'Paneer Pakoda', 'price': '299'},
    {'name': 'French Fries', 'price': '169'},
    {'name': 'Peri Peri Fries', 'price': '199'},
    {'name': 'Chips Chilly', 'price': '199'},
    {'name': 'Wai-Wai Sadheko', 'price': '169'},
    {'name': 'Chatpate', 'price': '169'},
    {'name': 'Aalu Sadheko', 'price': '149'},
    {'name': 'Peanuts Sadheko', 'price': '169'},
    {'name': 'Golden Fried Mushroom', 'price': '299'},
    {'name': 'Spicy Sweet Corn', 'price': '299'},
]

FOOD_NONVEG_SNACKS = [
    {'name': 'Timur Chicken', 'price': '349'},
    {'name': 'Chicken Chilly', 'price': '299'},
    {'name': 'Chicken Nuggets', 'price': '249'},
    {'name': 'Chicken Sadheko', 'price': '269'},
    {'name': 'Sukuti Sadheko', 'price': '249'},
    {'name': 'Buff Chhoila', 'price': '229'},
    {'name': 'Chicken Chhoila', 'price': '229'},
    {'name': 'Suasage Fry', 'price': '199'},
    {'name': 'Garlic Chicken', 'price': '399'},
    {'name': 'Chicken 65', 'price': '299'},
    {'name': 'Paprika Chicken', 'price': '299'},
    {'name': 'Chicken Kurkure', 'price': '399'},
    {'name': 'Crispy Chicken', 'price': '399'},
    {'name': 'Chicken Leg Piece (2pcs)', 'price': '499'},
    {'name': 'Spicy Pork', 'price': '299'},
]

FOOD_SPECIAL = [
    {'name': 'Non-Veg Platter', 'price': '699'},
    {'name': 'MO:MO Platter', 'price': '449'},
    {'name': 'Long Crispy Potato', 'price': '249'},
    {'name': 'Shyabali (2pcs)', 'price': '299'},
]

FOOD_BURGER = [
    {'name': 'Veg Burger', 'price': '199'},
    {'name': 'Chicken Crispy Burger', 'price': '249'},
    {'name': 'Veg Sandwich', 'price': '199'},
    {'name': 'Chicken Sandwich', 'price': '299'},
    {'name': 'Club Sandwich', 'price': '349'},
]

FOOD_SIZZLER = [
    {'name': 'Chicken Sizzler', 'price': '449'},
    {'name': 'Sizzling Brownie', 'price': '299'},
]

FOOD_CHOWMIEN = [
    {'name': 'Veg', 'price': '169'},
    {'name': 'Chicken', 'price': '199'},
    {'name': 'Buff', 'price': '199'},
    {'name': 'Pork', 'price': '299'},
    {'name': 'Mix', 'price': '249'},
]

FOOD_PASTA = [
    {'name': 'Spaghetti Arrabbiata', 'price': '299'},
    {'name': 'Spaghetti Carbonara', 'price': '389'},
]

FOOD_PIZZA = [
    {'name': 'Margarita', 'price': '349 / 549'},
    {'name': 'Chicken', 'price': '399 / 599'},
    {'name': 'Mixed', 'price': '499 / 649'},
    {'name': 'Meat Lover', 'price': '599 / 799'},
    {'name': 'Cheesy Pineapple Berries', 'price': '399 / 699'},
]

FOOD_NOODLES = [
    {'name': 'Chicken Keema Noodles', 'price': '219'},
    {'name': 'Buff Keema Noodles', 'price': '219'},
    {'name': 'Buldak', 'price': '349'},
    {'name': 'Current', 'price': '149'},
]

FOOD_MOMO = [
    {'name': 'Veg', 'steam': '179', 'kothey': '199', 'jhol': '210', 'chilly': '240'},
    {'name': 'Chicken', 'steam': '199', 'kothey': '229', 'jhol': '239', 'chilly': '249'},
    {'name': 'Buff', 'steam': '199', 'kothey': '229', 'jhol': '239', 'chilly': '249'},
]


def index(request):
    return render(request, 'core/index.html', {'reviews': REVIEWS})


def reserve(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your reservation has been confirmed! We look forward to seeing you.')
            return redirect('reserve')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ReservationForm()
    return render(request, 'core/reserve.html', {'form': form})


def _db_or_fallback(tab, subcategory, fallback):
    """Return DB items as dicts if any exist, else return hardcoded fallback list."""
    qs = MenuItem.objects.filter(tab=tab, is_active=True)
    if subcategory:
        qs = qs.filter(subcategory=subcategory)
    if qs.exists():
        return [item.as_dict() for item in qs]
    return fallback


def menu(request):
    return render(request, 'core/menu.html', {
        'smoke_items':       _db_or_fallback('smoke',     '',              SMOKE_ITEMS),
        'mocktail_items':    _db_or_fallback('mocktails', '',              MOCKTAIL_ITEMS),
        'cocktail_items':    _db_or_fallback('cocktails', '',              COCKTAIL_ITEMS),
        'spirits':           _db_or_fallback('bar',       'spirits',       SPIRITS),
        'wines':             _db_or_fallback('bar',       'wine',          WINES),
        'shots':             _db_or_fallback('bar',       'shots',         SHOTS),
        'beers':             _db_or_fallback('bar',       'beers',         BEERS),
        'cafe_espresso':     _db_or_fallback('cafe',      'espresso',      CAFE_ESPRESSO),
        'cafe_ice_espresso': _db_or_fallback('cafe',      'ice_espresso',  CAFE_ICE_ESPRESSO),
        'cafe_alternatives': _db_or_fallback('cafe',      'alternatives',  CAFE_ALTERNATIVES),
        'frappes':           _db_or_fallback('cafe',      'frappes',       FRAPPES),
        'milkshakes':        _db_or_fallback('cafe',      'milkshakes',    MILKSHAKES),
        'lassi':             _db_or_fallback('cafe',      'lassi',         LASSI),
        'juices':            _db_or_fallback('cafe',      'juices',        JUICES),
        'matcha':            _db_or_fallback('cafe',      'matcha',        MATCHA),
        'tea':               _db_or_fallback('cafe',      'tea',           TEA),
        'food_salads':       _db_or_fallback('food',      'salads',        FOOD_SALADS),
        'food_gravy':        _db_or_fallback('food',      'gravy',         FOOD_GRAVY),
        'food_rice_bowl':    _db_or_fallback('food',      'rice_bowl',     FOOD_RICE_BOWL),
        'food_veg_snacks':   _db_or_fallback('food',      'veg_snacks',    FOOD_VEG_SNACKS),
        'food_nonveg_snacks':_db_or_fallback('food',      'nonveg_snacks', FOOD_NONVEG_SNACKS),
        'food_special':      _db_or_fallback('food',      'specials',      FOOD_SPECIAL),
        'food_burger':       _db_or_fallback('food',      'burgers',       FOOD_BURGER),
        'food_sizzler':      _db_or_fallback('food',      'sizzler',       FOOD_SIZZLER),
        'food_chowmien':     _db_or_fallback('food',      'chowmien',      FOOD_CHOWMIEN),
        'food_pasta':        _db_or_fallback('food',      'pasta',         FOOD_PASTA),
        'food_pizza':        _db_or_fallback('food',      'pizza',         FOOD_PIZZA),
        'food_noodles':      _db_or_fallback('food',      'noodles',       FOOD_NOODLES),
        'food_momo':         _db_or_fallback('food',      'momo',          FOOD_MOMO),
    })


_GALLERY_CATEGORY_KEYWORDS = {
    'lounge':  ['lounge', 'kounge', 'interior', 'vip', 'ambien', 'room', 'seat', 'sofa'],
    'hookah':  ['hookah', 'shisha', 'smoke', 'pipe', 'coal'],
    'drinks':  ['drink', 'cocktail', 'mocktail', 'juice', 'bar', 'glass', 'bottle', 'beer', 'wine'],
    'events':  ['event', 'party', 'birthday', 'celebrat', 'live', 'music', 'night', 'dj'],
    'food':    ['food', 'snack', 'pizza', 'momo', 'burger', 'pasta', 'plate', 'dish'],
    'cafe':    ['cafe', 'coffee', 'tea', 'latte', 'frappe', 'matcha', 'espresso'],
}
_GALLERY_EXTS = {'.jpg', '.jpeg', '.png', '.webp'}


def _gallery_category(filename):
    name = filename.lower()
    for cat, keywords in _GALLERY_CATEGORY_KEYWORDS.items():
        if any(kw in name for kw in keywords):
            return cat
    return 'lounge'


def _scan_gallery_folder():
    """Auto-read every image in media/gallery/ — no DB, no admin needed."""
    from pathlib import Path
    from django.conf import settings as _s
    folder = Path(_s.MEDIA_ROOT) / 'gallery'
    if not folder.exists():
        return []
    images = []
    for f in sorted(folder.iterdir()):
        if f.is_file() and f.suffix.lower() in _GALLERY_EXTS:
            images.append({
                'title':     f.stem.replace('_', ' ').replace('-', ' ').title(),
                'image_url': _s.MEDIA_URL + 'gallery/' + f.name,
                'category':  _gallery_category(f.name),
                'is_large':  f.name.lower().startswith('large_'),
            })
    return images


def gallery(request):
    # 1. DB images (added via admin) take priority
    db_images = GalleryImage.objects.filter(is_active=True)
    if db_images.exists():
        images = [
            {'title': img.title, 'image_url': img.src,
             'category': img.category, 'is_large': img.is_large}
            for img in db_images
        ]
        return render(request, 'core/gallery.html', {'images': images})

    # 2. Auto-scan media/gallery/ — just drop files in, they appear instantly
    scanned = _scan_gallery_folder()
    if scanned:
        return render(request, 'core/gallery.html', {'images': scanned})

    # 3. Nothing found — show empty state (no Unsplash placeholders)
    return render(request, 'core/gallery.html', {'images': []})


def team(request):
    return render(request, 'core/team.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            messages.success(request, "Thank you for reaching out! We'll get back to you shortly.")
        else:
            messages.error(request, 'Please fill in all required fields.')
        return redirect('contact')
    return render(request, 'core/contact.html')


def about(request):
    return render(request, 'core/about.html')
