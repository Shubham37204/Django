# FBV - Function Based Views

from .models import Item
from .forms import ItemForm
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# from django.views.decorators.cache import cache_page
# from django.views.decorators.cache import vary_on_headers
# import logging

# Get an instance of the logger for this module
# logger = logging.getLogger(__name__)


@login_required
# @cache_page(60)
# @vary_on_headers("User-Agent")
def home(request):

    # logger.info("An informational message for the view was logged.")
    items = Item.objects.all()
    # logger.info(f"user requested is {request.user} with an ip of {request.META.get('REMOTE_ADDR')}")
    # logger.debug(f"An informational message {items.count()} items for the view was logged.")

    paginator = Paginator(items, 3)  # 3 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'mysite/index.html', context)


def detail(request, id):
    # first id is the items and second id is coming from web broswer
    # logger.info(f"Detail view accessed for item id: {id}")
    try:
        item = get_object_or_404(Item, id=id)
        # logger.debug(f"Item found: {item.name}")
    except Exception as e:
        # logger.error(f"Error retrieving item with id {id}: {e}")
        raise
    # item = Item.objects.get(id=id)
    context = {'item': item}
    return render(request, 'mysite/Detail.html', context)


@login_required
def createItem(request):
    form = ItemForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("mysite:home")
        # else:
        #     print(form.errors['price'])
    context = {
        "form": form
    }
    return render(request, 'mysite/item.html', context)


def edit_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("mysite:home")
    context = {
        "form": form
    }
    return render(request, 'mysite/item.html', context)


def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == "POST":
            item.delete()
            return redirect("mysite:home")

    context = {'item': item}
    return render(request, 'mysite/delete.html', context)


# CBV - Class Based Views
# from django.urls import reverse_lazy
# from .models import Item
# from .forms import ItemForm
# from django.shortcuts import redirect, render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# class ItemListView(ListView):
#     model = Item
#     template_name = 'mysite/index.html'
#     context_object_name = 'items'


# class ItemDetailView(DetailView):
#     model = Item
#     template_name = 'mysite/Detail.html'
#     context_object_name = 'item'


# class ItemCreateView(CreateView):
#     model = Item
#     fields = ['name', 'description', 'price', 'image']


# class ItemUpdateView(UpdateView):
#     model = Item
#     fields = ['name', 'description', 'price', 'image']
#     template_name_suffix = '_update_item'


# class ItemDeleteView(DeleteView):
#     model = Item
#     success_url = reverse_lazy('mysite:home')
