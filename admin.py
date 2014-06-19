from django.contrib import admin

from zenaida.contrib.feedback.models import FeedbackItem

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("timestamp", "__unicode__", "content", "resolved",)
    list_links = ("timestamp", "__unicode__")
    list_editable = ("resolved",)
    list_filter = ("resolved", "request_path", "view", "timestamp",)

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

    def mark_resolved(self, request, queryset):
        queryset.update(resolved=True)
    mark_resolved.short_description = "Mark these items as resolved."

    def mark_unresolved(self, request, queryset):
        queryset.update(resolved=False)
    mark_resolved.short_description = "Mark these items as not resolved."

    actions = [mark_resolved, mark_unresolved]

admin.site.register(FeedbackItem, FeedbackAdmin)
