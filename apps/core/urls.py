from django.urls import path

from .views import AccountPageLinkAggregator

urlpatterns = [
    path(
        "@<username>",
        AccountPageLinkAggregator.as_view(),
        name="account-page-link-aggregator"
    ),
]
