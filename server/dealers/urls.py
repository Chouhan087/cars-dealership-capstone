from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("static/login.html", views.login_page, name="login_page"),
    path("api/login/", views.login_user, name="login"),
    path("api/logout/", views.logout_user, name="logout"),
    path("api/dealers/", views.dealers, name="dealers"),
    path("api/dealers/<int:dealer_id>/", views.dealer_by_id, name="dealer_by_id"),
    path("api/dealers/<int:dealer_id>/reviews/", views.dealer_reviews, name="dealer_reviews"),
    path("api/dealers/<int:dealer_id>/reviews/create/", views.create_review, name="create_review"),
    path("api/dealers/state/<str:state>/", views.dealers_by_state, name="dealers_by_state"),
    path("api/car-makes/", views.car_makes, name="car_makes"),
    path("api/analyze-review/", views.analyze_review, name="analyze_review"),

    # Browser pages used for the required screenshots
    path("dealers/state/<str:state>/", views.home, name="state_page"),
    path("dealers/<int:dealer_id>/", views.home, name="dealer_page"),
    path("dealers/<int:dealer_id>/review/", views.home, name="review_page"),
]
