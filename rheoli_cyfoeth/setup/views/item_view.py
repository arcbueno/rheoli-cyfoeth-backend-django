from rest_framework import viewsets, generics

from setup.models.item import Item
from setup.serializer import CreateItemSerializer, DepartmentItemListSerializer, ItemSerializer

class ItemView(viewsets.ModelViewSet):
    
    queryset = Item.objects.all();
    serializer_class = ItemSerializer
    
    # Override
    def get_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        if(self.action == 'create' or self.action == 'update' or self.action == 'partial_update'):
            serializer_class = CreateItemSerializer
        else:
            serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)
    
class DepartmentItemList(generics.ListAPIView):

    def get_queryset(self):
        if(self.kwargs == None or self.kwargs['pk'] == None):
            queryset = Item.objects.all()
        queryset = Item.objects.filter(department_id=self.kwargs['pk']);
        return queryset
    
    serializer_class = DepartmentItemListSerializer