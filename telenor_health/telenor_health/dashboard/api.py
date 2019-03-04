from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from models import FactTable, Fact2
from serializers import FactSerializer


class FactList(generics.ListCreateAPIView):
    queryset = FactTable.objects.all()
    serializer_class = FactSerializer


class ReportApiView(APIView):
    """

    """
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.AllowAny,)

    def get(self, request, format=None):
        facts = Fact2.objects.all()
        report = {}
        report['total_member'] = facts.count()

        renewal_trend = {}
        renew_list = []
        renew_list.append(facts.filter(number_of_renew_performed=None).count())
        renew_list.append(facts.filter(number_of_renew_performed=1).count())
        renew_list.append(facts.filter(number_of_renew_performed=2).count())
        renew_list.append(facts.filter(number_of_renew_performed=3).count())
        renew_list.append(facts.filter(number_of_renew_performed=4).count())
        renew_list.append(facts.filter(number_of_renew_performed=5).count())
        renew_list.append(facts.filter(number_of_renew_performed__gte=6).count())
        renewal_trend['renewal_trend'] = renew_list
        report['renewal_trend'] = renewal_trend

        subscription_trend = {}
        subscription_trend['unpaid_subscriber'] = facts.filter(number_of_paid_subscription=None).count()
        subscription_trend['paid_subscriber'] = report['total_member'] - subscription_trend['unpaid_subscriber']
        report['subscription_trend'] = subscription_trend

        channel_identification_rate = {}
        channels = [channel['first_retailer_or_channel'] for channel in facts.values('first_retailer_or_channel').distinct()]
        for channel in channels:
            channel_identification_rate[channel] = facts.filter(first_retailer_or_channel=channel).count()
        report['channel_identification_rate'] = channel_identification_rate

        average_membership_duration={}
        average_membership_duration['1 to 10 days'] = facts.filter(avg_membership_duration__lte=10).count()
        average_membership_duration['10 to 20 days'] = facts.filter(avg_membership_duration__lte=20).count()
        average_membership_duration['20 to 30 days'] = facts.filter(avg_membership_duration__lte=30).count()
        average_membership_duration['more than 30 days'] = facts.filter(avg_membership_duration__gte=30).count()
        report['average_membership_duration'] = average_membership_duration

        return Response(report)
