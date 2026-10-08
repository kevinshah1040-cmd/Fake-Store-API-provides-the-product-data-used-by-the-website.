import requests

from django.shortcuts import render


# ================= HOME PAGE =================

def home(request):

    api_url = "https://dummyjson.com/products?limit=12"

    response = requests.get(api_url)

    data = response.json()

    products = data.get("products", [])

    return render(
        request,
        "home.html",
        {
            "products": products
        }
    )


# ================= PRODUCTS PAGE =================

def products(request):

    api_url = "https://dummyjson.com/products?limit=30"

    response = requests.get(api_url)

    data = response.json()

    products = data.get("products", [])

    return render(
        request,
        "products.html",
        {
            "products": products
        }
    )


# ================= CATEGORIES PAGE =================

def categories(request):

    category = request.GET.get("category")

    products = []

    if category:

        api_url = (
            f"https://dummyjson.com/products/category/{category}"
        )

        response = requests.get(api_url)

        data = response.json()

        products = data.get("products", [])


    return render(
        request,
        "categories.html",
        {
            "products": products,
            "selected_category": category
        }
    )


# ================= CONTACT PAGE =================

def contact(request):

    return render(
        request,
        "contact.html"
    )