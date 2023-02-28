from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Balancesheet


class IndexView(generic.TemplateView):
    template_name="index.html"

class SummaryView(LoginRequiredMixin, generic.ListView):
    model = Balancesheet
    template_name = 'balance_list.html'

    def get_queryset(self):
        balance_list = Balancesheet.objects.filter(user=self.request.user).order_by('date')    
        return balance_list

