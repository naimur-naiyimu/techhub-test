from django.urls import path
from users.views import UserView
from course.views import CourseView, EnrollView, EnrollUserView
from job.views import JobView, JobViewID
from blog.views import BlogView, BlogViewID
from chat.views import HomeView, RoomView, CheckView, MessageView, MessageDetailView

urlpatterns = [
    path('user/', UserView.as_view()),
    path('course/', CourseView.as_view()),
    path('course/<int:pk>/', CourseView.as_view()),
    path('job/', JobView.as_view()),
    path('job/<int:pk>/', JobViewID.as_view()),
    path('blog/', BlogView.as_view()),
    path('blog/<int:pk>', BlogViewID.as_view()),
    path('enroll/', EnrollView.as_view()),
    path('enroll/<int:pk>/', EnrollView.as_view()),
    # path('enrolluser/<int:pk>/', Enrolluser.as_view()),
    path('enrollments/user/<int:user_id>/',
         EnrollUserView.as_view(), name='user-enrollments'),
    
    path('chat/', HomeView.as_view(), name='home'),
    path('<str:name>/', RoomView.as_view(), name='room'),
    path('checkview/', CheckView.as_view(), name='checkview'),
    path('send/', MessageView.as_view(), name='send'),
    path('getMessages/<str:room>/', MessageView.as_view(), name='getMessages'),
    path('message/<int:pk>/', MessageDetailView.as_view(), name='message-detail'),

]
