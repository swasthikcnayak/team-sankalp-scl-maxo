from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
import users.urls as user_url

import attendance.urls as attendance_url
import marks.urls as marks_url
import assignments.urls as assignment_url
import academics.urls as academics_url

handler404 = 'djangoProject.views.handler404'
handler500 = 'djangoProject.views.handler500'
handler400 = 'djangoProject.views.handler400'
handler403 = 'djangoProject.views.handler403'

urlpatterns = [
    path('users/', include(user_url)),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    # path('attendance/', include(attendance_url)),
    # path('marks/', include(marks_url)),
    # path('assignments/', include(assignment_url)),
    # path('academics/',include(academics_url)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
