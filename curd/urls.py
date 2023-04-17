from django.urls import path
from .views import createView, store, index, deleteEmp, updateView, update, viewEmp

urlpatterns = [
    path(''               , index),
    path('create'         , createView),
    path('store'          , store     , name='store'),
    path('view/<int:pk>'  , viewEmp   , name='viewEmp'),
    path('delete/<int:pk>', deleteEmp , name='deleteEmp'),
    path('update/<int:pk>', updateView, name='updateEmp'),
    path('edit/<int:pk>'  , update    , name='edit'),
]
