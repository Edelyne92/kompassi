from django.test import TestCase


from core.models import Event, Person

from .models import LabourEventMeta, Qualification, JobCategory


class LabourEventAdminTest(TestCase):
    def test_event_adminship(self):
        person, unused = Person.get_or_create_dummy(superuser=False)
        labour_event_meta, unused = LabourEventMeta.get_or_create_dummy()

        assert not labour_event_meta.is_user_admin(person.user)

        labour_event_meta.admin_group.user_set.add(person.user)

        assert labour_event_meta.is_user_admin(person.user)

    def test_event_adminship_superuser(self):
        person, unused = Person.get_or_create_dummy(superuser=True)
        labour_event_meta, unused = LabourEventMeta.get_or_create_dummy()

        assert labour_event_meta.is_user_admin(person.user)

    def test_qualifications(self):
        person, unused = Person.get_or_create_dummy()
        qualification1, qualification2 = Qualification.get_or_create_dummies()
        jc1, jc2 = JobCategory.get_or_create_dummies()

        jc1.required_qualifications.add(qualification1)

        assert not jc1.is_person_qualified(person)
        assert jc2.is_person_qualified(person)

        person.personqualification_set.create(qualification=qualification2)

        assert not jc1.is_person_qualified(person)
        assert jc2.is_person_qualified(person)

        person.personqualification_set.create(qualification=qualification1)

        assert jc1.is_person_qualified(person)
        assert jc2.is_person_qualified(person)