from unittest import TestCase

from carbon14.neonode import Collection


CHILD = "child"


class TestFieldIsAccessible(TestCase):
    def setUp(self):
        self.collection = Collection()

    def test_not_accessible_if_no_fields(self):
        setattr(self.collection, "_fields", {})

        assert not self.collection.field_is_accessible(child=CHILD)

    def test_not_accessible_if_child_not_in_fields(self):
        setattr(self.collection, "_fields", {CHILD})

        assert not self.collection.field_is_accessible(child="something else")

    def test_is_accessible_if_child_in_fields_and_no_permitted_fields(self):
        setattr(self.collection, "_fields", {CHILD})
        setattr(self.collection, "permitted_fields", None)

        assert self.collection.field_is_accessible(child=CHILD)

    def test_is_accessible_if_child_in_permitted_fields(self):
        setattr(self.collection, "_fields", {CHILD})
        setattr(self.collection, "permitted_fields", {CHILD})

        assert self.collection.field_is_accessible(child=CHILD)

    def test_not_accessible_if_child_not_in_permitted_fields(self):
        setattr(self.collection, "_fields", {CHILD})
        setattr(self.collection, "permitted_fields", {"some other field"})

        assert not self.collection.field_is_accessible(child=CHILD)
