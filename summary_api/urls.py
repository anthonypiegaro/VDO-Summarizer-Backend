from django.urls import path

from .views import (
    ProcessYouTubeURLView, 
    UserVideoSummaryListView,
    VideoSummaryView
)

urlpatterns = [
    path("summary/", ProcessYouTubeURLView.as_view(), name="summary"),
    path("history/", UserVideoSummaryListView.as_view(), name="history"),
    path("prev-summary/<str:video_id>/", VideoSummaryView.as_view(), name="prev-summary"),
]
