from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views import generic
from eventos.models import Expo, Actividad, Evento
from nucleo.models import Tag, Articulo, TipoActividad, Publicacion
from django.template.context_processors import static
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render


# Create your views here.


# class HomeView(TemplateView):
#     # template_name = "../cccviews/dist/home.html"
#     template_name = "index.html"
#
#     # def expo(request):
#     #     return render(request, '../cccviews/dist/expo.html')
#
#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         context['expo_list'] = Expo.objects.all()[:5]
#         return context

############HOME+++++++++++++++++
class HomeView(TemplateView):
    template_name = 'index.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        expos = Expo.objects.order_by("-fecha_inicio")[:6]
        acts = Actividad.objects.filter(fecha_fin__gt=timezone.now()).order_by("-fecha_fin")[:6]
        items = list(expos) + list(acts)
        items.sort(key=lambda i: i.fecha_inicio, reverse=True)
        owlexpo = Expo.objects.filter(carrusel=True).order_by('-fecha_inicio')[:6]

        return {"owlexpo": owlexpo, "acts": acts}
        # return {}

    # def get_queryset(self):
    #     return Expo.objects.all()


###############EXPOS´´´´´´´´´´´´´´´´´´´´
class ExpoListView(generic.ListView):
    template_name = 'expo-grid-list.html'
    context_object_name = 'expo_list'
    tags_list = 'expo_tags'


    def get_queryset(self):
        return Expo.objects.filter(fecha_fin__gt=timezone.now())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ExpoListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['current_expo_list'] = Expo.objects.filter(fecha_fin__gt=timezone.now())
        return context


    # def get_queryset(self):
    #     expolist = Expo.objects.filter(fecha_fin__gt=timezone.now())
    #     tagslist = Tag.objects.all()
    #     context =  {"expo_list" : expolist, "tags_list" : tagslist}
    #     return context

class ArchivoExposListView(generic.ListView):
    template_name = 'archive-expo-list.html'
    context_object_name = 'archive_expo_list'
    paginate_by = '15'
    tags_list = 'expo_tags'

    # def get_queryset(self):
    #     return Expo.objects.filter(fecha_fin__lt=timezone.now())
    #
    # def listing(request):
    #     expo_list = Expo.objects.filter(fecha_fin__lt=timezone.now())
    #     paginator = Paginator(expo_list, 8)  # Show 25 contacts per page
    #
    #     page = request.GET.get('page')
    #     try:
    #         expos = paginator.page(page)
    #     except PageNotAnInteger:
    #         # If page is not an integer, deliver first page.
    #         expos = paginator.page(1)
    #     except EmptyPage:
    #         # If page is out of range (e.g. 9999), deliver last page of results.
    #         expos = paginator.page(paginator.num_pages)
    #
    #     return render(request, 'archive-expo-list.html', {'archivo': expos})


    def get_queryset(self):
        return Expo.objects.filter(fecha_fin__lt=timezone.now())

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArchivoExposListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['current_expo_list'] = Expo.objects.filter(fecha_fin__gt=timezone.now())
        return context


class ExpoDetailView(generic.DetailView):
    model = Expo
    template_name = 'expos-detail-event.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ExpoDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['current_expo_list'] = Expo.objects.filter(fecha_fin__gt=timezone.now())
        return context


#################ACTS""""""""""""""""
class ActsListView(generic.ListView):
    template_name = 'acts-grid-list.html'
    context_object_name = 'acts_list'
    tags_list = 'acts_tags'

    def get_queryset(self):
        return Actividad.objects.filter(fecha_fin__gt=timezone.now())
        # return Actividad.objects.all()


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ActsListView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['tipo_acts_list'] = TipoActividad.objects.all()
        return context


class ArchivoActsListView(generic.ListView):
    template_name = 'archive-acts-list.html'
    context_object_name = 'archive_acts_list'
    paginate_by = '15'
    tags_list = 'acts_tags'

    def get_queryset(self):
        return Actividad.objects.filter(fecha_fin__lt=timezone.now())


class ActsDetailView(generic.DetailView):
    model = Actividad
    template_name = 'act-detail-event.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ActsDetailView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['current_acts_list'] = Actividad.objects.filter(fecha_fin__gt=timezone.now())
        return context


#################ARTICULO¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿
class ArticleDetailView(generic.DetailView):
    model = Articulo
    template_name = 'article-detail.html'


#################PUBLICACIO*****************
class PublsListView(generic.ListView):
    template_name = 'publs-grid-list.html'
    context_object_name = 'publs_list'

    def get_queryset(self):
        return Publicacion.objects.all()











# class HomeView(generic.ListView):
#     template_name = 'base.html'
#     context_object_name = 'expo_list'
#
#     def get_queryset(self):
#         return Expo.objects.all()
#
#
#
# class IndexView(generic.ListView):
#     template_name = 'base.html'
#     context_object_name = 'expo_list'
#
#     def get_queryset(self):
#         return Expo.objects.all()
#
#
#
# class DetailView(generic.DetailView):
#     model = Expo
#     template_name = 'expo.html'
