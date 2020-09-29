from django.urls import path
from .views import *

urlpatterns = [
    #to show in browser type 127.0.0... url and then /api/v1/boards/ and then type action what you want to perform
    #like board_list/ or board_create etc.
    path('board_list/', BoardList.as_view()),
    path('board_create/', BoardCreate.as_view()),
    path("board/<int:pk>/", BoardRUD.as_view()),
    path('list/filter/board/<int:board_id>/', BoardFilter.as_view()),
]