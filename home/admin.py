from django.contrib import admin
from .models import ChatbotVisitorMessage, CustomerSupportRequest, CSOVisitorMessage, CSOVisitorConvoInfo
from .user_connectivity_models import ChatSupportUserOnline


class ChatbotVisitorMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'visitors_msg', 'bot_msg', 'client_ip', 'created_at']
    list_display_links = ['id']
    search_fields = ['id', 'client_ip', 'created_at']
    readonly_fields = ['created_at'] # to view these fields in the "Food" model inside the admin-panel, it's required to explicitly mention these fields as readonly fields, oetherwise they won't be visible.
    list_filter = ['created_at']
    list_per_page = 15
    ordering = ['-id']


class CustomerSupportRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_ip', 'room_slug', 'visitor_session_uuid', 'created_at']
    list_display_links = ['id']
    search_fields = list_display
    readonly_fields = ['room_slug', 'visitor_session_uuid', 'created_at'] # to view these fields in the "Food" model inside the admin-panel, it's required to explicitly mention these fields as readonly fields, oetherwise they won't be visible.
    list_filter = ['created_at']
    list_per_page = 15
    ordering = ['-id']


class CSOVisitorMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'user_identity', 'room_slug', 'created_at']
    list_display_links = ['id']
    search_fields = list_display
    readonly_fields = ['room_slug', 'created_at'] # to view these fields in the "Food" model inside the admin-panel, it's required to explicitly mention these fields as readonly fields, oetherwise they won't be visible.
    list_filter = ['user_identity', 'created_at']
    list_per_page = 15
    ordering = ['-id']


class CSOVisitorConvoInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_slug', 'cso_email', 'is_resolved', 'is_connected', 'created_at']
    list_display_links = ['id']
    search_fields = list_display[:-1]   # except the "created_at" field
    # readonly_fields = ['room_slug', 'created_at']
    readonly_fields = ['created_at']
    list_filter = ['is_resolved', 'is_connected', 'created_at']
    list_per_page = 15
    ordering = ['-id']


class ChatSupportUserOnlineAdmin(admin.ModelAdmin):
    list_display = ['id', 'cso_email', 'visitor_session_uuid', 'room_slug', 'is_active', 'joined_at', 'last_update',]
    list_display_links = ['id']
    search_fields = list_display[:-3]   # except the "is_active", "joined_at" & "last_update" fields
    # readonly_fields = ['room_slug', 'created_at']
    readonly_fields = ['room_slug', 'joined_at', 'last_update',]
    list_filter = ['is_active', 'joined_at', 'last_update',]
    list_per_page = 15
    ordering = ['-id']


admin.site.register(ChatbotVisitorMessage, ChatbotVisitorMessageAdmin)
admin.site.register(CustomerSupportRequest, CustomerSupportRequestAdmin)
admin.site.register(CSOVisitorMessage, CSOVisitorMessageAdmin)
admin.site.register(CSOVisitorConvoInfo, CSOVisitorConvoInfoAdmin)

# User online connectivity models
admin.site.register(ChatSupportUserOnline, ChatSupportUserOnlineAdmin)
