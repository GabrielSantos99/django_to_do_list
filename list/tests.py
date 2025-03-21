import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.core.exceptions import ValidationError
from .models import Task

class TaskModelTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(task_title="Teste de criação",task_description="",status=0,)

    def test_create_task(self):
        self.assertEqual(self.task.task_title, "Teste de criação")
        self.assertEqual(self.task.conclusion_date, None)

    def test_future_date_save(self):
        self.task.conclusion_date = timezone.now() + datetime.timedelta(days=1)

        with self.assertRaises(ValidationError):
            self.task.save()


class TaskStatusTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            task_title="Teste de criação",
            task_description="",
            status=0,
        )

    def test_change_status_to_done(self):
        self.task.status = Task.STATUS_CHOICE[-1][0]
        self.task.save()

        self.task.refresh_from_db()
        self.assertIsNotNone(self.task.conclusion_date)

class TaskViewResponse(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            task_title="Teste de criação",
            task_description="",
            status=0,
        )

    def test_views_without_pk(self):
        views = (
            'task_create',
            'task_list',
        )
        for view_name in views:
            with self.subTest(view = view_name):
                view_response = self.client.get(reverse(view_name))
                self.assertEqual(view_response.status_code, 200, f"Erro na view: {view_name}")

    def test_views_with_pk(self):
        views = (
            'task_detail',
            'task_update',
            'task_delete',
        )
        for view_name in views:
            with self.subTest(view = view_name):
                view_response = self.client.get(reverse(view_name, kwargs={'pk': self.task.pk}))
                self.assertEqual(view_response.status_code, 200, f"Erro na view: {view_name}")
