from django.urls import path
from .views import PagesListView,PageDetailView, PageCreate, PageUpdate, PageDelete
from django.contrib.auth.decorators import login_required

# urlpatterns = [
pages_patterns = ([
    path('', PagesListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('create/', PageCreate.as_view(), name='create'),
    path('update/<int:pk>/', PageUpdate.as_view(), name='update'),
    # path('delete/<int:pk>/', login_required(PageDelete.as_view(template_name='delete'))),
    path('delete/<int:pk>/', PageDelete.as_view(), name='delete'),

], 'pages')