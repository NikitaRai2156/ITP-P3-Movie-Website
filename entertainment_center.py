# -*- coding: utf-8 -*-
#use contents of media.py and fresh_tomatoes.py
import fresh_tomatoes
import media

#for Finding Nemo
finding_nemo = media.Movie("Finding Nemo",
                           "&#9733; &#9733; &#9733; &#9733;",
                           "images/findingNemo.jpg",
                           "https://www.youtube.com/watch?v=bMtzgW-FVLY")

#for Toy Story
toy_story = media.Movie("Toy Story",
                        "&#9733; &#9733; &#9733;",
                        "images/toyStory.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#for Avatar
avatar = media.Movie("Avatar",
                     "&#9733; &#9733; &#9733; &#9733;",
                     "images/avatar.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#for Harry Potter and the Sorcerer's Stone
harry_potter1 = media.Movie("Harry Potter and the Sorcerer's Stone",
                            "&#9733; &#9733; &#9733; &#9733; &#9733;",
                            "images/hp1.jpg",
                            "https://www.youtube.com/watch?v=VyHV0BRtdxo")

#for Harry Potter and the Chamber of Secrets
harry_potter2 = media.Movie("Harry Potter and the chamber of Secrets",
                            "&#9733; &#9733; &#9733; &#9733;",
                            "images/hp2.jpg",
                            "https://www.youtube.com/watch?v=1bq0qff4iF8")

#for harry Potter and the Prisoner of Azkaban
harry_potter3 = media.Movie("Harry Potter and the Prisoner of Azkaban",
                            "&#9733; &#9733; &#9733; &#9733; &#9733;",
                            "images/hp3.jpg",
                            "https://www.youtube.com/watch?v=1ZdlAg3j8nI")

#for Harry Potter and the Goblet of Fire
harry_potter4 = media.Movie("Harry Potter and the Goblet of Fire",
                            "&#9733; &#9733; &#9733; &#9733;",
                            "images/hp4.jpg",
                            "https://www.youtube.com/watch?v=3EGojp4Hh6I")

#for Harry Potter and the Order of the Phoenix
harry_potter5 = media.Movie("Harry Potter and the Order of the Phoenix",
                            "&#9733; &#9733; &#9733; &#9733;",
                            "images/hp5.jpg",
                            "https://www.youtube.com/watch?v=y6ZW7KXaXYk")

#for Harry Potter and the Half-Blood Prince
harry_potter6 = media.Movie("Harry Potter and the Half-Blood Prince",
                            "&#9733; &#9733; &#9733; &#9733; &#9733;",
                            "images/hp6.jpg",
                            "https://www.youtube.com/watch?v=sg81Lts5kYY")

#for Harry Potter and the Deathly Hallows - Part 1
harry_potter7 = media.Movie("Harry Potter and the Deathly Hallows - Part 1",
                            "&#9733; &#9733; &#9733; &#9733; &#9733;",
                            "images/hp7.jpg",
                            "https://www.youtube.com/watch?v=-L-z8VNbrcU")

#for Harry Potter and the Deathly Hallows - Part 2
harry_potter8 = media.Movie("Harry Potter and the Deathly Hallows - Part 2",
                            "&#9733; &#9733; &#9733; &#9733; &#9733;",
                            "images/hp8.jpg",
                            "https://www.youtube.com/watch?v=ll1H-9Qm1UM")

#for Fantastic Beasts and Where to Find Them
fantastic_beasts = media.Movie("Fantastic Beasts and Where to find Them",
                               "&#9733; &#9733; &#9733; &#9733;",
                               "images/fantasticBeasts.jpg",
                               "https://www.youtube.com/watch?v=Vso5o11LuGU")

#the next line creates a list of all the movies mentioned 
movies = [finding_nemo, toy_story, avatar, harry_potter1, harry_potter2, harry_potter3, harry_potter4, harry_potter5, harry_potter6, harry_potter7, harry_potter8, fantastic_beasts]

#turning this into a website using the open_movies_page function in the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
