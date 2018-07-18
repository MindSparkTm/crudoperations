from django.conf.urls import url, include
from rest_framework import routers
from . import views
from . import api

router = routers.DefaultRouter()


router.register(r'userapi', api.Registerusersviewset)








urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),

)

urlpatterns += (
    # urls for patientVisit

    url(r'^register/$', views.Registerusers.as_view(), name='register'),
    url(r'^viewusers/$', views.Viewusers.as_view(), name='viewusers'),
    url(r'^deleteusers/$', views.deleteuser, name='deleteuser'),
    url(r'^updateusers/$', views.Updateusers.as_view(), name='updateusers'),
    #url(r'^updateexistinguser/$', views.updateuser, name='updateexistinguser'),

)



