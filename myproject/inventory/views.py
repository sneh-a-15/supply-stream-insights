from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app1.models import UserPreference, UserProduct
from django.http import JsonResponse
import requests, random
import json

def fetch_books_media(api_url):
    products = []
    total_books = 0
    max_results = 30
    start_index = 0

    while total_books < 100:  # Fetch up to 100 books
        paginated_url = f'{api_url}&startIndex={start_index}'
        response = requests.get(paginated_url)
        response.raise_for_status()
        data = response.json()

        fetched_books = data.get('items', [])
        for item in fetched_books:
            volume_info = item.get('volumeInfo', {})
            products.append({
                'title': volume_info.get('title', 'No title available'),
                'price': random.randint(400, 1000),
                'image': volume_info.get('imageLinks', {}).get('thumbnail', '')
            })

        total_books += len(fetched_books)
        start_index += max_results

        if len(fetched_books) < max_results:
            break

    return products

def fetch_food_items(api_url):
    products = []
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    for item in data.get('products', []):
        products.append({
            'title': item.get('title', 'No title available'),
            'price': random.randint(400, 1000),
            'image': item.get('image', '')
        })
    
    return products

def fetch_products(api_url):
    products = []
    response = requests.get(api_url)
    response.raise_for_status()
    data = response.json()

    items = data.get('search_results', [{}])[0].get('item', [])
    
    for item in items:
        products.append({
            'title': item.get('title', 'No title available'),
            'price': item.get('current_price', 'No price available'),
            'image': item.get('thumbnail', '')
        })
    print(products)
    return products

@login_required
def product_list(request):
    try:
        user_preferences = UserPreference.objects.filter(user=request.user)
        if user_preferences.exists():
            user_preference = user_preferences.latest('id')
            selected_category = user_preference.category
        else:
            return render(request, 'inventory/no_preferences.html')
    except UserPreference.DoesNotExist:
        return render(request, 'inventory/no_preferences.html')

    # API Endpoints for each category
    api_endpoints = {
        'Clothing & Apparel': 'https://api.ecommerceapi.io/walmart_search?api_key=66e00017a8ec8d83dd78d4ae&url=https://www.walmart.com/search?q=clothing',
        'Electronics & Gadgets': 'https://api.ecommerceapi.io/walmart_search?api_key=66e00017a8ec8d83dd78d4ae&url=https://www.walmart.com/search?q=electronics', 
        'Food Items': 'https://api.spoonacular.com/food/products/search?query=a&offset=0&number=30&apiKey=e6351a982f264e1daf124bc8a9d6e074',
        'Home & Kitchen': 'https://api.ecommerceapi.io/walmart_search?api_key=66e00017a8ec8d83dd78d4ae&url=https://www.walmart.com/search?q=kitchen',
        'Books & Media': 'https://www.googleapis.com/books/v1/volumes?q=engineering&maxResults=40',
        'Sports & Outdoor': 'https://api.ecommerceapi.io/walmart_search?api_key=66e00017a8ec8d83dd78d4ae&url=https://www.walmart.com/search?q=sports+equipment',
    }

    if selected_category in api_endpoints:
        api_url = api_endpoints[selected_category]
        if selected_category == 'Books & Media':
            products = fetch_books_media(api_url)
        elif selected_category == 'Food Items':
            products = fetch_food_items(api_url)
        else:
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            products = fetch_products(api_url) 
    else:
        return render(request, 'inventory/no_products_found.html', {'message': 'No products found for the selected category.'})

    UserProduct.objects.filter(user=request.user).delete()  # Clear previous entries
    for product in products:
        name = product.get('title', 'No title available')
        price = random.randint(400, 1000)
        stock_level = random.randint(100, 1000)
        image_url = product.get('image', '')
        UserProduct.objects.create(
            user=request.user, 
            product_name=name, 
            price=price, 
            stock_level=stock_level, 
            image_url=image_url
        )

    user_products = UserProduct.objects.filter(user=request.user)

    return render(request, 'inventory/product_list.html', {'products': user_products})
