from django.urls import path
from . import views

urlpatterns = [
    # --- Authentication ---
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    # --- Main Pages ---
    path('', views.landing_page, name="landing_page"),
   # path('home/', views.home_page, name="home"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('about-us/', views.about_us, name="about_us"),
    path('contact-us/', views.contact_us, name="contact_us"),

    # --- Events ---
    path('events/', views.events_page, name="events"),
    path('events/create/', views.create_event, name="create_event"),
    path('projects/', views.project_list, name='project_list'),

    # --- Groups ---
    path('groups/', views.group_discovery, name="group_discovery"),
    # using 'home' as the name
    path('groups/', views.home, name='home'), 
    path('create-room/', views.create_room, name='create-room'),
    path('groups/join/<int:group_id>/', views.join_group, name="join_group"),
    path('groups/<int:group_id>/chat/', views.group_chat, name="group_chat"),

    # --- Housing ---
    path('housing/', views.housing_search, name="housing_search"),
     
    path('jobs/', views.job_search, name='job_search'), 
    path('jobs/<int:job_id>/', views.job_details, name='job_details'),
    path('profile/<int:pk>/', views.user_profile, name='user-profile'),

   

   # path('jobs/', views.job_search, name='job-details'), 
    # --- Messaging handled inside group_chat ---
  
    #path('api/', views.job_api, name='job_api'),


    # Optional catch-all test/debug routes
    path('layout/', views.layout, name="layout_test"),
]
