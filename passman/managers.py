import googlemaps
from django.db import models
from django.conf import settings


class MailingAddressManager(models.Manager):

    def create(self, **kwargs):
        address_line1 = kwargs.get('address_line1')
        address_line2 = kwargs.get('address_line2', None)
        city = kwargs.get('city')
        state = kwargs.get('state')
        zip_code = kwargs.get('zip_code')
        address_str = address_line1
        if address_line2:
            address_str += ' ' + address_line2
        address = f'{address_str} {city} {state} {zip_code}'
        google_maps_key = settings.GOOGLE_MAPS_API_KEY
        gmaps = googlemaps.Client(key=google_maps_key)
        geocode_result = gmaps.geocode(address)
        if len(geocode_result) == 0:
            return False
        geocoded = geocode_result[0]
        fields = {
            'period_start': kwargs.get('period_start'),
            'period_end': kwargs.get('period_end', None),
            'address_id': geocoded['place_id'],
            'apt_suite': kwargs.get('apt_suite', None),
            'formatted_address': geocoded['formatted_address'],
            'comment': kwargs.get('comment', None)
        }
        obj = self.model(**fields)
        obj.save(force_insert=True, using=self.db)
        return obj
