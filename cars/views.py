from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView
from .models import Car
from .forms import CarForm
from django.views.generic import ListView
from django.views.generic.edit import CreateView


def car_list(request):
    query = request.GET.get('q')
    if query:
        cars = Car.objects.filter(make__icontains=query) | Car.objects.filter(model__icontains=query)
    else:
        cars = Car.objects.all()

    return render(request, 'car_list.html', {'cars': cars})

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            car.is_published = False  # Поле is_published будет False при создании
            car.save()
            return   # Перенаправление на список автомобилей после сохранения
    else:
        form = CarForm()
    return render(request, 'car_form.html', {'form': form})

class CarUpdateView(UpdateView):
    model = Car
    fields = ['make', 'model', 'year', 'price', 'description', 'image']
    template_name = 'car_form.html'
    success_url = 'cars'

    def get_form(self, form_class=None):
        """Удаляем поле 'is_published', если пользователь не администратор"""
        form = super().get_form(form_class)
        if not self.request.user.is_staff:  # Если пользователь не администратор
            form.fields.pop('is_published', None)  # Убираем поле 'is_published'
        return form

    def form_valid(self, form):
        car = form.save(commit=False)
        if not self.request.user.is_staff:  # Если пользователь не администратор
            car.is_published = Car.objects.get(pk=self.object.pk).is_published  # Сохраняем старое значение
        car.save()
        return super().form_valid(form)
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarCreateView(CreateView):
    model = Car
    template_name = 'car_form.html'
    fields = ['name', 'model', 'price']
