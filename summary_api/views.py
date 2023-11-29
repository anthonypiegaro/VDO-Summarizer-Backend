from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .helpers.yt_id_parser import get_id
from .helpers.get_yt_summary import get_summary
from .helpers.get_yt_title import get_video_title
from .helpers.get_yt_transcript import get_transcript
from .models import Summary, UserVideoSummary
from .serializers import UserVideoSummarySerializer, SummaryOnly


class VideoSummaryView(APIView):
    serializer_class = SummaryOnly
    permission_classes = [IsAuthenticated]

    def get(self, request, video_id):
        try:
            summary = Summary.objects.get(video_id=video_id)

            data = {"video_summary": summary.video_summary}

            return Response(data, status=status.HTTP_200_OK)
        
        except Summary.DoesNotExist:
            return Response({"detail": "Summary not found"}, status=status.HTTP_404_NOT_FOUND)


class UserVideoSummaryListView(ListAPIView):
    serializer_class = UserVideoSummarySerializer

    def get_queryset(self):
        user = self.request.user

        queryset = UserVideoSummary.objects.filter(user=user).order_by('-date')

        return queryset

class ProcessYouTubeURLView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            url = request.data.get('url')
            video_id = get_id(url)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        # check if in id in database
        try:
            summary_obj = Summary.objects.get(video_id=video_id)

            existing_record = UserVideoSummary.objects.filter(
                summary=summary_obj,
                user=request.user
            ).first()

            if not existing_record:
                # add summary obj to user history
                history = UserVideoSummary.objects.create(
                    summary=summary_obj,
                    user=request.user
                )
            
            data = {
                    "title": summary_obj.video_title,
                    "summary": summary_obj.video_summary
                }

            return Response(data, status=status.HTTP_201_CREATED)

        except Summary.DoesNotExist:
            print("Building summary")

        # get title
        try:
            video_title = get_video_title(url)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # get transcript
        try:
            transcript = get_transcript(video_id)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # get summary from openai API 
        try:
            summary = get_summary(transcript)
            print("Summary", summary)
        except Exception as e:
            return Response({'error': 'Service temporarily unavailable - please try again later.'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
    
        summary_obj = Summary.objects.create(
            video_id=video_id,
            video_summary=summary,
            video_title=video_title
        )

        history = UserVideoSummary.objects.create(
            summary=summary_obj,
            user=request.user
        )
        
        data = {"summary": summary, "title": video_title}

        return Response(data, status=status.HTTP_201_CREATED)
