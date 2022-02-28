from rest_framework.routers import DefaultRouter
from .views import CollegeStudentViewSet,DepartmentViewSet,CourseViewSet,CollegeViewSet
router = DefaultRouter()
router.register('college_student', CollegeStudentViewSet,basename='collegestudent')
router.register('college_department', DepartmentViewSet,basename='collegedepartment')
router.register('college_courses', CourseViewSet,basename='collegecourses')
router.register('college', CollegeViewSet,basename='colleges')