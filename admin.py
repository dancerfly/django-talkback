from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from zenaida.contrib.feedback.models import FeedbackItem

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
            'fields': ("user", ("content", "screenshot",),)
        }),
        ("Request Data", {
            'fields': (
                ("view", "request_path", "request_method", "request_encoding",),
                ("request_meta", "request_get",),
                ("request_post", "request_files",),
            )
        }),
    )

    readonly_fields = (
        "user",
        "content",
        "screenshot",
        "view",
        "request_path",
        "request_method",
        "request_encoding",
        "request_meta",
        "request_get",
        "request_post",
        "request_files",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True)
    mark_resolved.short_description = "Mark these items as resolved."

    def mark_unresolved(self, request, queryset):
        queryset.update(resolved=False)
    mark_unresolved.short_description = "Mark these items as not resolved."

    actions = [mark_resolved, mark_unresolved]

admin.site.register(FeedbackItem, FeedbackAdmin)
