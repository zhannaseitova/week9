from django.shortcuts import render

from django.http.response import JsonResponse

from api.models import Product, Category

def product_list(request):
    try:
        products = Product.objects.all()
        products_json = [product.to_json() for product in products]
        return JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({"error": "no products in the database"})


def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
        product_json = product.to_json()
        return JsonResponse(product_json, safe=False)
    except:
        return JsonResponse({"error": "No such product"})


def category(request, id):
    try:
        category = Category.objects.get(id=id)
        category_json = category.to_json()
        return JsonResponse(category_json, safe=False)
    except:
        return JsonResponse({"error": "no such category"})


def categories(request):
    try:
        categories = Category.objects.all()
        categories_json = [category.to_json() for category in categories]
        return JsonResponse(categories_json, safe=False)
    except:
        return JsonResponse({"error": "There are no categories"})


def products_by_category(request, id):
    try:
        product_list = Product.objects.filter(category=id)
        products_json = product_list.to_json()
        return JsonResponse(products_json, safe=False)
    except:
        return JsonResponse({"error": "No products in this category"})
