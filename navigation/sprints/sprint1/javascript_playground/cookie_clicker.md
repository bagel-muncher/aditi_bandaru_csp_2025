---
layout: page
title: Cookie Clicker
description: cookies
permalink: /sprints/sprint1/javascripts_playground/cookie_clicker/
---
<style>
.game_button {
    color: white;
    background-color: #71BC78;
    border: none;
    border-radius: 5px;
    padding: 10px;
}
.game_container {
    background-color: #1d8096;
    padding: 20px;
    margin: 0;
}

p {
    color: white;
    font-size: 30px;
}

#cookie_container {
    margin: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

#cookie {
    width: 200px;
    cursor: pointer;
    transition: transform 0.1s ease;
}

#cookie:active {
    transform: scale(0.9);
}

#reset {
    color: white;
    background-color: #4b91a1;
    margin-top: 20px;
    border: none;
    border-radius: 5px;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

</style>

<html>
<body>
    <div>
        <table>
            <tr>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/homepage/index"><img src="{{site.baseurl}}/images/sprints/sprint1_images/javascript_logo.jpg" height="60" title="GH Pages" alt="javascript_logo"></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/cookie_clicker/index"><button
                class="game_button">Cookie Clicker</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/calculator/index"><button class="game_button">Calculator</button></a></td>
            </tr>
        </table>
    </div>
    <br>
    <div class="game_container">
        <div id="cookie_container">
            <img id="cookie" src="{{site.baseurl}}/images/sprints/sprint1_images/cookie.png" alt="Cookie">
            <p>Cookies: <span id="score">0</span></p>
        </div>
        <br>
        <button id="reset">Reset Score</button>
    </div>
    <audio id="click-sound" src="{{site.baseurl}}/sounds/sprint1/cookie_sound.mp3" preload="auto"></audio>
    <script>
        let score = 0;
        const cookie = document.getElementById('cookie');
        const scoreDisplay = document.getElementById('score');
        const clickSound = document.getElementById('click-sound');
        const resetButton = document.getElementById('reset');
        cookie.addEventListener('click', () => {
        score++;
        scoreDisplay.textContent = score;
        // Play sound on click
        clickSound.currentTime = 0;
        clickSound.play();
        });
        resetButton.addEventListener('click', () => {
            score = 0;
            scoreDisplay.textContent = score;    
        }); 
    </script>
</body>
</html>
