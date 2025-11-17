from django.contrib import admin
from django.utils.html import format_html
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status_badge', 'created_on', 'updated_on')
    list_filter = ('status', 'created_on', 'author')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_on', 'updated_on')
    actions = ['archive_posts', 'restore_posts']
    
    def status_badge(self, obj):
        colors = {
            0: '#ffc107',
            1: '#28a745',
            2: '#6c757d',
        }
        labels = {
            0: 'Bozza',
            1: 'Pubblicato',
            2: 'Archiviato',
        }
        color = colors.get(obj.status, '#6c757d')
        label = labels.get(obj.status, 'Sconosciuto')
        return format_html(
            '<span style="background-color: {}; color: white; padding: 3px 8px; border-radius: 3px; font-size: 11px;">{}</span>',
            color, label
        )
    status_badge.short_description = 'Stato'
    
    def archive_posts(self, request, queryset):
        count = queryset.update(status=2)
        self.message_user(request, f'{count} post archiviato/i con successo.')
    archive_posts.short_description = 'Archivia i post selezionati'
    
    def restore_posts(self, request, queryset):
        count = queryset.filter(status=2).update(status=0)
        self.message_user(request, f'{count} post ripristinato/i come bozze.')
    restore_posts.short_description = 'Ripristina come bozze'
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs