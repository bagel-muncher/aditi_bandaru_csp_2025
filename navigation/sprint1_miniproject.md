---
layout: page
title: Movies Blog
description: Blog about movies
permalink: /sprint1_miniproject/
---
<style>
    body {
        background-color: black;
    }

p {
    color: white;
}

    .movie_menu {
        background-color: black;
        display: flex;
        align-items: center;
    }
    
    .movie_button {
        color: white;
        background-color: #71BC78;
        border: none;
        border-radius: 5px;
        padding: 10px;
    }
    .blog_intro {
        display: flex;
        align-items: center;
    }
</style>
<html>
<body>
    <div class="movie_menu">
        <table class="movie_table">
            <tr>
                <td><img src="{{site.baseurl}}/images/sprints/sprint1_images/movie_blog1.png" height="60" title="GH Pages" alt=""></td>
                <td><a href="{{site.baseurl}}/sprint1_miniproject/index"><button class="movie_button">Home</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/classics_page/index"><button class="movie_button">Classics</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/sci_fi_page/index"><button class="movie_button">Sci-Fi</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/fantasy_page/index"><button class="movie_button">Fantasy</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/action_page/index"><button class="movie_button">Action</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/animation_page/index"><button class="movie_button">Animation</button></a></td>
            </tr>
        </table>
    </div>
    <br>
    <div class="blog_intro">
        <div>
            <p>Movies have been a huge part of my life. I grew up on Star Wars, Dreamworks, and Disney movies and they hold up even today. In this mini blog, I'm listing my top 5 favorite movies in 5 genres: Classics, Science Fiction, Fantasy, Action, and Animation.</p>
        </div>
        <img src="{{site.baseurl}}/images/sprints/sprint1_images/mainpage_image.jpg" alt="oppenheimer" height="350">
    </div>
</body>
</html>