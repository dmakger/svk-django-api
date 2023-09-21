class Order:
    @staticmethod
    def _get_valid_order(order=None):
        if order is None:
            return []
        if type(order) is not list:
            return [order]
        return order

    @staticmethod
    def by(queryset, request=None, order=None):
        system_order = Order._get_valid_order(order)
        user_order = []
        if request is not None:
            user_order = Order._get_valid_order(request.query_params.getlist('order_by'))
        return queryset.order_by(*user_order, *system_order)
