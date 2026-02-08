#skip yhe admin course part
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotAllowed
from .form import PersonForm, TodoForm
from .models import Todo, Person


def hello_html(request):
    return render(request, 'todo/hello.html')


def hello_name(request, name):
    return HttpResponse(f"Hello, {name}! This is another view.")


def hello_query(request):
    name = request.GET.get("q")
    return HttpResponse(f"Hello, {name}! This is a query parameter view.")


def special_view(request):
    return redirect('hello_html')


def template_view(req):
    context = {
        "name": "Mike",
        "age": 30,
        "skills": ["python"]
    }

    return render(req, 'todo/template_demo.html', context)

# eg-1
# def post_view(request):
#     if request.method == "POST":
#         age = request.POST.get("age")
#         name = request.POST.get("name")
#         return HttpResponse(f"Received POST age: {age}, Name: {name}")
#     else:
#         return HttpResponseNotAllowed(['POST method is allowed.'])

# def submit_post(request):
#     return render(request, 'todo/submit.html')

# eg-2
# def post_view(request):
#     if request.method == "POST":
#         form = PersonForm(request.POST)  # Loads submitted data into form

#         if form.is_valid():
#             name = form.cleaned_data['name']
#             age = form.cleaned_data['age']
#             return HttpResponse(f"Received POST age: {age}, Name: {name}")
#     else:
#         return HttpResponseNotAllowed(['POST method is allowed.'])


# def submit_django_post(request):
#     # send a blank template to the form
#     form = PersonForm()
#     return render(request, 'todo/submit.html', {
#         "form": form
#     })


def todos_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            return HttpResponse('Todo successfully created!')
    else:
        form = TodoForm()
        todos = Todo.objects.all()
        return render(request, 'todo/todos.html', {'form': form, 'todos': todos})


def person_details(request, person_id):
    person = Person.objects.filter(id=person_id).first()
    return render('todos/person_details.html', {'person': person})


def delete_todo(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    todo.delete()
    return HttpResponse('Todo successfully deleted!')


def toggle_todo_done(request, todo_id):
    todo = Todo.objects.filter(id=todo_id).first()
    if todo:
        todo.done = not todo.done
        todo.save()
        return HttpResponse('Todo status toggled successfully!')
    return HttpResponse('Todo not found!', status=404)
