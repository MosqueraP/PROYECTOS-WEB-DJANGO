from django.urls import path
from messenger.views import ThreadList, ThreadDetail

messenger_patterns = ([
    path('', ThreadList.as_view(), name='list'),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name='detail'),
], 'messenger') 