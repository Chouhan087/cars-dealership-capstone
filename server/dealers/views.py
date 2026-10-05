import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Dealer, Review, CarMake

def home(request, state=None, dealer_id=None):
    return render(request, "index.html")

def login_page(request):
    return render(request, "login.html")

@csrf_exempt
def login_user(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    username = data.get("username", "")
    password = data.get("password", "")
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({"error": "Invalid credentials"}, status=401)
    login(request, user)
    return JsonResponse({"message": "Login successful", "username": user.username})

@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({"message": "Logout successful"})

def dealers(request):
    return JsonResponse({"dealers": list(Dealer.objects.values(
        "id", "name", "city", "state", "address", "phone"
    ))})

def dealer_by_id(request, dealer_id):
    try:
        d = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
        return JsonResponse({"error": "Dealer not found"}, status=404)
    return JsonResponse({
        "id": d.id, "name": d.name, "city": d.city,
        "state": d.state, "address": d.address, "phone": d.phone
    })

def dealer_reviews(request, dealer_id):
    reviews = Review.objects.filter(dealer_id=dealer_id).values(
        "id", "username", "text", "sentiment", "created_at"
    )
    return JsonResponse({"reviews": list(reviews)})

def dealers_by_state(request, state):
    qs = Dealer.objects.filter(state__iexact=state)
    return JsonResponse({"dealers": list(qs.values(
        "id", "name", "city", "state", "address", "phone"
    ))})

def car_makes(request):
    result = []
    for make in CarMake.objects.all():
        models = list(make.models.values_list("name", flat=True)) if hasattr(make, "models") else []
        result.append({"make": make.make, "models": models})
    return JsonResponse({"car_makes": result})

@csrf_exempt
def analyze_review(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    review = data.get("review", "")
    positive_words = ["fantastic","excellent","great","good","amazing","wonderful","love"]
    sentiment = "positive" if any(w in review.lower() for w in positive_words) else "neutral"
    return JsonResponse({"review": review, "sentiment": sentiment})

@csrf_exempt
def create_review(request, dealer_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    text = data.get("text", "").strip()
    if not text:
        return JsonResponse({"error": "Review text required"}, status=400)
    sentiment = "positive" if any(
        w in text.lower() for w in ["fantastic","excellent","great","good","amazing","wonderful","love"]
    ) else "neutral"
    review = Review.objects.create(
        dealer_id=dealer_id,
        username=request.user.username,
        text=text,
        sentiment=sentiment
    )
    return JsonResponse({"message": "Review added successfully", "id": review.id})
