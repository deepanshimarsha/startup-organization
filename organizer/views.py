"""Views for Organizer App"""

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    RedirectView,
    UpdateView,
)

from .forms import NewsLinkForm, StartupForm, TagForm
from .models import NewsLink, Startup, Tag


class NewsLinkCreate(
    CreateView
):
    """Create a link to an article about a startup"""

    extra_context = {"update": False}
    form_class = NewsLinkForm
    model = NewsLink
    template_name = "newslink/form.html"

    def get_initial(self):
        """Pre-select Startup in NewsLinkForm"""
        startup = get_object_or_404(
            Startup, slug=self.kwargs.get("startup_slug")
        )
        return dict(
            super().get_initial(), startup=startup.pk
        )


class NewsLinkDelete(
    DeleteView
):
    """Delete a link to an article about a startup"""
    model = NewsLink

    template_name = "newslink/confirm_delete.html"

    def get_success_url(self):
        """Return the detail page of the Startup parent
        http://ccbv.co.uk/DeletionMixin
        """
        startup = get_object_or_404(
            Startup, slug=self.kwargs.get("startup_slug")
        )
        return startup.get_absolute_url()


class NewsLinkDetail(RedirectView):
    """Redirect to Startup Detail page
    http://ccbv.co.uk/RedirectView/
    """
    model = NewsLink

    def get_redirect_url(self, *args, **kwargs):
        """Redirect user to Startup page"""
        return self.get_object().get_absolute_url()


class NewsLinkUpdate(

    UpdateView
):
    """Update a link to an article about a startup"""
    model = NewsLink

    extra_context = {"update": True}
    form_class = NewsLinkForm
    template_name = "newslink/form.html"


class TagList(ListView):
    """Display a list of Tags"""
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tag/list.html"


class TagDetail(DetailView):
    """Display a single Tag"""
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tag/detail.html"


class TagCreate(CreateView):
    """Create new Tags via HTML form"""

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": False}


class TagUpdate(UpdateView):
    """Update a Tag via HTML form"""

    form_class = TagForm
    model = Tag
    template_name = "tag/form.html"
    extra_context = {"update": True}


class TagDelete(DeleteView):
    """Confirm and delete a Tag via HTML Form"""

    model = Tag
    template_name = "tag/confirm_delete.html"
    success_url = reverse_lazy("tag_list")


class StartupCreate(CreateView):
    """Create new Startups via HTML form"""

    form_class = StartupForm
    model = Startup
    template_name = "startup/form.html"
    extra_context = {"update": False}


class StartupDelete(DeleteView):
    """Confirm and delete a Startup via HTML Form"""

    model = Startup
    template_name = "startup/confirm_delete.html"
    success_url = reverse_lazy("startup_list")


class StartupList(ListView):
    """Display a list of Startups"""
    model = Startup
    queryset = Startup.objects.all()
    template_name = "startup/list.html"


class StartupDetail(DetailView):
    """Display a single Startup"""
    model = Startup
    queryset = Startup.objects.all()
    template_name = "startup/detail.html"


class StartupUpdate(UpdateView):
    """Update a Startup via HTML form"""

    form_class = StartupForm
    model = Startup
    template_name = "startup/form.html"
    extra_context = {"update": True}