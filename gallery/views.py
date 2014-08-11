from django.shortcuts import render
from django.template import RequestContext
from gallery.models import Album, Photo
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

def home(request):
    context = RequestContext(request)
    context['photos'] = Album.objects.all()
    return render(request, 'index.html', context)

def photo(request):
    context = RequestContext(request)
    return render(request, 'detail.html', context)

class AlbumDetailView(DetailView):
    model = Album

    def get_context_data(self, **kwargs):

        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        print(context)
        ss = Album()
        photos = Photo.objects.filter(album=self.object.id)
        context['photos'] = photos

        return context

class AlbumListView(ListView):

    model = Album

    def get_context_data(self, **kwargs):

        context = super(AlbumListView, self).get_context_data(**kwargs)

        return context
