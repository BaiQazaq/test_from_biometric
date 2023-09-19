from django.urls import path

from .views import PeopleView

urlpatterns = [
    path('', PeopleView.as_view()),
    path('people/', PeopleView.as_view()),
    path('people/<int:pk>/', PeopleView.as_view())

]