---
layout: page
title: Cookie Clicker
description: cookies
permalink: /sprints/sprint1/javascripts_playground/cookie_clicker/
---
<style>

.game-container {
    text-align: center;
}

#cookie-container {
    margin: 20px;
}

#cookie {
    width: 200px;
    cursor: pointer;
    transition: transform 0.1s ease;
}

#cookie:active {
    transform: scale(0.9);
}

</style>

<html>
<body>
    <div>
        <table>
            <tr>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/homepage/index"><img src="{{site.baseurl}}/images/sprints/sprint1_images/javascript_logo.jpg" height="60" title="GH Pages" alt="javascript_logo"></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/cookie_clicker/index"><button class="movie_button">Cookie Clicker</button></a></td>
            </tr>
        </table>
    </div>
    <br>
    <div class="game_container">
        <div id="cookie-container">
            <img id="cookie" src="{{site.baseurl}}/images/sprints/sprint1_images/cookie.png" alt="Cookie">
        </div>
        <h2>Cookies: <span id="score">0</span></h2>
    </div>
    <audio id="click-sound" src="{{site.baseurl}}/sounds/sprint1/cookie_sound.mp3" preload="auto"></audio>
    <script>
        let score = 0;
        const cookie = document.getElementById('cookie');
        const scoreDisplay = document.getElementById('score');
        const clickSound = document.getElementById('click-sound');
        cookie.addEventListener('click', () => {
        score++;
        scoreDisplay.textContent = score;
        // Play sound on click
        clickSound.currentTime = 0;
        clickSound.play();
        });     
    </script>
</body>
</html>
