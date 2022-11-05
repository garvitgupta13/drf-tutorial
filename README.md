# drf-tutorial

<hr/>

-   Create env -> `python -m venv env `
-   Activate env -> `.\env\Scripts\activate`
-   Install required libraries

```
pip install django
pip install djangorestframework
pip install pygments
```

<hr>

## Tutorial1 - Serialization

-   Create new project `django-admin startproject tutorial1_serialization`
-   Create new app name `snippets` inside project

```
cd .\tutorial1_serialization\
python manage.py startapp snippets
```

-   Create an initial migration for our snippet model, and sync the database for the first time

```
python manage.py makemigrations snippets
python manage.py migrate snippets
```

<b>Serialization</b> : Convert complex data types(querset, model instance) to python native data types (dict)
<b>JSON Rendering</b> : Convert python data types to JSON format to share response

```
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

snippet = Snippet(code='print("hello, world")\n')
snippet.save() ->model instance

serializer = SnippetSerializer(snippet) #serializing model instance
serializer.data -> python dict

serializer2 = SnippetSerializer(Snippet.objects.all(), many=True) #serializing queryset
serializer2.data ->list of dicts

print(type(serializer.data))
<class 'rest_framework.utils.serializer_helpers.ReturnDict'>

content = JSONRenderer().render(serializer.data)
content -> JSON
print(type(content))
<class 'bytes'>
```

<b>Deserialization</b>: Convert JSON to complex data types

```
import io

stream = io.BytesIO(content)
data = JSONParser().parse(stream)
stream -> <class '_io.BytesIO'>
data -> dict

serializer = SnippetSerializer(data=data)
serializer.is_valid() -> validate dict

serializer.validated_data
# OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
serializer.save() -? creates a model instance
# <Snippet: Snippet object>
```

<hr/>

## Tutorial2 - Requests and Responses

-   Request object is the `request.data` attribute
-   REST framework provides two wrappers you can use to write API views.
    -   The @api_view decorator for working with function based views.
    -   The APIView class for working with class-based views.
