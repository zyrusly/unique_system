"""MedicalSymptoms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Med import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<symptom_id>/',views.symptom_page,name='symptom_page'),
    path('<symptom_id>/diagnosis/<yob>/<gender>/',views.symptom_diagnosis,name='symptom_diagnosis'),
    path('treatment/<issue_id>/<lat>/<lon>/',views.treatment,name='treatment'),
]
