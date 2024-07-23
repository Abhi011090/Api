from django.utils.timezone import now, timedelta
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Q
from api.models import Product, ProductView
from api.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        view = ProductView(product=instance)
        view.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='top')
    def top_products(self, request):
        timeframe = request.query_params.get('timeframe', 'all')
        current_time = now()

        if timeframe == 'day':
            start_time = current_time - timedelta(days=1)
        elif timeframe == 'week':
            start_time = current_time - timedelta(weeks=1)
        else:
            start_time = None

        if start_time:
            top_products = Product.objects.annotate(view_count=Count('views', filter=Q(views__view_at__gte=start_time))).order_by('-view_count')[:5]
        else:
            top_products = Product.objects.annotate(view_count=Count('views')).order_by('-view_count')[:5]

        serializer = self.get_serializer(top_products, many=True)
        return Response(serializer.data)
