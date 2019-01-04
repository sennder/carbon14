from carbon14.django_queryset_operations import sort_instances
from unittest.mock import Mock
from unittest import TestCase


class SortInstancesTest(TestCase):
    def setUp(self):
        self.queryset = Mock()
        self.queryset.order_by.return_value = self.queryset

    def test_no_sort_order(self):
        sort_instances(self.queryset, sort_order=None)
        self.queryset.order_by.assert_called_once_with('id')

    def test_with_sort_order(self):
        sort_instances(self.queryset, sort_order='a,b')
        self.queryset.order_by.assert_called_once_with('a', 'b', 'id')

    def test_with_sort_order_with_id(self):
        sort_instances(self.queryset, sort_order='a,b,id')
        self.queryset.order_by.assert_called_once_with('a', 'b', 'id')
