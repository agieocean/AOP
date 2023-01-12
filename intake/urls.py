from django.urls import path

from .views import AOPCoreAbuserView, AOPCoreReportView, AOPCoreWorkPlaceView, Index, thanks

urlpatterns = [
    path('', Index.index, name='index'),
    path('aop-abuser/', AOPCoreAbuserView.abuser, name="AOPCoreAbuser"),
    path('aop-report/', AOPCoreReportView.report, name="AOPCoreReport"),
    path('aop-workplace/', AOPCoreWorkPlaceView.workplace, name="AOPCoreWorkplace"),
    path('thanks/', thanks.thanks, name="thanks"),
]