from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PlanInfoSerializer
from .models import Plan
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

plan_price = (
    ('Arcade', 9, 90),
    ('Advanced', 12, 120),
    ('Pro', 15, 150)
)

add_ons_price = (
    ('online_service', 1, 10),
    ('larger_storage', 2, 20),
    ('customizable_profile', 2, 20)
)

def findAddOnsIndex(plan_data, add_ons_index):
    if plan_data['online_service']:
        add_ons_index.append(0)
    
    if plan_data['larger_storage']:
        add_ons_index.append(1)
    
    if plan_data['customizable_profile']:
        add_ons_index.append(2)


class PlanView(viewsets.ModelViewSet):
    serializer_class = PlanInfoSerializer
    queryset = Plan.objects.all()
    
    def create(self, request, *args, **kwargs):
        plan_data = request.data
        cost = 0
        duration = 1
        add_ons = 0
        add_ons_index = []
        
        if not plan_data['plan_duration_is_monthly']:
            duration = 2
            
        findAddOnsIndex(plan_data, add_ons_index)
            
        if add_ons_index.__len__() > 0:
            for i in add_ons_index:
                add_ons = add_ons_price[i][duration]
                        
        cost = plan_price[int(plan_data['plan_name'])-1][duration] + add_ons
        
        add_ons_list = []
        
        for i in add_ons_index:
            add_ons_list.append((add_ons_price[i][0], add_ons_price[i][duration]))
        
        summary_data = {
            'plan_name': plan_price[int(plan_data['plan_name'])-1][0],
            'plan_cost': plan_price[int(plan_data['plan_name'])-1][duration],
            'add_ons': add_ons_list,      
            'total_cost': cost,  
        }
        return Response(summary_data)
    
