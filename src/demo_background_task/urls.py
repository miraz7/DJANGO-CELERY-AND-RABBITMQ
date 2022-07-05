from django.urls import path

from demo_background_task.views import CreateBackgroundTask


urlpatterns=[
     
    path('create/', CreateBackgroundTask.as_view())

]