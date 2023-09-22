import logging

logging.getLogger('file')

from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import CloudLogin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from .serializers import CloudLoginSerializer


from django.http import JsonResponse
from .models import CloudLogin
import boto3
import csv

from .forms import AccountIdForm

class CloudLoginViewSet(generics.CreateAPIView):
    queryset = CloudLogin.objects.all()
    serializer_class = CloudLoginSerializer

def enter_account_id(request):
    if request.method == 'POST':
        form = AccountIdForm(request.POST)
        if form.is_valid():
            account_id = form.cleaned_data['account_id']
            # Retrieve the AWS credentials from the database
            try:
                aws_credentials = CloudLogin.objects.get(account_id=account_id)
                #return render(request, 'fetch_instances.html', {'aws_credentials': aws_credentials})
                return redirect('fetch-instances', account_id=account_id)
            except CloudLogin.DoesNotExist:
                return render(request, 'error.html', {'message': 'AWS credentials not found for the provided Account ID'})
        else:
            return render(request, 'error.html', {'message': 'Invalid form data'})

    form = AccountIdForm()
    return render(request, 'account_id_form.html', {'form': form})


def fetch_instances(request, account_id):
    try:
        aws_credentials = CloudLogin.objects.get(account_id=account_id)
        ec2 = boto3.client(
            'ec2',
            aws_access_key_id=aws_credentials.access_key,
            aws_secret_access_key=aws_credentials.secret_key,
            region_name='us-east-1'
        )
        print("aws_secret_access_key")
        instances = ec2.describe_instances()

        # Process instances data as needed
        instance_list = []
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_list.append({
                    'InstanceId': instance['InstanceId'],
                    'InstanceType': instance['InstanceType'],
                    'LaunchTime': instance['LaunchTime'],
                    'ImageId': instance['ImageId'],
                })

        return render(request, 'fetch_instances.html', {'instances': instance_list})
    except CloudLogin.DoesNotExist:
        return render(request, 'error.html', {'message': 'AWS credentials not found for the provided Account ID'})
    except Exception as e:
        return render(request, 'error.html', {'message': str(e)})
