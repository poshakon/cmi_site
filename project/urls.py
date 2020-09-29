from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from service.views import index, register, UserLogin, UserLogout, \
    dashboard, events_list, notices_list, news_list, part_list, user_info, evaluation, \
    parts_events, parts_notices, parts_evaluation, \
    event_edit, notice_edit, news_edit, \
    event_add, notice_add, news_add, \
    event_remove, notice_remove, news_remove, \
    events, notices, news, \
    event_view, notice_view, news_view, \
    become_part, unfollow_notice, parts_eval_notice, admin_report


urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', UserLogin.as_view(), name='login'),
    path('accounts/logout/', UserLogout.as_view(), name='logout'),
    path('accounts/register/', register, name='register'),

    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/report/', admin_report, name='admin_report'),

    path('dashboard/events/', events_list, name='events_list'),
    path('dashboard/notices/', notices_list, name='notices_list'),
    path('dashboard/news/', news_list, name='news_list'),
    path('dashboard/part_list/', part_list, name='part_list'),
    path('dashboard/user_info/', user_info, name='user_info'),
    path('dashboard/evaluation/', evaluation, name='evaluation'),

    path('dashboard/parts_events/', parts_events, name='parts_events'),
    path('dashboard/parts_notices/', parts_notices, name='parts_notices'),
    path('dashboard/parts_evaluation/', parts_evaluation, name='parts_evaluation'),

    path('dashboard/events/edit/<int:event_id>', event_edit, name='event_edit'),
    path('dashboard/notices/edit/<int:notice_id>', notice_edit, name='notice_edit'),
    path('dashboard/news/edit/<int:news_id>', news_edit, name='news_edit'),

    path('dashboard/events/add', event_add, name='event_add'),
    path('dashboard/notices/add', notice_add, name='notice_add'),
    path('dashboard/news/add', news_add, name='news_add'),

    path('dashboard/events/remove/<int:event_id>',
         event_remove, name='event_remove'),
    path('dashboard/notices/remove/<int:notice_id>',
         notice_remove, name='notice_remove'),
    path('dashboard/news/remove/<int:news_id>',
         news_remove, name='news_remove'),

    path('events/', events, name='events'),
    path('notices/', notices, name='notices'),
    path('news/', news, name='news'),

    path('event/<int:record_id>', event_view, name='event_view'),
    path('notices/<int:record_id>', notice_view, name='notice_view'),
    path('news/<int:record_id>', news_view, name='news_view'),

    path('become_part/<int:notice_id>', become_part, name='become_part'),
    path('unfollow_notice/<int:notice_id>', unfollow_notice, name='unfollow_notice'),
    path('eval_notice/<int:notice_id>', parts_eval_notice, name='parts_eval_notice'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
