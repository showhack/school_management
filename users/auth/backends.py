# from django.contrib.auth import SESSION_KEY
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.sessions.models import Session
#
#
# class OneSessionBackend(ModelBackend):
#     def _retrieve_user_sessions(self, user):
#         user_sessions = []
#         for session in Session.objects.all():
#             session_id = session.get_decoded()[SESSION_KEY]
#             if user.pk == int(session_id):
#                 user_sessions.append(session)
#         return user_sessions
#
#     def _remove_last_user_sessions(self, user):
#         for session in self._retrieve_user_sessions(user):
#             session.delete()
#
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         user = super().authenticate(request, username, password, **kwargs)
#         if user:
#             self._remove_last_user_sessions(user)
#         return user
