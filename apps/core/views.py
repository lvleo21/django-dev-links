from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from .models import Account


class AccountPageLinkAggregator(TemplateView):
    template_name = "core/pages/account_page_link.html"

    def get(self, request, *args, **kwargs):
        username = kwargs.get("username")
        self.user = get_object_or_404(Account, username=username)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"user": self.user})
        return context
