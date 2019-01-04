def sort_instances(instances, sort_order):
    sort_order_list = []
    if sort_order:
        sort_order_list += sort_order.split(',')
    # Sort by ID as lowest priority to make sort order deterministic
    if 'id' not in sort_order_list:
        sort_order_list.append('id')
    return instances.order_by(*sort_order_list)


def paginate_instances(instances, offset, limit):
    instances = instances[offset:]
    if limit:
        instances = instances[:limit]
    return instances
