from rest_framework import viewsets, generics

from setup.models.item import Item
from setup.serializer import DepartmentItemListSerializer, ItemSerializer

class ItemView(viewsets.ModelViewSet):
    
    queryset = Item.objects.all();
    serializer_class = ItemSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    
class DepartmentItemList(generics.ListAPIView):

    def get_queryset(self):
        queryset = Item.objects.filter(department_id=self.kwargs['pk']);
        return queryset
    
    serializer_class = DepartmentItemListSerializer