from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import FormView

from hello_world_app.forms import NameForm
from hello_world_app.models import Name


class NameCreationView(FormView):
    template_name = 'create_name.html'
    form_class = NameForm

    def form_valid(self, form):
        new_name = form.save()
        return redirect('show_name', name_id=new_name.id)


class NameShowView(View):
    template_name = 'show_name.html'

    def get(self, request, name_id):
        name = get_object_or_404(Name, pk=name_id)
        return render(request, self.template_name, {'name': name.value})
