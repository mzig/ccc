from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import generic
from eventos.models import Expo
from django.template.context_processors import static


# Create your views here.

#
# class HomePageView(TemplateView):
#     # template_name = "../cccviews/dist/home.html"
#     template_name = "home.html"
#
#     # def expo(request):
#     #     return render(request, '../cccviews/dist/expo.html')
#
#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         context['expo_list'] = Expo.objects.all()#[:5]
#         return context


class HomeView(generic.ListView):
    template_name = 'base.html'
    context_object_name = 'expo_list'

    def get_queryset(self):
        return Expo.objects.all()



class IndexView(generic.ListView):
    template_name = 'base.html'
    context_object_name = 'expo_list'

    def get_queryset(self):
        return Expo.objects.all()



class DetailView(generic.DetailView):
    model = Expo
    template_name = 'expo.html'
