from collections import Counter

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import UserPreferencesForm
from .models import Product, UserPreferences


@login_required
def update_preferences(request):
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST, instance=request.user.userpreferences)
        if form.is_valid():
            form.save()
            response = render(request, 'preferences/preferences_updated.html')
            response.set_cookie('preferred_categories', form.cleaned_data['preferred_categories'])
            response.set_cookie('viewed_products', form.cleaned_data['viewed_products'])
            response.set_cookie('purchased_items', form.cleaned_data['purchased_items'])
            return response
    else:
        form = UserPreferencesForm(instance=request.user.userpreferences)
    return render(request, 'preferences/update_preferences.html', {'form': form})

def get_recommendations(request):
    # Retrieve user preferences from cookies
    preferred_categories = request.COOKIES.get('preferred_categories', [])
    viewed_products = request.COOKIES.get('viewed_products', [])
    purchased_items = request.COOKIES.get('purchased_items', [])

    # Get all products from the database
    all_products = Product.objects.all()

    # Initialize a Counter to store product scores
    product_scores = Counter()

    # Calculate scores for each product
    for product in all_products:
        if product.category in preferred_categories:
            product_scores[product] += 3  # Weight for preferred category
        if product in viewed_products:
            product_scores[product] += 2  # Weight for viewed product
        if product in purchased_items:
            product_scores[product] += 1  # Weight for purchased item

    # Get the top 10 products as recommendations
    recommended_products = product_scores.most_common(10)

    return render(request, 'preferences/recommendations.html', {'recommendations': recommended_products})