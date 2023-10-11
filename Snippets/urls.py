from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('', views.index_page, name='home'),
    path('snippets/add', views.add_snippet_page, name='add'),
    path('snippets/list', views.snippets_page, name='list'),
    path('snippets/<int:id_snip>', views.snippet, name='snippet'),
    path('snippets/delete/<int:id_snip>', views.delete_snippet, name='delete_snippet'),
    path('snippets/update/<int:id_snip>', views.update_snippet, name='update_snippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
