from django.urls import path
from api.views.RcuCommand import *

app_name = "api"

urlpatterns = [
    path("GetAllRCUCommand", ConfigByRCUType.as_view(), name="get_all_rcu_command")
]