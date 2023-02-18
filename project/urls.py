from django.urls import path, include

from django.views.generic import TemplateView



urlpatterns = [
    
    # path('api/', include('project.back_app.urls')),
    
    path('front/', TemplateView.as_view(template_name='front_app/index.html')),
    
]
