from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField

from wagtail.core.models import Page


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context


class BasePage(Page):
    body = RichTextField(blank=True)

    footer = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        FieldPanel('footer', classname="full"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['menuitems'] = HomePage.objects.get(slug='home', depth=2).get_children().filter(
            live=True, show_in_menus=True)

        return context
