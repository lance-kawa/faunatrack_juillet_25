from django.test import TestCase
from django.contrib.auth.models import User

from faunatrack.models import FaunatrackUser, Project, ProjectUserAccess

# Create your tests here.

class RBACTest(TestCase):

    def setUp(self):
        self.project = Project.objects.create(title="test")
        self.project2 = Project.objects.create(title="test")
        self.user, _ = FaunatrackUser.objects.get_or_create(user=User.objects.create(username="test"))
        self.user_access = ProjectUserAccess.objects.create(project=self.project, user=self.user)
        self.user_access2 = ProjectUserAccess.objects.create(project=self.project2, user=self.user)

    def tearDown(self):
        pass

    def test_something(self):
        try:
            user_access = ProjectUserAccess.objects.get(project=self.project)
            self.assertEqual(user_access.user, self.user) 
        except ProjectUserAccess.DoesNotExist:
            pass
        