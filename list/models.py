from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

class Task(models.Model):
    # Manter sempre o concluido na útima posição do Array
    STATUS_CHOICE = [
        (0, "Pendente"),
        (1, "Em Andamento"),
        (2, "Concluido")
    ]
    task_title = models.CharField('Titulo', max_length=200)
    task_description = models.TextField('Descrição', blank=True, default="")
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    conclusion_date = models.DateTimeField("Finalizado em", null=True, blank=True)
    created_date = models.DateTimeField("Criado em", default=timezone.now, editable=False)

    def clean(self):
        if self.conclusion_date != None and self.conclusion_date > timezone.now():
            raise ValidationError("A data de conclusão não pode ser no futuro.")

    def save(self, *args, **kwargs):
        self.clean()

        conclusion_status = self.STATUS_CHOICE[-1][0]

        if self.status == conclusion_status and self.conclusion_date is None:
            self.conclusion_date = timezone.now()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.task_title
