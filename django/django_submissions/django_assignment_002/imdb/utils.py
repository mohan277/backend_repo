from .models import *

# actors_list = [
#         {
#             "actor_id": "actor_1",
#             "name": "Actor 1"
#         },
#         {
#             "actor_id": "actor_2",
#             "name": "Actor 2"
#         },
#         {
#             "actor_id": "actor_3",
#             "name": "Actor 3"
#         },
#         {
#             "actor_id": "actor_4",
#             "name": "Actor 4"
#         },
#         {
#             "actor_id": "actor_5",
#             "name": "Actor 5"
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
    
# Task2

def populate_database(actors_list, movies_list, directors_list, movie_rating_list):
    
    for dir_name in directors_list:
        Director.objects.create(name=dir_name)
    
    
    for act_name_id in actors_list:
        Actor.objects.create(actor_id=act_name_id['actor_id'],name=act_name_id['name'])
    
    
    for movie_attributes_dict in movies_list:
        movie_obj = Movie.objects.create(movie_id=movie_attributes_dict['movie_id'],
                                name=movie_attributes_dict['name'],
                                box_office_collection_in_crores=movie_attributes_dict['box_office_collection_in_crores'],
                                release_date=movie_attributes_dict['release_date'],
                                director=Director.objects.get(name=movie_attributes_dict['director_name']))
        
        for actor_dict in movie_attributes_dict['actors']:
            Cast.objects.create(actor=Actor.objects.get(actor_id=actor_dict['actor_id']), 
                                    role=actor_dict['role'], 
                                    is_debut_movie=actor_dict['is_debut_movie'],
                                    movie= movie_obj
                                    )
            
    
    for rating_dict in movie_rating_list:
        Rating.objects.create( movie=Movie.objects.get(movie_id=rating_dict['movie_id']),
                                rating_one_count=rating_dict['rating_one_count'],
                                rating_two_count=rating_dict['rating_two_count'],
                                rating_three_count=rating_dict['rating_three_count'],
                                rating_four_count=rating_dict['rating_four_count'],
                                rating_five_count=rating_dict['rating_five_count'])
        
        
        
        
        

# task3

def get_no_of_distinct_movies_actor_acted(actor_id):
    return Movie.objects.filter(cast__actor__actor_id=actor_id).distinct().count()


# task4

def get_movies_directed_by_director(director_obj):
    return Movie.objects.filter(director=director_obj)
    
# task5

def get_average_rating_of_movie(movie_obj):
    try:
        rating_obj = Rating.objects.get(movie=movie_obj)
        numerator = rating_obj.rating_one_count*1+rating_obj.rating_two_count*2+rating_obj.rating_three_count*3+rating_obj.rating_four_count*4+rating_obj.rating_five_count*5
        denominator = rating_obj.rating_one_count+rating_obj.rating_two_count+rating_obj.rating_three_count+rating_obj.rating_four_count+rating_obj.rating_five_count
        average = numerator/denominator
        return average
    except:
        return 0
    
# task6

def delete_movie_rating(movie_obj):
    return Rating.objects.get(movie=movie_obj).delete()

# task7

def get_all_actor_objects_acted_in_given_movies(movie_objs):
    return Actor.objects.filter(cast__movie__in=movie_objs).distinct()

# Task8

def update_director_for_given_movie(movie_obj, director_obj):
    movie_obj.director = director_obj
    movie_obj.save()

# Task 9

def get_distinct_movies_acted_by_actor_whose_name_contains_john():
    return Movie.objects.filter(cast__actor__name__contains='john').distinct()

# Task 10

def remove_all_actors_from_given_movie(movie_obj):
    movie_obj.actors.clear()
    
# Task 11

def get_all_rating_objects_for_given_movies(movie_objs):
    return Rating.objects.filter(movie__in=movie_objs)
