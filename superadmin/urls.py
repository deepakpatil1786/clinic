from django.urls import path
from.import views

urlpatterns = [

   path('index/',views.index,name='index'),
   path('index-doctor/',views.index_doctor,name='index-doctor'),
   path('index-patient/',views.index_patient,name='index-patient'),
   path('',views.login,name='login'),
   path('logout/',views.logout,name='logout'),



    #--doctor--#
    
    path('create-doctor/',views.Create_doctor,name='create-doctor'),
    path('view-doctor/',views.view_doctor,name='view-doctor'),
    path('update-doctor/<int:pk>',views.update_doctor,name='update-doctor'),
    path('delete-doctor/<int:pk>',views.delete_doctor,name='delete-doctor'),
    path('profile-doctor/',views.profile_doctor,name='profile-doctor'),
    path('slot',views.slot,name='slot'),
    path('view-appointment-doc',views.view_appointment_doc,name='view-appointment-doc'),

    
     #--patient--#


   path('create-patient/',views.create_patient,name='create-patient'),
   path('view-patient/',views.view_patient,name='view-patient'),
   path('update-patient/<int:pk>',views.update_patient,name='update-patient'),
   path('delete-patient/<int:pk>',views.delete_patient,name='delete-patient'),
   path('profile-patient',views.profile_patient,name='profile-patient'),
   path('view-appointment-admin',views.view_appointment_admin,name='view-appointment-admin'),


    #---slots--#

    path('view-slot',views.view_slot,name='view-slot'),
    path('update-slot/<int:pk>',views.update_slot,name='update-slot'),
    path('delete-slot/<int:pk>',views.delete_slot,name='delete-slot'),

   #--appointment--#
   
   path('book-appointment/',views.book_appointment,name='book-appointment'),
   path('create_appointment/',views.create_appointment,name='create_appointment'),
   path('get-slot-list/',views.get_slot_list,name='get-slot-list'),
   path('view-appointment',views.view_appointment,name='view-appointment'),



 #--status------
   path('status-complete/<int:pk>',views.status_complete,name='status-complete'),
   path('status-absent/<int:pk>',views.status_absent,name='status-absent'),
   path('status-cancel/<int:pk>',views.status_cancel,name='status-cancel'),

]
