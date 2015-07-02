
# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from gameapi.models import World
from gameapi.serializers import WorldSerializer

class JSONResponse(HttpResponse):
  def __init__(self, data, **kwargs):
    content = JSONRenderer().render(data)
    kwargs['content_type'] = 'application/json'
    super(JSONResponse, self).__init__(content, **kwargs)

def world_list(request):
  """
  List all code worlds, or create a new world.
  """
  if request.method == 'GET':
    worlds = World.objects.all()
    serializer = WorldSerializer(worlds, many=True)
    return JSONResponse(serializer.data)

  elif request.method == 'POST':
    data = JSONParser().parse(request)
    serializer = WorldSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data, status=201)
    return JSONResponse(serializer.errors, status=400)

def world_detail(request, pk):
  """
  Retrieve, update or delete a code world.
  """
  try:
    world = World.objects.get(pk=pk)
  except World.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = WorldSerializer(world)
    return JSONResponse(serializer.data)

  elif request.method == 'PUT':
    data = JSONParser().parse(request)
    serializer = WorldSerializer(world, data=data)
    if serializer.is_valid():
      serializer.save()
      return JSONResponse(serializer.data)
    return JSONResponse(serializer.errors, status=400)

  elif request.method == 'DELETE':
    world.delete()
    return HttpResponse(status=204)
