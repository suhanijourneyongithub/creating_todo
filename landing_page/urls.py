from django.urls import path
from . import views
#~~~~~~~~~~~~~~~~~~~~~~~~~~MEDIA KE LIYE~~~~~~~~~~
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("cls", views.landing_page, name = "landing_page"),

    path("to_do", views.to_do, name = "to_do"),

    path("add_todo", views.add_todo, name = "add_todo"),

    path("delete_todo/<int:todo_id>", views.delete_todo, name = "delete_todo"),
    
    path("update_todo/<int:todo_id>", views.update_todo, name = "update_todo"),

    path("mark_complete/<int:todo_id>", views.mark_complete, name = "mark_complete"),

    path("profile_pic", views.profile_pic, name = "profile_pic")
  
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)