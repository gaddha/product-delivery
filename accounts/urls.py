from django.urls import path
from . import views

urlpatterns = [

    # <editor-fold desc="registration">
    path('signup/',views.accountsUserCreationView.as_view(),name='sign_up'),
    # </editor-fold>

    path('update_profile/<int:pk>/',views.UpdateProfileView.as_view(), name='auth_update_profile'),

    path('detail-view/',views.accountProfileListView.as_view(),name='list_all_users'),

]