movie_list = []

def display_menu():
    print('1. Add a movie')
    print('2. View all  movies')
    print('3. Count watched vs unwatched')
    print('4. Find a movie')
    print('5. Exit')

def add_movie(movie_list):
    movie_tile = input('Enter movie title: ')
    director = input('Enter the director: ')
    status = input('Watcher or Unwatched: ')

    movie = (f'{movie_tile} - {director} - {status}')

    movie_list.append(movie)
    print('Movie Addded Successfully')

def view_movies(movie_list):

    listlength = (len(movie_list))

    if listlength == 0:
        print('No movies in the collection')
    else:
        print('=== All Movies ===')
        for i in movie_list:
            print(i)

def count_watched_unwatched(movie_list):
    pass


def find_movie(movie_list):
    title = input('Enter the title of the movie: ')

    for x in movie_list:
        if title in x:
            print('Movie found!')
            print(x)
        else:
            print('Movie not found.')

def main():
    while True:
        print('=== Movie Collection Manager ===')
        display_menu()
        choice = int(input('Choose an option: '))

        if choice == 1:
            add_movie(movie_list)
        elif choice == 2:
            view_movies(movie_list)
        elif choice == 3:
            print(' Counted watched and unwatched')
        elif choice == 4:
            find_movie(movie_list)
        elif choice == 5:
            print('Exiting')
            break

main()