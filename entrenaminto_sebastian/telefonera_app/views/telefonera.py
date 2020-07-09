# store/views.py
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# specific to this view
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.urls import reverse_lazy

from entrenaminto_sebastian.telefonera_app.models import Telefono


class TelefonoListView(ListView):

    model = Telefono
    template_name = 'telefonera_app/telefonos/list.html'
    context_object_name = 'telefonos'
    paginate_by = 5
    
    '''
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        books = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(books, self.paginate_by)
        try:
            books = paginator.page(page)
        except PageNotAnInteger:
            books = paginator.page(1)
        except EmptyPage:
            books = paginator.page(paginator.num_pages)
        context['books'] = books
        return context
    '''    

class TelefonoCreateView(CreateView):
    model = Telefono
    template_name = 'telefonera_app/telefonos/form.html'
    fields = ('tipo', 'nombre', 'telefono', )
    success_url = reverse_lazy('telefonera_app:telefonera-list')


class TelefonoDetailView(DetailView):

    model = Telefono
    template_name = 'telefonera_app/telefonos/detail.html'
    context_object_name = 'telefono'


class TelefonoUpdateView(UpdateView):

    model = Telefono
    template_name = 'telefonera_app/telefonos/form.html'
    context_object_name = 'telefono'
    fields = ('tipo', 'nombre', 'telefono', )

    def get_success_url(self):
        return reverse_lazy('telefonera_app:telefonera-list')


class TelefonoDeleteView(DeleteView):
    model = Telefono
    context_object_name = 'telefono'
    template_name = 'telefonera_app/telefonos/confirm_delete.html'
    success_url = reverse_lazy('telefonera_app:telefonera-list')