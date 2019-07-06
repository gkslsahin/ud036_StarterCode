import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A sotry about a boy and his toys which get life",
                        "http://cdn.filmlerim.com/mi/19/1b/iVbyAOhNQVK8sihfGg5x0CWrFSJvCAufKApPAIEW.jpeg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A Marine On An Alien Planet",
                    "https://upload.wikimedia.org/wikipedia/tr/thumb/1/12/Avatar-Film-Posteri.jpg/220px-Avatar-Film-Posteri.jpg",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                            "https://images-na.ssl-images-amazon.com/images/I/81gtCOwWXdL._SY355_.jpg",
                            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is chef in Paris",
                            "http://tr.web.img4.acsta.net/c_215_290/pictures/bzp/01/46211.jpg",
                            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight In Paris", "Going back in time to meet authors",
                            "https://1.bp.blogspot.com/-ksOa4uHOjkI/W-9gBmIpeiI/AAAAAABBQQ4/MLp3_8hu9NIIjdtQz4z1AWppXwr4__gNgCLcBGAs/s400/Midnight_in_Paris-2011-Woody_Allen-movie-1.jpg",
                            "https://www.youtube.com/watch?v=FAfR8omt-CY") 


dark_knight_rises = media.Movie("Dark Knight Rises","The struggle of Batman and the Joker",
                                "https://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                                "https://www.youtube.com/watch?v=g8evyE9TuYk")

movie_list = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, dark_knight_rises]


#print(media.Movie.VALID_RATINGS)
#print(media.Movie.__doc__)

fresh_tomatoes.open_movies_page(movie_list)