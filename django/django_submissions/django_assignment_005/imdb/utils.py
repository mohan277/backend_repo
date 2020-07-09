from .models import *
from collections import *

# actors_list = [
#         {
#             "actor_id": "actor_1",
#             "name": "Actor 1",
#             "gender":"MALE"
#         },
#         {
#             "actor_id": "actor_2",
#             "name": "Actor 2",
#             "gender":"MALE"
#         },
#         {
#             "actor_id": "actor_3",
#             "name": "Actor 3",
#             "gender":"FEMALE"
#         },
#         {
#             "actor_id": "actor_4",
#             "name": "Actor 4",
#             "gender":"MALE"
#         },
#         {
#             "actor_id": "actor_5",
#             "name": "Actor 5",
#             "gender":"FEMALE"
#         }
#     ]

# movies_list = [
#         {
#             "movie_id": "movie_1",
#             "name": "Movie 1",
#             "actors": [
#                 {
#                     "actor_id": "actor_1",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 1"
#         },
#         {
#             "movie_id": "movie_2",
#             "name": "Movie 2",
#             "actors": [
#                 {
#                     "actor_id": "actor_2",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 2"
#         },
#         {
#             "movie_id": "movie_3",
#             "name": "Movie 3",
#             "actors": [
#                 {
#                     "actor_id": "actor_3",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 3"
#         },
#         {
#             "movie_id": "movie_4",
#             "name": "Movie 4",
#             "actors": [
#                 {
#                     "actor_id": "actor_4",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 4"
#         },
#         {
#             "movie_id": "movie_5",
#             "name": "Movie 5",
#             "actors": [
#                 {
#                     "actor_id": "actor_5",
#                     "role": "hero",
#                     "is_debut_movie": False
#                 }
#             ],
#             "box_office_collection_in_crores": "12.3",
#             "release_date": "2020-3-3",
#             "director_name": "Director 5"
#         }
        
#     ]
    
# directors_list = [
#         "Director 1","Director 2","Director 3","Director 4","Director 5"
#     ]

# movie_rating_list = [
#         {
#             "movie_id": "movie_1",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_2",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_3",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_4",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         },
#         {
#             "movie_id": "movie_5",
#             "rating_one_count": 4,
#             "rating_two_count": 4,
#             "rating_three_count": 4,
#             "rating_four_count": 4,
#             "rating_five_count": 4
#         }
#     ]


# Task 1
def populate_database(actors_list, movies_list, directors_list, movie_rating_list):
    
    
    
    Director.objects.bulk_create([Director(name=director) for director in directors_list])
        
    Actor.objects.bulk_create([Actor(gender=actor['gender'], actor_id=actor['actor_id'], name=actor['name']) for actor in actors_list])
    
    dir_objs = Director.objects.all()
    
    def dir_fun(dir_name):
        for dir_obj in dir_objs:
            if dir_obj.name == dir_name:
                return dir_obj
        
    Movie.objects.bulk_create(
        [Movie(
            movie_id=movie['movie_id'],
            name=movie['name'],
            box_office_collection_in_crores=movie['box_office_collection_in_crores'],
            release_date=movie['release_date'],
            director=dir_fun(movie['director_name'])) for movie in movies_list])
    
    Cast.objects.bulk_create(
        [Cast(
            actor_id=actor['actor_id'], 
            role=actor['role'],
            is_debut_movie=actor['is_debut_movie'],
            movie_id= movie['movie_id']) for movie in movies_list for actor in movie['actors']])
            
    Rating.objects.bulk_create(
        [Rating(
            movie_id=ratings['movie_id'],
            rating_one_count=ratings['rating_one_count'],
            rating_two_count=ratings['rating_two_count'],
            rating_three_count=ratings['rating_three_count'],
            rating_four_count=ratings['rating_four_count'],
            rating_five_count=ratings['rating_five_count']) for ratings in movie_rating_list])

# Task 2
def remove_all_actors_from_given_movie(movie_object):
    Cast.objects.filter(movie=movie_object).delete()

# Task 3
def get_all_rating_objects_for_given_movies(movie_objs):
    return Rating.objects.filter(movie__in=movie_objs)

