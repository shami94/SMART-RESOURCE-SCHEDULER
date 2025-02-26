from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='custome_index'),
    path('house/', housedesigns, name='custome_housedesigns'),
    path('house/<int:id>', housedesignsdetails, name='custome_housedesignsdetails'),

    path('booknow/<int:id>', booknow, name='custome_booknow'),
    path('orders/', my_orders, name='custome_my_orders'),
    path('orders/delete/<int:id>', delete_order, name='custome_delete_order'),
    path('project/', manage_project, name='custome_manage_project'),
    path('project/create/', add_project, name='custome_add_project'),
    path('project/edit/<int:id>', edit_project, name='custome_edit_project'),
    path('project/remove/<int:id>', delete_project, name='custome_delete_project'),
    path('complaint/', add_compalints, name='custome_add_compalints'),

]