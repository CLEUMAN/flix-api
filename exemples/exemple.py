'''
def genre_list_view(request):
    genres = Genre.objects.all().order_by('name')
    
    response = []
    for genre in genres:
        response.append(
            {'id': genre.id, 'name': genre.name}
        )
     
    response = [{'id': genre.id, 'name': genre.name} for genre in genres]
    return JsonResponse(response, safe=False)


@csrf_exempt
def genre_create_view(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        new_genre = Genre(name=data['name'])
        new_genre.save()
        return JsonResponse({'id': new_genre.id, 'name': new_genre.name}, status=201)

@csrf_exempt
def genre_show_view(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    data = {'id': genre.id, 'name': genre.name}
    return JsonResponse(data)

@csrf_exempt
def genre_update_view(request, pk):
     if request.method == 'PUT':
        genre = get_object_or_404(Genre, pk=pk)
        data = json.loads(request.body.decode('utf-8'))
        
        genre.name = data['name']
        genre.save()
        
        response = {'id': genre.id, 'name': genre.name}
        return JsonResponse(response)
         
@csrf_exempt
def genre_delete_view(request, pk):       
    if request.method == 'DELETE':
        genre = get_object_or_404(Genre, pk=pk)
        genre.delete()
        return JsonResponse({'mennsage':'Gênero excluído com sucesso!'}, status=204)
        
        
        
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()
'''