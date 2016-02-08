import fresh_tomatoes
import media

# TVShow Listing
got = media.TVShow("Game of Thrones",
                   "While a civil war brews between several noble families in Westeros, the children of the former rulers of the land attempt to rise up to power. Meanwhile a forgotten race, bent on destruction, return after thousands of years in the North.",
                   "http://ia.media-imdb.com/images/M/MV5BMTYwOTEzMDMzMl5BMl5BanBnXkFtZTgwNzExODIzNzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                   "https://www.youtube.com/watch?v=BpJYNVhGf1s",
                   "6",
                   "60")

friends = media.TVShow("Friends",
                       "Follows the lives of six 20-something friends living in Manhattan.",
                       "http://ia.media-imdb.com/images/M/MV5BMTg4NzEyNzQ5OF5BMl5BanBnXkFtZTYwNTY3NDg4._V1._CR24,0,293,443_UX182_CR0,0,182,268_AL_.jpg",
                       "https://www.youtube.com/watch?v=E9SFstXn7YU",
                       "10",
                       "236")

big_bang_theory = media.TVShow("The Big Bang Theory",
                               "A woman who moves into an apartment across the hall from two brilliant but socially awkward physicists shows them how little they know about life outside of the laboratory.",
                               "http://ia.media-imdb.com/images/M/MV5BMjI1Mzc4MDUwNl5BMl5BanBnXkFtZTgwMDAzOTIxMjE@._V1_UY268_CR16,0,182,268_AL_.jpg",
                               "https://www.youtube.com/watch?v=5NbsjMFI8Cc",
                               "9",
                               "202")

# Movie Listing
interstellar = media.Movie("Interstellar",
                           "A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
                           "http://ia.media-imdb.com/images/M/MV5BMjIxNTU4MzY4MF5BMl5BanBnXkFtZTgwMzM4ODI3MjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=3WzHXI5HizQ",
                           "2h 49min")

star_wars = media.Movie("Star Wars: Episode VII - The Force Awakens",
                        "Three decades after the defeat of the Galactic Empire, a new threat arises. The First Order attempts to rule the galaxy and only a ragtag group of heroes can stop them, along with the help of the Resistance.",
                        "http://ia.media-imdb.com/images/M/MV5BOTAzODEzNDAzMl5BMl5BanBnXkFtZTgwMDU1MTgzNzE@._V1_SY317_CR0,0,214,317_AL_.jpg",
                        "https://www.youtube.com/watch?v=sGbxmsDFVnE",
                        "135 min")

gravity = media.Movie("Gravity",
                      "A medical engineer and an astronaut work together to survive after an accident leaves them adrift in space.",
                      "http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_UX182_CR0,0,182,268_AL_.jpg",
                      "https://www.youtube.com/watch?v=OiTiKOy59o4",
                      "1h 31min")

the_martian = media.Movie("The Martian",
                          "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive.",
                          "http://ia.media-imdb.com/images/M/MV5BMTc2MTQ3MDA1Nl5BMl5BanBnXkFtZTgwODA3OTI4NjE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8",
                          "2h 24min")

lord_of_the_rings = media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                                "A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.",
                                "http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_UY268_CR0,0,182,268_AL_.jpg",
                                "https://www.youtube.com/watch?v=V75dMMIW2B4",
                                "2h 58min")

ind_day_res = media.Movie("Independence Day: Resurgence",
                          "Two decades after the first Independence Day invasion, Earth is faced with a new extra-Solar threat. But will mankind's new space defenses be enough?",
                          "http://ia.media-imdb.com/images/M/MV5BMTc4NTA2NDIzMF5BMl5BanBnXkFtZTgwMTYxNjc0NzE@._V1_UX182_CR0,0,182,268_AL_.jpg",
                          "https://www.youtube.com/watch?v=LbduDRH2m2M",
                          "NOT_YET_KNOWN")

movies = [got, friends, big_bang_theory, interstellar, gravity, the_martian, lord_of_the_rings, ind_day_res, star_wars]

fresh_tomatoes.open_movies_page(movies)
