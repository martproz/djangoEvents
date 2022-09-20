from django.test import TestCase

from events.models import *

@classmethod
class VenueModelTest(TestCase):

    def setUpTestData(cls):
        Venue.objects.create(name="Roman", adress="Calle Falsa", zip_code="1234", phone="1123112344", web="www.crud.com", email_adress="rcolombo@gmail.com")

    def test_name_label(self):
        venue= Venue.objects.get(id=1)
        field_label = venue._meta.get_field("name").verbose_name
        self.assertEquals(field_label,"name")

    def test_name_max_length(self):
        venue= Venue.objects.get(id=1)
        max_length = venue._meta.get_field("name").max_length
        self.assertEquals(max_length,120)

    def test_adress_label(self):
        venue= Venue.objects.get(id=1)
        field_label = venue._meta.get_field("adress").verbose_name
        self.assertEquals(field_label,"adress")

    def test_adress_max_length(self):
        venue= Venue.objects.get(id=1)
        max_length = venue._meta.get_field("adress").max_length
        self.assertEquals(max_length,300)

    def test_zip_code_label(self):
        venue= Venue.objects.get(id=1)
        field_label = venue._meta.get_field("zip_code").verbose_name
        self.assertEquals(field_label,"zip_code")

    def test_zip_code_max_length(self):
        venue= Venue.objects.get(id=1)
        max_length = venue._meta.get_field("zip_code").max_length
        self.assertEquals(max_length,300)

    def test_phone_label(self):
        venue= Venue.objects.get(id=1)
        field_label = venue._meta.get_field("phone").verbose_name
        self.assertEquals(field_label,"phone")

    def test_phone_max_length(self):
        venue= Venue.objects.get(id=1)
        max_length = venue._meta.get_field("phone").max_length
        self.assertEquals(max_length,300)

    def test_web_label(self):
        venue= Venue.objects.get(id=1)
        field_label = venue._meta.get_field("web").verbose_name
        self.assertEquals(field_label,"web")

    def test_web_max_length(self):
        venue= Venue.objects.get(id=1)
        max_length = venue._meta.get_field("web").max_length
        self.assertEquals(max_length,300)
    
    def test_email_adress_label(self):
        venue= Venue.objects.get(id=1)
        field_label = venue._meta.get_field("email_adress").verbose_name
        self.assertEquals(field_label,"email_adress")

    def test_email_adress_max_length(self):
        venue= Venue.objects.get(id=1)
        max_length = venue._meta.get_field("email_adress").max_length
        self.assertEquals(max_length,300)

    def test_get_absolute_url_movie(self):
        venue= Venue.objects.get(id=1)
        self.assertEquals(venue.get_absolute_url(),"/events/venue/1")

@classmethod
class MyClubUserModelTest(TestCase):

    def setUpTestData(cls):
        MyClubUser.objects.create(first_name="Roman", last_name="Colombo", email="rcolombo@gmail.com")

    def test_first_name_label(self):
        myclubuser= MyClubUser.objects.get(id=1)
        field_label = myclubuser._meta.get_field("first_name").verbose_name
        self.assertEquals(field_label,"first_name")

    def test_first_name_max_length(self):
        myclubuser= MyClubUser.objects.get(id=1)
        max_length = myclubuser._meta.get_field("first_name").max_length
        self.assertEquals(max_length,50)

    def test_last_name_label(self):
        myclubuser= MyClubUser.objects.get(id=1)
        field_label = myclubuser._meta.get_field("last_name").verbose_name
        self.assertEquals(field_label,"last_name")

    def test_last_name_max_length(self):
        myclubuser= MyClubUser.objects.get(id=1)
        max_length = myclubuser._meta.get_field("last_name").max_length
        self.assertEquals(max_length,400)

    def test_email_label(self):
        myclubuser= MyClubUser.objects.get(id=1)
        field_label = myclubuser._meta.get_field("email").verbose_name
        self.assertEquals(field_label,"email")

    def test_email_max_length(self):
        myclubuser= MyClubUser.objects.get(id=1)
        max_length = myclubuser._meta.get_field("email").max_length
        self.assertEquals(max_length,50)

    def test_get_absolute_url_entrada(self):
        myclubuser= MyClubUser.objects.get(id=1)
        self.assertEquals(myclubuser.get_absolute_url(),"/events/myclubuser/1")

@classmethod
class EventModelTest(TestCase):

    def setUpTestData(cls):
        Event.objects.create(name="Roman", event_date="12/12/22", venue="", manager="Carlos", description="OK", attendees="myclubuser")

    def test_name_label(self):
        event= Event.objects.get(id=1)
        field_label = event._meta.get_field("name").verbose_name
        self.assertEquals(field_label,"name")

    def test_nombre_max_length(self):
        event= Event.objects.get(id=1)
        max_length = event._meta.get_field("nombre").max_length
        self.assertEquals(max_length,60)

    def test_event_date_label(self):
        event= Event.objects.get(id=1)
        field_label = event._meta.get_field("event_date").verbose_name
        self.assertEquals(field_label,"event_date")

    def test_event_date_max_length(self):
        event= Event.objects.get(id=1)
        max_length = event._meta.get_field("event_date").max_length
        self.assertEquals(max_length,400)
    
    def test_venue_label(self):
        event= Event.objects.get(id=1)
        field_label = event._meta.get_field("venue").verbose_name
        self.assertEquals(field_label,"venue")

    def test_venue_max_length(self):
        event= Event.objects.get(id=1)
        max_length = event._meta.get_field("venue").max_length
        self.assertEquals(max_length,400)

    def test_manager_label(self):
        event= Event.objects.get(id=1)
        field_label = event._meta.get_field("manager").verbose_name
        self.assertEquals(field_label,"manager")

    def test_manager_max_length(self):
        event= Event.objects.get(id=1)
        max_length = event._meta.get_field("manager").max_length
        self.assertEquals(max_length,400)
    
    def test_description_label(self):
        event= Event.objects.get(id=1)
        field_label = event._meta.get_field("description").verbose_name
        self.assertEquals(field_label,"description")

    def test_description_max_length(self):
        event= Event.objects.get(id=1)
        max_length = event._meta.get_field("description").max_length
        self.assertEquals(max_length,400)

    def test_attendees_label(self):
        event= Event.objects.get(id=1)
        field_label = event._meta.get_field("attendees").verbose_name
        self.assertEquals(field_label,"attendees")

    def test_attendees_max_length(self):
        event= Event.objects.get(id=1)
        max_length = event._meta.get_field("attendees").max_length
        self.assertEquals(max_length,400)

    def test_get_absolute_url_comentario(self):
        event= Event.objects.get(id=1)
        self.assertEquals(event.get_absolute_url(),"/events/event/1")