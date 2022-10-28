from django.contrib import admin
from .models import OperatingSystemStats
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from .models import OperatingSystemStats

@admin.register(OperatingSystemStats)
class OperatingSystemStatsAdmin(admin.ModelAdmin):
    def admin_panel_view(self, request, extra_context=None):

        stat_data = (
            OperatingSystemStats.objects.annotate().values("win","mac","iph","android","oth")
        )

        # data = OperatingSystemStats.objects.all()
        # newdata = serializers.serialize('json', list(data), fields=("win","mac","iph","android","oth"))
        # print(newdata)

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data": as_json}

        return super().admin_panel_view(request, extra_context=extra_context)

