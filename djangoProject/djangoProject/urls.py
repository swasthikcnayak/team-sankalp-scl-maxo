from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



import users.urls as user_url
import attendance.urls as attendance_url
import marks.urls as marks_url
import assignments.urls as assignment_url
import academics.urls as academics_url

urlpatterns = [
    path('users/',include(user_url)),
    # path('attendance/', include(attendance_url)),
    # path('marks/', include(marks_url)),
    # path('assignments/', include(assignment_url)),
    # path('academics/',include(academics_url)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
