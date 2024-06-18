from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView


class HomeTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "core/pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "social_networks": self.request.user.get_all_socialnetworks(),
            "account_links": self.request.user.get_all_accountlinks(),
        })

        return context
