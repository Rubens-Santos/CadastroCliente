from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario
@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm
    form = CustomUsuarioChangeForm
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'username', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissões', {'fields': ('is_active', 'is_staff',   'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )


    def get_queryset(self, request):

        qs = super(CustomUsuarioAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs

        return qs.filter(username=request.user)






