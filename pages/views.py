from django.shortcuts import render
from django.views.generic import TemplateView


def pages(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THank you FOR visitING",
    }
    return render(request, "pages/pages.html", context)


class AboutPageView(TemplateView):
    template_name = "pages/about_page_view.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555"
        return context
