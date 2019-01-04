from django.urls import path
from . import views


app_name = 'Controller'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/setName', views.set_name, name='set_name'),
    path('login/checkUser', views.check_user, name='check_user'),
    path('event/addEvent', views.create_calendar, name='create_calendar'),
    path('user/events', views.get_calendar, name='get_calendar'),
    path('event/deleteEvent', views.delete_calendar, name='delete_calendar'),
    path('event/modifyEvent', views.edit_calendar, name='edit_calendar'),
    path('invitation/addInvitation', views.create_invitation, name='create_invitation'),
    path('invitation/modifyInvitation', views.edit_invitation, name='edit_invitation'),
    path('invitation/deleteInvitation', views.delete_invitation, name='delete_invitation'),
    path('invitation/acceptInvitation', views.accept_invitation, name='accept_invitation'),
    path('invitation/getInviterInvitations', views.get_inviter_invitations, name='get_inviter_invitations'),
    path('invitation/getSingleInvitation', views.get_single_invitation, name='get_single_invitation'),
    path('invitation/getInviteeInvitations', views.get_invitee_invitations, name='get_invitee_invitations'),
    path('statistics/getStatistics', views.get_statistics, name='get_statistics'),
    path('statistics/addStatistic', views.add_statistic, name='add_statistic'),
    path('statistics/getSingleStatistic', views.get_single_statistic, name='get_single_statistic'),
    path('statistics/addReply', views.add_reply, name='add_reply')
]