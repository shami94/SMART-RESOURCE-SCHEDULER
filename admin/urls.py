from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='admin_index'),
    path('equipment/', manage_equipment, name='admin_manage_equipment'),
    path('equipment/add/', add_equipment, name='admin_add_equipment'),
    path('equipment/edit/<int:id>', edit_equipment, name='admin_edit_equipment'),
    path('equipment/remove/<int:id>', delete_equipment, name='admin_delete_equipment'),
    path('equipment/orders/', equipment_orders, name='admin_equipment_orders'),
    path('equipment/orders/approve/<int:id>', equipment_orders_approve, name='admin_equipment_orders_approve'),
    path('projects/new/', new_project, name='admin_new_project'),
    path('projects/assigned/', assigned_project, name='admin_assigned_project'),
    path('projects/assign/<int:id>', assign_engineer, name='admin_assign_engineer'),
    path('engineer/manage/', manage_site_engineer, name='admin_manage_site_engineer'),
    path('engineer/delete/<int:id>', delete_engineer, name='admin_delete_engineer'),
    path('engineer/change_status/<int:id>', change_status, name='admin_change_status'),
    path('house_design/', manage_house_design, name='admin_manage_house_design'),
    path('house_design/add/', add_house_design, name='admin_add_house_design'),
    path('house_design/edit/<int:id>', edit_house_design, name='admin_edit_house_design'),
    path('house_design/remove/<int:id>', delete_house_design, name='admin_delete_house_design'),
    path('complaints/', manage_complaints, name='admin_manage_complaints'),
    path('complete/<int:id>', mark_complete, name='admin_mark_complete'),

]