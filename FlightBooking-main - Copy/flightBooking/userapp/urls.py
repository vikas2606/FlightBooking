from django.urls import path,include
from userapp import views

urlpatterns = [
    
    #path('find_flights/', views.find_flights),
    #path('book_tickets/',views.save_reservation),
    #path('flights/<int:pk>',views.view_flight,name='flight-detail'),
    
    path('flights/',views.FlightList.as_view()),
    path('reservations/',views.save_reservation),
    path('flights/<str:pk>',views.FlightDetail.as_view()),
    

]
