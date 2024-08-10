from django.urls import path

from expense import views

urlpatterns = [
    path("category/", views.CategoryListCreateView.as_view()),
    path("category/<int:id>/", views.CategoryRetrieveView.as_view()),

    path("expense/", views.ExpenseListCreateView.as_view()),
    path("expense/<int:id>/", views.ExpenseRetrieveView.as_view()),
]