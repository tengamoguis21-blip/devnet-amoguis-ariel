movie_list = []

def display_menu():
    print('1. Add a movie')
    print('2. View all  movies')
    print('3. Count watched vs unwatched')
    print('4. Find a movie')
    print('5. Remove a movie')
    print('6. Exit')

def add_movie(movie_list):
    movie_tile = input('Enter movie title: ')
    director = input('Enter the director: ')
    status = input('Watched or Unwatched: ')

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
    watched_count = 0
    unwatched_count = 0
    
    for x in movie_list:
        if 'unwatched' in x:
            unwatched_count += 1
        else:
            watched_count += 1
            
    print(f"Watched: {watched_count}")
    print(f"Unwatched: {unwatched_count}")
    return watched_count, unwatched_count

def find_movie(movie_list):

    title = input('Enter the title of the movie: ')

    for x in movie_list:
        if title in x:
            print('Movie found!')
            print(x)
        else:
            print('Movie not found.')

def remove_movie(movie_list):
    title = input('Enter the title of the movie: ')

    for x in movie_list:
            if title in x:
                print('Movie found.')
                movie_list.remove(x)
                print('Movie deleted.')
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
            count_watched_unwatched(movie_list)
        elif choice == 4:
            find_movie(movie_list)
        elif choice == 5:
            remove_movie(movie_list)
        elif choice == 6:
            print('Exiting')
            break
        else:
            print('Invalid input')

main()