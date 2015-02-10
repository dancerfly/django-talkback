from django.conf import settings
from django.contrib import admin
from django.template.defaultfilters import linebreaksbr
from django.utils.translation import ugettext_lazy as _

from talkback.models import FeedbackItem

class ResolvedListFilter(admin.SimpleListFilter):
    """
    Filter for FeedbackAdmin, which filters on the `resolved` field,
    but defaults to showing unresolved items.

    """

    title = _("resolved")
    parameter_name = "resolved"

    def lookups(self, request, modeladmin):
        return (
            ("all", _("All")),
            (None, _("No")),
            ("yes", _("Yes"))
        )

    def choices(self, cl):
        for lookup, title in self.lookup_choices:
            yield {
                'selected': self.value() == lookup,
                'query_string': cl.get_query_string({
                    self.parameter_name: lookup,
                }, []),
                'display': title,
            }

    def queryset(self, request, queryset):
        if self.value() == "all":
            return queryset
        elif self.value() == "yes":
            return queryset.filter(resolved=True)
        else:
            return queryset.filter(resolved=False)

def _preformatted_display_method(attr_name):
    def inner(self, obj):
        return linebreaksbr(getattr(obj, attr_name).replace("  ","&nbsp;&nbsp;").replace("\n ","&nbsp;"))
    return inner

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "__unicode__", "content", "resolved",)
    list_links = ("timestamp", "__unicode__")
    list_editable = ("resolved",)
    list_filter = (ResolvedListFilter, "request_path", "view", "timestamp",)

    fieldsets = (
        (None, {
            'fields': ('resolved',)
        }),
        ("Content", {
            'fields': ("user", ("content_html", "screenshot_html",),)
        }),
        ("Request Data", {
            'fields': (
                ("view", "request_path", "request_method", "request_encoding",),
                ("request_meta_html", "request_get_html",),
                ("request_post_html", "request_files_html",),
            )
        }),
    )

    readonly_fields = (
        "user",
        "content_html",
        "screenshot_html",
        "view",
        "request_path",
        "request_method",
        "request_encoding",
        "request_meta_html",
        "request_get_html",
        "request_post_html",
        "request_files_html",
    )

    # Custom Fields
    request_meta_html = _preformatted_display_method("request_meta")
    request_meta_html.short_description = "Request meta"
    request_get_html = _preformatted_display_method("request_get")
    request_get_html.short_description = "Request GET"
    request_post_html = _preformatted_display_method("request_post")
    request_post_html.short_description = "Request POST"
    request_files_html = _preformatted_display_method("request_files")
    request_files_html.short_description = "Request FILES"

    def content_html(self, obj):
        return linebreaksbr(obj.content)
    content_html.short_description = "Content"

    def screenshot_html(self, obj):
        return "<a href=\"{url}\"><img src=\"{url}\" width=\"300\" /></a>".format(url=obj.screenshot.url)
    screenshot_html.short_description = "Screenshot"

    # Admin API Methods

    def has_add_permission(self, request, obj=None):
        return False

    # Actions

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True)
    mark_resolved.short_description = "Mark these items as resolved."

    def mark_unresolved(self, request, queryset):
        queryset.update(resolved=False)
    mark_unresolved.short_description = "Mark these items as not resolved."

    actions = [mark_resolved, mark_unresolved]

admin.site.register(FeedbackItem, FeedbackAdmin)
