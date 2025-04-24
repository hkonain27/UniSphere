from django.urls import path
from . import views

urlpatterns = [
    # --- Authentication ---
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),

    # --- Main Pages ---
    path('', views.landing_page, name="landing_page"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('about-us/', views.about_us, name="about_us"),
    path('contact-us/', views.contact_us, name="contact_us"),

    # --- Events ---
    path('events/', views.events_list, name="events_list"),
    path('events/create/', views.create_event, name="create_event"),

    # --- Groups ---
    path('groups/', views.group_discovery, name="group_discovery"),
    path('groups/join/<int:group_id>/', views.join_group, name="join_group"),
    path('groups/<int:group_id>/chat/', views.group_chat, name="group_chat"),

    # --- Housing ---
    path('housing/', views.housing_search, name="housing_search"),
    
    path('jobs/', views.job_search, name='job_details'),  # ✅ Correct
    # --- Messaging handled inside group_chat ---
  
    path('api/', views.job_api, name='job_api'),


    # Optional catch-all test/debug routes
    path('layout/', views.layout, name="layout_test"),
]
