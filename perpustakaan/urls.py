from django.urls import path
from .views import (get_book, get_book_by_id_json, get_book_json, get_book_by_id,
                    get_book_review_id_json,get_book_history_active_id_json,
                    get_book_history_done_id_json,
                    borrow, review, return_book)
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from depoksmartcity import settings

app_name = 'perpustakaan'

urlpatterns = [
    path('', get_book, name='get_book'),
    path('json', get_book_json, name='get_book_json'),
    path('book/<int:id>', get_book_by_id, name='get_book_by_id'),
    path('book/<int:id>/json', get_book_by_id_json, name='get_book_by_id_json'),
    path('book/borrow/<int:id>', borrow, name='borrow'),
    path('book/return/<int:id>', return_book, name='return_book'),
    path('book/review/<int:id>', review, name='review'),
    path('book/history/active/<int:id>', get_book_history_active_id_json, name='get_book_history_active_id_json'),
    path('book/history/done/<int:id>', get_book_history_done_id_json, name='get_book_history_done_id_json'),
    path('book/review/<int:id>/json', get_book_review_id_json, name='get_book_review_id_json'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)