from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from .models import ProjectEntry

# Create your tests here.

class ProjectEntryTests(TestCase):
    project_name = "project name test"
    description = "description test"
    git_repo = "http://www.gitrepo.com"

    def test_validator_start_year_valid(self):
        entry = ProjectEntry(proj_name=self.project_name, description=self.description, start_year=2020, git_repo=self.git_repo) 
        entry.full_clean()

    def test_validator_start_year_early(self):
        entry = ProjectEntry(proj_name=self.project_name, description=self.description, start_year=1899, git_repo=self.git_repo)
        with self.assertRaises(ValidationError):
            entry.full_clean()
    def test_validator_start_year_future(self):
        year = timezone.now().year + 1

        entry = ProjectEntry(proj_name=self.project_name, description=self.description, start_year=year, git_repo=self.git_repo)
        with self.assertRaises(ValidationError):
            entry.full_clean()
