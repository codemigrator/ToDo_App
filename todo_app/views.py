from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from.models import Task
from.forms import FormsTask
from django .views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView



class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task1'


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ['name','priority','date']


    def get_success_url(self):
        return reverse_lazy('cbdv',kwargs={'pk':self.object.id})


class TaskUpdateView(DeleteView):
    model = Task
    template_name = 'delete.html'
    context_object_name = 'task'


def add(request):
    task1 = Task.objects.all()
    # if request.method == 'POST':
    #     name = request.POST.get('name', '')
    #     priority = request.POST.get('priority', '')
    #     date = request.POST.get('date', '')
    #     task = Task(name=name, priority=priority, date=date)
    #     task.save()

    return render(request, "index.html", {"task1": task1})


def update(request,id):
    data = Task.objects.get(id=id)
    frm = FormsTask(request.POST or None,instance=data)
    if frm.is_valid():
        frm.save()
        return redirect('/')
    return render(request,"update.html",{'form':frm,'data':data})


def delete(request,id):
    if request.method == 'POST':
        delte = Task.objects.get(id=id)
        delte.delete()
        return redirect('/')
    return render(request,'delete.html',)


