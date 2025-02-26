from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="engineer_index"),
    path('accept/<int:id>', accept, name="engineer_accept"),
    path('reject/<int:id>', reject, name="engineer_reject"),
    path('labour/', manage_labour, name="engineer_manage_labour"),
    path('labour/add', add_labour, name="engineer_add_labour"),
    path('labour/remove/<int:id>', delete_labour, name="engineer_delete_labour"),
    path('projects/', accepted_project, name='engineer_accepted_project'),
    path('assign/projects/equipments/<int:id>', assigne_equipments, name="engineer_assigne_equipments"),
    path('assign/projects/labour/<int:id>', assigne_labours, name="engineer_assigne_labours"),
    path('assign/projects/project/remove/<int:id>', delete_assigne_equipments, name="engineer_delete_assigne_equipments"),
    path('assign/projects/labour/remove/<int:id>', delete_assigne_labours, name="engineer_delete_assigne_labours"),
    path('design/', house_designs, name='engineer_house_designs'),
]