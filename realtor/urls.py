from django.urls import path
from .views import  *


urlpatterns = [
    path('', AgentListView.as_view(), name='agents'),
    path('<pk>/', AgentDetailView.as_view(), name='agent-detail'),
    path('topseller', TopsellerListView.as_view(), name='topseller'),

]
