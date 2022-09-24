from django.test import TestCase

from events.forms import *

@classmethod
class EventFormTest(TestCase):

    def test_name_text_field_label(self):
        form = EventForm()
        self.asserTrue(form.fields["name"].label==None or form.fields["name"].label=="name")

    def test_event_date_text_field_label(self):
        form = EventForm()
        self.asserTrue(form.fields["event_date"].label==None or form.fields["event_date"].label=="event_date")

    def test_venue_text_field_label(self):
        form = EventForm()
        self.asserTrue(form.fields["venue"].label==None or form.fields["venue"].label=="venue")

    def test_manager_text_field_label(self):
        form = EventForm()
        self.asserTrue(form.fields["manager"].label==None or form.fields["manager"].label=="manager")

    def test_attendees_text_field_label(self):
        form = EventForm()
        self.asserTrue(form.fields["attendees"].label==None or form.fields["attendees"].label=="attendees")

    def test_description_text_field_label(self):
        form = EventForm()
        self.asserTrue(form.fields["description"].label==None or form.fields["description"].label=="description")

@classmethod
class VenueFormTest(TestCase):

    def test_name_text_field_label(self):
        form = VenueForm()
        self.asserTrue(form.fields["name"].label==None or form.fields["name"].label=="name")

    def test_adress_text_field_label(self):
        form = VenueForm()
        self.asserTrue(form.fields["adress"].label==None or form.fields["adress"].label=="adress")

    def test_zip_code_text_field_label(self):
        form = VenueForm()
        self.asserTrue(form.fields["zip_code"].label==None or form.fields["zip_code"].label=="zip_code")

    def test_phone_text_field_label(self):
        form = VenueForm()
        self.asserTrue(form.fields["phone"].label==None or form.fields["phone"].label=="phone")

    def test_web_text_field_label(self):
        form = VenueForm()
        self.asserTrue(form.fields["web"].label==None or form.fields["web"].label=="web")

    def test_email_adress_text_field_label(self):
        form = VenueForm()
        self.asserTrue(form.fields["email_adress"].label==None or form.fields["email_adress"].label=="email_adress")