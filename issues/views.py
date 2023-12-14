from django.views.generic import (
    ListView,
    CreateView,
    UpdateView)
from .models import Issue, Status 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)

# Create your views here.

class BoardView(ListView):
    template_name = "issues/board.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        to_do = Status.objects.get(name="to do")
        in_prog = Status.objects.get(name="in progress")
        done = Status.objects.get(name="done")
# you can send anything to the context object as long as you have a key you can give it any value
        context ["to_do_list"] = Issue.objects.filter(
            status=to_do
        ).order_by("created_on").reverse()
        context["in_prog_list"] = Issue.objects.filter(
            status=in_prog
        ).order_by("created_on").reverse()
        context ["done_list"] = Issue.objects.filter(
            status=done 
        ).order_by("created_on").reverse()
        return context 

# update issue
class StatusUpdateView(UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["status"]
    success_url = reverse_lazy("board")



# Create 
class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/create.html"
    model = Issue
    fields = ["summary", "description", "status"]

    def form_valid(self, form):
        status = Status.objects.get(name=form.instance.status)
        return super().form_valid(form)

# Read 
# class IssueDetailView(DetailView)
