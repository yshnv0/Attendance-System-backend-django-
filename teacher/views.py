from teacher.models import Teacher
from django.http import JsonResponse
from teacher.serializer import TeacherSerializer
def teacher(request):
    data=Teacher.objects.all()
    serializer=TeacherSerializer(data,many=True)
    return JsonResponse({'teacher': serializer.data} )


