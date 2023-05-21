from data import *
from linkedlist import LinkedList

def insert_movie_types():
    movie_type_list = LinkedList()
    for movie_type in types:
        movie_type_list.insert_beginning(movie_type)
    return movie_type_list

def insert_movies():
    movie_list = LinkedList()
    for movie_type in types:
        movie_sublist = LinkedList()
        for movie in movies:
            if movie[0] == movie_type:
                movie_sublist.insert_beginning(movie)
        movie_list.insert_beginning(movie_sublist)
    return movie_list

my_movie_type_list = insert_movie_types()
my_movie_list = insert_movies()

selected_movie_type = ""

while len(selected_movie_type) == 0:
    user_input = str(input("What type of movie would you like to watch? ")).lower()

    matching_types = []
    type_list_head = my_movie_type_list.get_head_node()
    while type_list_head is not None:
        if str(type_list_head.get_value()).startswith(user_input):
            matching_types.append(type_list_head.get_value())
        type_list_head = type_list_head.get_next_node()

    for type in matching_types:
        print(type)
    
    if len(matching_types) == 1:
        select_type = str(input("The only genre of movie that matches that input is " + matching_types[0] + ". Do you want to look at the top imdb rated movies in " + 
                                matching_types[0] + "? Enter y for yes or n for no: ")).lower()
        
        if select_type == 'y':
            selected_movie_type = matching_types[0]
            print("You've selected the genre: " + selected_movie_type)
            movie_list_head = my_movie_list.get_head_node()
            while movie_list_head.get_next_node() is not None:
                sublist_head = movie_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_movie_type:
                    while sublist_head.get_next_node() is not None:
                        print("--------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Imdb rating: " + str(sublist_head.get_value()[2]))
                        print("Imdb rank: " + str(sublist_head.get_value()[3]))
                        print("Year: " + str(sublist_head.get_value()[4]))
                        print("--------\n")
                        sublist_head = sublist_head.get_next_node()
                movie_list_head = movie_list_head.get_next_node()

            repeat_loop = str(input("\nDo you want to look up other movies? Enter y for yes or n for no: ")).lower()
            if repeat_loop == "y":
                selected_movie_type = ""

