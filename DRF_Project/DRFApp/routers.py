from pkg_resources import DefaultProvider
from rest_framework.routers import DefaultRouter
from DRFApp.views import TeacherViewSet, StudentGenericAPIView, StudentViewSet,BookViewSet

# router  = SimpleRouter()  # it doesn't support hyperlinks and API root
router = DefaultRouter()
router.register('teacher',TeacherViewSet,basename = 'teachers')
router.register('book',BookViewSet,basename = 'books')
router.register('student',StudentViewSet,basename = 'students')
# router.register('genericstudent',StudentGenericAPIView,basename = 'genericstudents')

