from typing import Any
from django.shortcuts import render

from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "core/pages/home.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context.update({
            "social_networks": self.request.user.get_all_socialnetworks(),
            "account_links": self.request.user.get_all_accountlinks(),
        })

        return context
