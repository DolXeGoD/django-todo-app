from django.shortcuts import render

# Create your views here.
from django.views import generic


class Todo_main(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = "todo_main/index.html"
        return render(request, template_name)