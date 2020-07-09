from django.urls import path
from entrenaminto_sebastian.telefonera_app.views import telefonera

app_name = "telefonera_app"

urlpatterns = [
    path('', telefonera.TelefonoListView.as_view(), name='telefonera-list'),
    path('create/', telefonera.TelefonoCreateView.as_view(), name='telefonera-create'),
    path('detail/<int:pk>', telefonera.TelefonoDetailView.as_view(), name='telefonera-detail'),
    path('update/<int:pk>', telefonera.TelefonoUpdateView.as_view(), name='telefonera-update'),
    path('delete/<int:pk>', telefonera.TelefonoDeleteView.as_view(),name='telefonera-delete'),
]