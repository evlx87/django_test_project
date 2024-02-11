from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_category_cache():
    if settings.CACHE_ENABLED:
        key = f'category_list'
        subject_list = cache.get(key)
        if subject_list is None:
            subject_list = Category.objects.all()
            cache.set(key, subject_list)
            return subject_list
        return subject_list