# Task 4
def get_movies_by_given_movie_names(movie_names):
    cast_objs = Cast.objects.filter(movie__name__in=movie_names).select_related('movie','actor','movie__rating','movie__director')
    
    cast = defaultdict(list)
    for cast_obj in cast_objs:
        cast[cast_obj.movie].append(cast_obj)
        
    movie_details_final_list = []
    for movie_obj,cast_objs in cast.items():
        movie_details_final_list.append(movie_details(movie_obj,cast_objs))
    return movie_details_final_list

def movie_details(movie_obj,cast_objs):
    movie_dict = {}
    movie_dict['movie_id'] = movie_obj.movie_id
    movie_dict['name'] = movie_obj.name
    movie_dict['cast'] = cast_func(cast_objs)
    movie_dict['box_office_collection_in_crores'] = movie_obj.box_office_collection_in_crores
    movie_dict['release_date'] = str(movie_obj.release_date)
    movie_dict['director_name'] = movie_obj.director.name
    movie_dict['average_rating'] = avg_rating_func(movie_obj)
    movie_dict['total_number_of_ratings'] = total_number_of_ratings(movie_obj)
    return movie_dict
    
def cast_func(cast_objs):
    
    cast_list = []
    
    for cast_obj in cast_objs:
        actor_dict = {}
        cast_dict = {}
        actor_dict['name'] = cast_obj.actor.name
        actor_dict['actor_id'] = cast_obj.actor.actor_id
        cast_dict['actor'] = actor_dict
        cast_dict['role'] = cast_obj.role
        cast_dict['is_debut_movie'] = cast_obj.is_debut_movie
        cast_list.append(cast_dict)
    return cast_list
        
        
def avg_rating_func(movie_obj):
    try:
        numerator = movie_obj.rating.rating_one_count*1 + movie_obj.rating.rating_two_count*2 + movie_obj.rating.rating_three_count*3 + movie_obj.rating.rating_four_count*4 + movie_obj.rating.rating_five_count*5
        denominator = movie_obj.rating.rating_one_count + movie_obj.rating.rating_two_count + movie_obj.rating.rating_three_count + movie_obj.rating.rating_four_count + movie_obj.rating.rating_five_count
        avg_rating = numerator/denominator    
        return avg_rating
    except:
        return 0

def total_number_of_ratings(movie_obj):
    try:
        numerator = movie_obj.rating.rating_one_count*1 + movie_obj.rating.rating_two_count*2 + movie_obj.rating.rating_three_count*3 + movie_obj.rating.rating_four_count*4 + movie_obj.rating.rating_five_count*5
        return numerator
    except:
        return 0
# Task 5
def get_all_actor_objects_acted_in_given_movies(movie_objs):
    pass

# Task 7
def get_actor_movies_released_in_year_greater_than_or_equal_to_2000():
    cast_objs = Cast.objects.filter(movie__release_date__year__gte=2000).select_related('movie','actor','movie__rating','movie__director')
    
    actor_details_final_list = []
    
    actor_objs_dict = defaultdict(list)
    
    for cast_obj in cast_objs:
        actor_objs_dict[cast_obj.actor].append(cast_obj)
    
    for actor_obj,cast_objs in actor_objs_dict.items():
        actor_details_final_list.append(cast_details(actor_obj,cast_objs))
    return actor_details_final_list

def cast_details(actor_obj,cast_objs):
    cast_dict = {}
    cast_dict['name'] = actor_obj.name
    cast_dict['actor_id'] = actor_obj.actor_id
    cast_dict['movies'] = movies_list(cast_objs)
    return cast_dict
    
def movies_list(cast_objs):
    movies_list = []
    for cast_obj in cast_objs:
        movie_dict = {}
        movie_dict['movie_id'] = cast_obj.movie.movie_id
        movie_dict['name'] = cast_obj.movie.name
        movie_dict['cast'] = cast_details_list(cast_obj)
        movie_dict['box_office_collection_in_crores'] = cast_obj.movie.box_office_collection_in_crores
        movie_dict['release_date'] = str(cast_obj.movie.release_date)
        movie_dict['director_name'] = cast_obj.movie.director.name
        movie_dict['average_rating'] = avg_rating_func(cast_obj.movie)
        movie_dict['total_number_of_ratings'] = total_number_of_ratings(cast_obj.movie)
        movies_list.append(movie_dict)
    return movies_list
    
def cast_details_list(cast_obj):
    cast_list = []
    cast_dict = {}
    cast_dict['role'] = cast_obj.role
    cast_dict['is_debut_movie'] = cast_obj.is_debut_movie
    cast_list.append(cast_dict)
    return cast_list