from .models import *
from django.db.models import Q
import datetime

# Task1
def average_rating(movie_obj):
    try:
        rating_obj = Rating.objects.get(movie=movie_obj)
    except:
        return 0
    denominator = rating_obj.rating_one_count + rating_obj.rating_two_count + rating_obj.rating_three_count + rating_obj.rating_four_count + rating_obj.rating_four_count
    if denominator==0:
        return 0
    else:
        numerator = rating_obj.rating_one_count*1 + rating_obj.rating_two_count*2 + rating_obj.rating_three_count*3 + rating_obj.rating_four_count*4 + rating_obj.rating_four_count*5
        return numerator/denominator

def total_number_of_ratings(movie_obj):
    try:
        rating_obj = Rating.objects.get(movie=movie_obj)
    except:
        return 0
    total = rating_obj.rating_one_count + rating_obj.rating_two_count + rating_obj.rating_three_count + rating_obj.rating_four_count + rating_obj.rating_four_count
    return total

def cast(movie_obj):
    cast_list = []
    cast_objects = Cast.objects.filter(movie=movie_obj)
    for cast_obj in cast_objects:
        cast_dict = {}
        actor_list = {}
        actor_list['name'] = cast_obj.actor.name
        actor_list['actor_id'] = cast_obj.actor.actor_id
        cast_dict['actor'] = actor_list
        cast_dict['role'] = cast_obj.role
        cast_dict['is_debut_movie'] = cast_obj.is_debut_movie
        cast_list.append(cast_dict)
    return cast_list

def movie_details_list(movie_obj):
    movies_dict = {}
    movies_dict['movie_id'] = movie_obj.movie_id
    movies_dict['name'] = movie_obj.name
    movies_dict['cast'] = cast(movie_obj)
    movies_dict['box_office_collection_in_crores'] = movie_obj.box_office_collection_in_crores
    movies_dict['release_date'] = movie_obj.release_date.strftime('%Y-%m-%d')
    movies_dict['director_name'] = movie_obj.director.name
    movies_dict['average_rating'] = average_rating(movie_obj)
    movies_dict['total_number_of_ratings'] = total_number_of_ratings(movie_obj)
    return movies_dict


def get_movies_by_given_movie_names(movie_names):
    movies_list = []
    for movie_name in movie_names:
        movie_objects = Movie.objects.filter(name=movie_name)
        for movie_obj in movie_objects:
            movies_list.append(movie_details_list(movie_obj))
    return movies_list


# Task2
def get_movies_released_in_summer_in_given_years():
    movies_list = []
    movie_objects = Movie.objects.filter(release_date__month__in=[5,6,7],release_date__year__range=(2006,2009))
    for movie_obj in movie_objects:
        movies_list.append(movie_details_list(movie_obj))
    return movies_list

# task3
def get_movie_names_with_actor_name_ending_with_smith():
    return Movie.objects.filter(cast__actor__name__iendswith='smith').values_list('name',flat=True).distinct()

# task4
def get_movie_names_with_ratings_in_given_range():
    return Movie.objects.filter(rating__rating_five_count__range=(1000,3000)).values_list('name',flat=True).distinct()

# task5
def get_movie_names_with_ratings_above_given_minimum():
    return Movie.objects.filter(Q(rating__rating_five_count__gte=500)|Q(rating__rating_four_count__gte=1000)|Q(rating__rating_three_count__gte=2000)|Q(rating__rating_two_count__gte=4000)|Q(rating__rating_one_count__gte=8000),release_date__year__gte=2001).values_list('name',flat=True).distinct()
    
# task6
def get_movie_directors_in_given_year():
    return Director.objects.filter(movie__release_date__year=2000).values_list('name',flat=True).distinct()

# task7
def get_actor_names_debuted_in_21st_century():
    return Actor.objects.filter(cast__is_debut_movie=True,cast__movie__release_date__year__range=(2001,2100)).values_list('name',flat=True)

# Task8
def get_director_names_containing_big_as_well_as_movie_in_may():
    return Movie.objects.filter(name__contains='big').filter(release_date__month=5).values_list('director',flat=True).distinct()

