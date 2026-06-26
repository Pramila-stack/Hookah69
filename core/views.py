from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Reservation, Review, MenuItem
from .forms import ReservationForm


REVIEWS = [
    {'name': 'Alex Johnson', 'initials': 'AJ', 'text': "Absolutely incredible experience! The hookah flavors were unlike anything I've tried before. The ambience is just perfect for a night out.", 'likes': 24, 'date_label': '2 days ago'},
    {'name': 'Sarah Miller', 'initials': 'SM', 'text': "Best hookah lounge in Kathmandu! The staff is super friendly and the cocktails are amazing. Will definitely be coming back!", 'likes': 18, 'date_label': '1 week ago'},
    {'name': 'Raj Sharma', 'initials': 'RS', 'text': "The VIP lounge experience is totally worth it. Live music on weekends makes it even better. Highly recommend the mint-lemon flavor!", 'likes': 31, 'date_label': '3 days ago'},
    {'name': 'Emily Chen', 'initials': 'EC', 'text': "Such a vibe! The lighting, the music, the hookah — everything was on point. This has become our go-to spot every weekend.", 'likes': 15, 'date_label': '5 days ago'},
    {'name': 'Mike Wilson', 'initials': 'MW', 'text': "Five stars without question. The premium hookah setup and the signature cocktails are absolutely top-notch. Premium quality all the way.", 'likes': 42, 'date_label': '1 day ago'},
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


def menu(request):
    hookah_items = MenuItem.objects.filter(category='hookah')
    drink_items = MenuItem.objects.filter(category='drinks')
    food_items = MenuItem.objects.filter(category='food')
    return render(request, 'core/menu.html', {
        'hookah_items': hookah_items,
        'drink_items': drink_items,
        'food_items': food_items,
    })


def gallery(request):
    return render(request, 'core/gallery.html')


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
