from .models import *
from django.db.models import *

# Task 1
def get_average_box_office_collections():
    try:
        movie_objs = Movie.objects.aggregate(Avg('box_office_collection_in_crores'))
        return round(movie_objs['box_office_collection_in_crores__avg'],3)
    except:
        return 0

# Task 2
def get_movies_with_distinct_actors_count():
    return list(Movie.objects.annotate(actors_count = Count('actors',distinct=True)))

# Task 3
def get_male_and_female_actors_count_for_each_movie():
    return list(Movie.objects.annotate(
        male_actors_count = Count('actors',distinct=True,filter = Q(actors__gender = 'MALE')),
        female_actors_count = Count('actors',distinct=True,filter = Q(actors__gender = 'FEMALE'))))

# Task 4
def get_roles_count_for_each_movie():
    return list(Movie.objects.annotate(roles_count = Count('cast__role',distinct=True)))

# Task 5
def get_role_frequency():
    return dict(Cast.objects.values_list('role').annotate(roles_count = Count('actor',distinct=True)))

# Task 6
def get_role_frequency_in_order():
    return list(Cast.objects.values_list('role').annotate(roles_count = Count('actor',distinct=True)).order_by('-movie__release_date'))

# Task 7
def get_no_of_movies_and_distinct_roles_for_each_actor():
    return list(Actor.objects.annotate(movies_count = Count('cast__movie',distinct=True), roles_count = Count('cast__role',distinct=True)))

# Task 8
def get_movies_with_atleast_forty_actors():
    return list(Movie.objects.annotate(actors_count = Count('actors',distinct=True)).filter(actors_count__gte=40))

# Task 9
def get_average_no_of_actors_for_all_movies():
    try:
        movie_objs = Movie.objects.annotate(actors_count = Count('actors')).aggregate(Avg('actors_count'))
        return round(movie_objs['actors_count__avg'],3)
    except:
        return 0
