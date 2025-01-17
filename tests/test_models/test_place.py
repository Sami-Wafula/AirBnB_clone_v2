#!/usr/bin/python3
""" """
import os

from tests.test_models.test_base_model import TestBasemodel
from models.place import Place


class TestPlace(TestBasemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertNotEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ """
        new = self.value()
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertEqual(type(new.amenity_ids), list)
