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

def check_post(request):
    template_name = 'todo_board/todo_board_success.html'

    if request.method == "POST":
        form = TodoForm(request.POST)
        print(form)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.todo_save()
            message = "일정 추가 완료"
            return render(request, template_name, {"message" : message})

    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form" : form})


