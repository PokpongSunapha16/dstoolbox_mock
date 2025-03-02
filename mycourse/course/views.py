from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from course.models import course


# Create your views here.

def course_list(request):
    courses = course.objects.all()
    return render(request ,'course_list.html', {"courses": courses})


def course_search(request):
    search = request.GET.get('id','')
    courses = course.objects.filter(id__icontains=search)
    return render(request, 'course_search.html', {'courses': courses})

class CourseUpdateView(UpdateView):
    model = course
    fields = ['id','name']
    template_name = 'course_update.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = course
    template_name = 'course_delete.html'
    success_url = reverse_lazy('course_list')

