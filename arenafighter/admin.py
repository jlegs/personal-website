from django.contrib import admin
from arenafighter.models.character import Player
from arenafighter.models.equipment import Inventory, InventoryItem, Armor, Weapon
from arenafighter.models.enemy import Enemy
from arenafighter.models.profile_model import Profile


class PlayerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Player, PlayerAdmin)


class InventoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Inventory, InventoryAdmin)


class InventoryItemAdmin(admin.ModelAdmin):
    pass
admin.site.register(InventoryItem, InventoryItemAdmin)


class ArmorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Armor, ArmorAdmin)


class WeaponAdmin(admin.ModelAdmin):
    pass
admin.site.register(Weapon, WeaponAdmin)


class EnemyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Enemy, EnemyAdmin)


class ProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(Profile, ProfileAdmin)


