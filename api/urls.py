from django.urls import path, include

urlpatterns = [
    path('yasg/', include('api.yasg')),
    path('estate/', include( 'movie.main.endpoints')),
    path('accounts/', include('accounts.auth.endpoints'))
]
