from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CreateSnippetRequest:
   def __init__(self, code, title=''):
       self.title = title
       self.code = code


class CreateSnippetRequestSerializer(serializers.Serializer):
   title = serializers.CharField(required=False, allow_blank=True,
                                 max_length=100)
   code = serializers.CharField()

   def create(self, validated_data):
       return CreateSnippetRequest(**validated_data)


class CreateSnippetResponseClass:
   def __init__(self, id, title, code):
       self.id = id
       self.title = title
       self.code = code


class CreateSnippetResponseSerializer(serializers.Serializer):
   id = serializers.IntegerField()
   title = serializers.CharField(required=False, allow_blank=True,
                                 max_length=100)
   code = serializers.CharField()

   def create(self, validated_data):
       return CreateSnippetResponseClass(**validated_data)


def create_snippet_in_db(title, code):
   """
   Create and return a new `Snippet` instance, given the validated data.
   """
   from snippets.models import Snippet
   return Snippet.objects.create(title=title, code=code)



def get_snippets_in_db():
   from snippets.models import Snippet
   return Snippet.objects.all().order_by('-id')


@api_view(['POST'])
def create_snippet(request):
   serializer = CreateSnippetRequestSerializer(data=request.data)
   is_invalid_request_data = not serializer.is_valid()

   if is_invalid_request_data:
       return Response(status=400)

   request_obj = serializer.save()

   new_snippet_obj = create_snippet_in_db(
       title=request_obj.title,
       code=request_obj.code
   )

   response_serializer = CreateSnippetResponseSerializer(new_snippet_obj)
   return Response(response_serializer.data)

@api_view(['GET'])
def get_list_of_snippets(request):
    list_of_snippets = get_snippets_in_db()
    serializer = CreateSnippetResponseSerializer(list_of_snippets, many=True)
    return Response(serializer.data)
