# -*- coding: utf-8 -*-
from markdown2 import Markdown

from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from core.parser import Itenary, toint


class IndexView(View):
    def get(self, request, *args, **kwargs):
        with open('README.md') as f:
            readme = Markdown().convert(f.read())
        return HttpResponse(readme)


class FindView(View):
    method_name = None

    def get(self, request, *args, **kwargs):
        itenary = Itenary(
            source=request.GET.get('source'),
            dest=request.GET.get('dest'),
            back=bool(request.GET.get('back')),
            adult=toint(request.GET.get('adult')),
            child=toint(request.GET.get('child')),
            infant=toint(request.GET.get('infant')),
        )
        data = getattr(itenary, self.method_name)()
        return JsonResponse({'success': True, 'data': data}, safe=False)
