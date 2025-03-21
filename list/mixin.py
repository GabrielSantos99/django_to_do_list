from django.contrib import messages
from django.core.exceptions import ValidationError

class SuccessMessageMixin:
    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except ValidationError as e:
            form.add_error(None, e)
            return self.form_invalid(form)
    