# Task9
def get_director_names_containing_big_and_movie_in_may():
    return Director.objects.filter(movie__name__contains='big',movie__release_date__month=5).values_list('name',flat=True).distinct()

# Task10
def reset_ratings_for_movies_in_this_year():
    return Rating.objects.filter(movie__release_date__year=2000).update(rating_one_count=0,rating_two_count=0,rating_three_count=0,rating_four_count=0,rating_five_count=0)








# Task1 not completed
# def get_movies_by_given_movie_names(movie_names):
#     movie_list = []
#     for movie_name_outer in movie_names:
#         main_dict = {
#                 "movie_id": 0,
#                 "name": '',
#                 "cast": [
#                     {
#                         "actor": {
#                             "name": '',
#                             "actor_id": 0
#                         },
#                         "role": '',
#                         "is_debut_movie": False
#                     }
#                 ],
#                 "box_office_collection_in_crores": '',
#                 "release_date": '',
#                 "director_name": '',
#                 "average_rating": 0,
#                 "total_number_of_ratings": 0
#             }
# [{'movie_id': 'movie_1',
#   'name': 'movie1',
#   'cast': [{'actor': {'name': 'actor1', 'actor_id': 'actor_1'},
#     'role': 'hero',
#     'is_debut_movie': False},
#   {'actor': {'name': 'actor3', 'actor_id': 'actor_3'},
#     'role': 'comedian',
#     'is_debut_movie': False}],
#   'box_office_collection_in_crores': 5356.0,
#   'release_date': '2020-03-01',
#   'director_name': 'director_1',
#   'average_rating': 4.3895305711560875,
#   'total_number_of_ratings': 9437}]
#         movie_objects = Movie.objects.filter(name=movie_name_outer).values('name')
#         count = movie_objects.count()
#         movie_names_inner = []
        
#         for i in range(count):
#             movie_names_inner.append(movie_objects.values('name')[i]['name'])
        
#         for movie_name in movie_names_inner:
#             movie_obj = Movie.objects.filter(name=movie_name).values('movie_id','name','release_date','box_office_collection_in_crores')
#             # Movie.objects.filter(name=movie_name).values('movie_id','name','release_date','box_office_collection_in_crores')
#             main_dict['movie_id']=movie_obj[0]['movie_id']
#             main_dict['name']=movie_obj[0]['name']
#             main_dict['release_date']=movie_obj[0]['release_date'].strftime('%Y-%m-%d')
#             main_dict['box_office_collection_in_crores']=movie_obj[0]['box_office_collection_in_crores']
            
#             try:
#                 rating_obj = Rating.objects.filter(movie__name=movie_name).values()
#             except:
#                 return 0
#             denominator = rating_obj[0]['rating_one_count']+rating_obj[0]['rating_two_count']+rating_obj[0]['rating_three_count']+rating_obj[0]['rating_four_count']+rating_obj[0]['rating_four_count']
#             numerator = (rating_obj[0]['rating_one_count']*1)+(rating_obj[0]['rating_two_count']*2)+(rating_obj[0]['rating_three_count']*3)+(rating_obj[0]['rating_four_count']*4)+(rating_obj[0]['rating_four_count']*5)
#             main_dict['total_number_of_ratings'] = denominator
#             try:
#                 main_dict['average_rating'] = numerator/denominator
#             except ZeroDivisionError:
#                 return 0
#             director_obj = Director.objects.filter(movie__name=movie_name).values()
#             main_dict['director_name'] = director_obj[0]['name']
            
#             actor_obj = Actor.objects.filter(cast__movie__name=movie_name).values('name','actor_id')
#             main_dict['cast'][0]['actor'] = actor_obj[0]
            
#             cast_obj = Cast.objects.filter(movie__name=movie_name).values()
#             m2ain_dict['cast'][0]['role'] = cast_obj[0]['role']
#             main_dict['cast'][0]['is_debut_movie'] = cast_obj[0]['is_debut_movie']
            
#             movie_list.append(main_dict)
#     return movie_list