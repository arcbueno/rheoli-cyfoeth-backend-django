from rest_framework import viewsets, generics

from setup.models.item import Item
from setup.serializer import DepartmentItemListSerializer, ItemSerializer

class ItemView(viewsets.ModelViewSet):
    
    queryset = Item.objects.all();
    serializer_class = ItemSerializer
    
class DepartmentItemList(generics.ListAPIView):

    def get_queryset(self):
        if(self.kwargs == None or self.kwargs['pk'] == None):
            queryset = Item.objects.all()
        queryset = Item.objects.filter(department_id=self.kwargs['pk']);
        return queryset
    
    serializer_class = DepartmentItemListSerializer