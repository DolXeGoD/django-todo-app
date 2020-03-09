from django.shortcuts import render
from .models import TbTodoList
from .forms import TodoForm

from django.views import generic

class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_board_list.html'
        todo_list = TbTodoList.objects.all()
        return render(request, template_name, {"todo_list" : todo_list})

class Todo_board_detail(generic.DetailView):
    model = TbTodoList
    template_name = 'todo_board/todo_board_detail_view.html'
    context_object_name = 'todo_list'

class Todo_board_update(generic.UpdateView):
    model = TbTodoList
    fields = {'title', 'content', 'end_date'}
    template_name = 'todo_board/todo_board_update.html'
    success_url = '/board/'

    def form_valid(self, form):
        form.save()
        return render(self.request, 'todo_board/todo_board_success.html', {"message":"일정 업데이트 완료"})

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object = self.object, form=form)

        return self.render_to_response(context)

def check_post(request):
    template_name = 'todo_board/todo_board_success.html'

    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정 추가 완료"
            return render(request, template_name, {"message" : message})

    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form" : form})


