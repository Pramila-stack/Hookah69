"""
Usage:
    python manage.py seed_gallery

Drop any image files into  media/gallery/  then run this command.
It scans the folder, guesses the category from the filename, and
creates a GalleryImage record for every new file it finds.
Already-registered files are skipped (safe to re-run).

Category auto-detection (first match wins):
  lounge  → filename contains: lounge, kounge, interior, vip, ambien, room, seat
  hookah  → filename contains: hookah, shisha, smoke, pipe, coal
  drinks  → filename contains: drink, cocktail, mocktail, juice, bar, glass, bottle
  events  → filename contains: event, party, birthday, celebrat, live, music, night
  food    → filename contains: food, snack, pizza, momo, burger, pasta, plate, dish
  cafe    → filename contains: cafe, coffee, tea, latte, frappe, matcha, espresso
  (default = lounge)

To mark an image as "large" (spans two columns in the grid), start the
filename with  large_  e.g.  large_lounge1.jpg
"""

import os
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from core.models import GalleryImage

# ── Category keyword map ────────────────────────────────────────────────────
CATEGORY_KEYWORDS = {
    'lounge':  ['lounge', 'kounge', 'interior', 'vip', 'ambien', 'room', 'seat', 'sofa'],
    'hookah':  ['hookah', 'shisha', 'smoke', 'pipe', 'coal', 'flavour'],
    'drinks':  ['drink', 'cocktail', 'mocktail', 'juice', 'bar', 'glass', 'bottle', 'beer', 'wine'],
    'events':  ['event', 'party', 'birthday', 'celebrat', 'live', 'music', 'night', 'dj'],
    'food':    ['food', 'snack', 'pizza', 'momo', 'burger', 'pasta', 'plate', 'dish', 'meal'],
    'cafe':    ['cafe', 'coffee', 'tea', 'latte', 'frappe', 'matcha', 'espresso', 'cappuccino'],
}

SUPPORTED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}


def guess_category(filename: str) -> str:
    name = filename.lower()
    for category, keywords in CATEGORY_KEYWORDS.items():
        if any(kw in name for kw in keywords):
            return category
    return 'lounge'


def friendly_title(filename: str) -> str:
    stem = Path(filename).stem
    stem = stem.removeprefix('large_')
    return stem.replace('_', ' ').replace('-', ' ').title()


class Command(BaseCommand):
    help = 'Scan media/gallery/ and register all images into the GalleryImage table.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Delete all existing GalleryImage records before seeding.',
        )

    def handle(self, *args, **options):
        gallery_dir = Path(settings.MEDIA_ROOT) / 'gallery'

        if not gallery_dir.exists():
            self.stdout.write(self.style.ERROR(
                f'Gallery folder not found: {gallery_dir}\n'
                'Create it and place your images inside, then re-run.'
            ))
            return

        if options['clear']:
            deleted, _ = GalleryImage.objects.all().delete()
            self.stdout.write(self.style.WARNING(f'Cleared {deleted} existing records.'))

        image_files = sorted([
            f for f in gallery_dir.iterdir()
            if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
        ])

        if not image_files:
            self.stdout.write(self.style.WARNING(
                f'No image files found in {gallery_dir}.\n'
                'Place .jpg / .jpeg / .png / .webp files there and re-run.'
            ))
            return

        created = 0
        skipped = 0

        for idx, f in enumerate(image_files, start=1):
            # Relative path stored in the ImageField  (e.g. "gallery/lounge.jpeg")
            relative_path = f'gallery/{f.name}'

            if GalleryImage.objects.filter(image=relative_path).exists():
                self.stdout.write(f'  skip  {f.name}  (already registered)')
                skipped += 1
                continue

            is_large   = f.name.lower().startswith('large_')
            category   = guess_category(f.name)
            title      = friendly_title(f.name)

            GalleryImage.objects.create(
                title      = title,
                image      = relative_path,
                category   = category,
                is_large   = is_large,
                sort_order = idx,
                is_active  = True,
            )
            self.stdout.write(
                self.style.SUCCESS(f'  added  {f.name}  →  [{category}]  large={is_large}')
            )
            created += 1

        self.stdout.write(self.style.SUCCESS(
            f'\nDone. {created} image(s) added, {skipped} skipped.'
        ))
        self.stdout.write(
            '\nTip: prefix a filename with  large_  to make it span two grid columns.\n'
            'Tip: run with  --clear  to wipe all records and re-seed from scratch.'
        )
