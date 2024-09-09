---
layout: page
title: Science Fiction
description: no need to explain
permalink: /sprints/sprint1/sci_fi_page/
---
<style>
    body {
        background-color: #ebfcfc/*#ebfaf4*/;
    }

    .scifi_title {
        font-size: 22px;
        color: #6ad0d4;
        font-weight: 20px;
    }
    .movie_menu {
        background-color: #ebfcfc;
        display: flex;
        align-items: center;
    }
    
    .movie_button {
        color: white;
        background-color: #6ad0d4;
        border: none;
        border-radius: 5px;
        padding: 10px;
    }
    .movie_box {
        border-style: solid;
        border-width: 3px;
        border-radius: 5px;
        border-color: #6ad0d4;
        padding: 10px;
        display: flex;
        gap: 20px;
        align-items: center;
    }
</style>
<html>
<body>
<!-- Template
    <div class="movie_box">
        <div>
            <h3></h3>
            <p></p>
                <ul>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                    <li></li>
                </ul>
        </div>
    </div>
    -->
    <div class="movie_menu">
            <table>
                <tr>
                    <td><img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_blog.png" height="60" title="GH Pages" alt=""></td>
                    <td><a href="/aditi_bandaru_csp_2025/sprint1_miniproject/index"><button class="movie_button">Home</button></a></td>
                    <td><a href="/aditi_bandaru_csp_2025/sprints/sprint1/classics_page/index"><button class="movie_button">Classics</button></a></td>
                    <td><a href="/aditi_bandaru_csp_2025/sprints/sprint1/sci_fi_page/index"><button class="movie_button">Sci-Fi</button></a></td>
                    <td><a href="/aditi_bandaru_csp_2025/sprints/sprint1/fantasy_page/index"><button class="movie_button">Fantasy</button></a></td>
                    <td><a href="/aditi_bandaru_csp_2025/sprints/sprint1/action_page/index"><button class="movie_button">Action</button></a></td>
                    <td><a href="/aditi_bandaru_csp_2025/sprints/sprint1/animation_page/index"><button class="movie_button">Animation</button></a></td>
                </tr>
            </table>
    </div>
    <br>
    <div class="movie_box">
        <div>
            <p class="scifi_title">Star Wars: The Empire Strikes Back</p>
            <p>(The best Star Wars movie ever) Luke Skywalker, Han Solo, Princess Leia and Chewbacca face attack by the Imperial forces and its AT-AT walkers on the ice planet Hoth. While Han and Leia escape in the Millennium Falcon, Luke travels to Dagobah in search of Yoda. Only with the Jedi master's help will Luke survive when the dark side of the Force beckons him into the ultimate duel with Darth Vader.</p>
                <ul>
                    <li>Director: Irvin Kershner (Story by George Lucas)</li>
                    <li>Cast: Mark Hamill (Luke Skywalker), Harrison Ford (Han Solo), Carrie Fisher, (Princess Leia), Billy Dee Williams (Lando Calrissian), Peter Mayhew (Chewbacca), Frank Oz (Yoda), Anthony Daniels (C-3PO), Kenny Baker (R2-D2)</li>
                    <li>Rotten Tomatoes Rating: 95%</li>
                    <li>Release Date: May 21, 1980</li>
                    <li>Music Composer: John Williams</li>
                </ul>
        </div>
        <img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_posters/empire_strikes_back.jpg" alt="empire strikes back poster" height="300">
    </div>
    <br>
    <div class="movie_box">
        <div >
            <p class="scifi_title">The Martian</p>
            <p>The Martian - When astronauts blast off from the planet Mars, they leave behind Mark Watney, presumed dead after a fierce storm. With only a meager amount of supplies, the stranded visitor must utilize his wits and spirit to find a way to survive on the hostile planet. Meanwhile, back on Earth, members of NASA and a team of international scientists work tirelessly to bring him home, while his crew mates hatch their own plan for a daring rescue mission.</p>
                <ul>
                    <li>Director: Ridley Scott (Story by Andy Weir)</li>
                    <li>Cast: Matt Damon, Jessica Chastain, Kristen Wiig</li>
                    <li>Rotten Tomatoes Rating: 91%</li>
                    <li>Release Date: October 2, 2015</li>
                    <li>Music Composer: Harry Gregson-Williams</li>
                </ul>
        </div>
        <img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_posters/the_martian.jpg" alt="the martian poster" height="300">
    </div>
    <br>
    <div class="movie_box">
        <div>
            <p class="scifi_title">Interstellar</p>
            <p>In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand, a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole. But first, Brand must send former NASA pilot Cooper and a team of researchers through the wormhole and across the galaxy to find out which of three planets could be mankind's new home.</p>
                <ul>
                    <li>Director: Christopher Nolan</li>
                    <li>Cast: Matthew McConaughey, Anne Hathaway, Jessica Chastain, Matt Damon, Michael Caine</li>
                    <li>Rotten Tomatoes Rating: 73%</li>
                    <li>Release Date: October 26, 2014</li>
                    <li>Music Composer: Hans Zimmer</li>
                </ul>
        </div>
        <img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_posters/interstellar.jpg" alt="interstellar poster" height="300">
    </div>
    <br>
    <div class="movie_box">
        <div>
            <p class="scifi_title">Dune: Part One</p>
            <p>Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, must travel to a dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of a precious resource in existence, only those who can conquer their own fear will survive.</p>
                <ul>
                    <li>Director: Denis Villeneuve (Story by Frank Herbert)</li>
                    <li>Cast: Timothée Chalamet, Zendaya, Rebecca Ferguson, Oscar Isaac, Jason Momoa, Stellan Skarsgård, Javier Bardem, Josh Brolin, Dave Bautista</li>
                    <li>Rotten Tomatoes Rating: 83%</li>
                    <li>Release Date: October 22, 2021</li>
                    <li>Music Composer: Hans Zimmer</li>
                </ul>
        </div>
        <img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_posters/dune.webp" alt="dune poster" height="300">
    </div>
    <br>
    <div class="movie_box">
        <div>
            <p class="scifi_title">Inception</p>
            <p>Dom Cobb is a thief with the rare ability to enter people's dreams and steal their secrets from their subconscious. His skill has made him a hot commodity in the world of corporate espionage but has also cost him everything he loves. Cobb gets a chance at redemption when he is offered a seemingly impossible task: Plant an idea in someone's mind. If he succeeds, it will be the perfect crime, but a dangerous enemy anticipates Cobb's every move.</p>
                <ul>
                    <li>Director: Christopher Nolan</li>
                    <li>Cast: Leonardo DiCaprio, Joseph Gordon-Levitt, Elliot Page, Tom Hardy, Ken Watanabe, Dileep Rao, Cillian Murphy, Marion Cotillard</li>
                    <li>Rotten Tomatoes Rating: 87%</li>
                    <li>Release Date: July 13, 2010</li>
                    <li>Music Composer: Hans Zimmer</li>
                </ul>
        </div>
        <img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_posters/inception.jpg" alt="inception poster" height="300">
    </div>
</body>
</html>