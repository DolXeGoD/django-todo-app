from django.http import JsonResponse
from django.shortcuts import render
from .models import TbTodoList
from .forms import TodoForm

from django.views import generic

class Todo_board(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'todo_board/todo_board_list.html'
        todo_list = TbTodoList.objects.all()

        # 진행 중인 할 일
        incomplete_todo_list = TbTodoList.objects.all().filter(end_date__isnull=False, is_complete=0).order_by('priority')

        # 마감된 할 일
        complete_todo_list = TbTodoList.objects.all().filter(is_complete=1).order_by('priority')

        return render(request, template_name, {"incomplete_todo_list" : incomplete_todo_list, "complete_todo_list" : complete_todo_list})

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

class Todo_board_delete(generic.DeleteView):
    model = TbTodoList
    success_url = '/board/'
    context_object_name = 'todo_list'


def check_post(request):
    template_name = 'todo_board/todo_board_success.html'

    if request.method == "POST":
        if str(request.path).split("/board/")[1].split("/")[0] == "insert":
            form = TodoForm(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.todo_save()
                message = "일정 추가 완료"
                return render(request, template_name, {"message" : message})

        elif str(request.path).split("/board/")[1].split("/")[0] == "is_complete":
            pk = request.POST['data']
            return_value = checkbox_event(pk, True)
            return JsonResponse(return_value)

        elif str(request.path).split("/board/")[1].split("/")[0] == "is_incomplete":
            pk = request.POST['data']
            return_value = checkbox_event(pk, False)
            return JsonResponse(return_value)

    else:
        template_name = 'todo_board/todo_board_insert.html'
        form = TodoForm
        return render(request, template_name, {"form" : form})

# 마감 체크박스 관련 함수
def checkbox_event(pk, is_check):
    todo_selected = TbTodoList.objects.get(pk=pk) # 해당 인덱스의 데이터를 가져옴
    if is_check == True: # 체크 시
        todo_selected.is_complete = 1 # 완료로 변경
        todo_selected.priority = None
    else: # 체크 해제 시
        todo_selected.is_complete = 0 # 미완료로 변경
    todo_selected.save()
    return_value = {'text': '저장되었습니다.'}
    return return_value
