from django.db import models
from cms.models import CMSPlugin
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class FeaturedProduct(CMSPlugin):
    product = models.ForeignKey('catalogue.Product')

    def __str__(self):
        if self.product:
            return self.product.get_title()
        return ''
