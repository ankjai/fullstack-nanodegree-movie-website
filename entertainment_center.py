import fresh_tomatoes
import media

# interstellar
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ")

# star wars
star_wars = media.Movie("Star Wars: Episode VII - The Force Awakens",
                        "Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.",
                        "http://ia.media-imdb.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE")

# gravity
gravity = media.Movie("Gravity",
                      "A medical engineer and an astronaut work together to survive after an accident leaves them adrift in space.",
                      "http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4")

# the martian
the_martian = media.Movie("The Martian",
                          "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive.",
                          "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

# lord of the rings
lord_of_the_rings = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                "A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.",
                                "http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_UY268_CR0,0,182,268_AL_.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4")

# ind day
ind_day_res = media.Movie("Independence Day: Resurgence",
                          "Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough?",
                          "http://ia.media-imdb.com/images/M/MV5BMTc4NTA2NDIzMF5BMl5BanBnXkFtZTgwMTYxNjc0NzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=LbduDRH2m2M")

movies = [interstellar, gravity, the_martian, lord_of_the_rings, ind_day_res, star_wars]
fresh_tomatoes.open_movies_page(movies)
