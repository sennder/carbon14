from carbon14.django_queryset_operations import sort_instances
from unittest.mock import Mock


def test_sort_instances():
    queryset = Mock()
    queryset.order_by.return_value = queryset

    sort_instances(queryset, sort_order=None)
    assert queryset.order_by.called_once_with()

    sort_instances(queryset, sort_order="a,b")
    assert queryset.order_by.called_once_with()

    sort_instances(queryset, sort_order="a,b, id")
    assert queryset.order_by.called_once_with()
