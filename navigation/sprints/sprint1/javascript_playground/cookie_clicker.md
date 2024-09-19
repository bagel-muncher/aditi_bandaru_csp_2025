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
    width: 300px;
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
/* Shop styling */
#shop {
    margin-top: 30px;
    padding: 20px;
    background-color: #fffacd;
    border-radius: 10px;
    box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
}

.upgrade {
    margin-bottom: 20px;
}

.upgrade button {
    padding: 10px;
    background-color: #32cd32;
    border: none;
    border-radius: 5px;
    color: white;
    font-size: 1em;
    cursor: pointer;
}

.upgrade button:disabled {
    background-color: #90ee90;
}

.upgrade p {
    font-size: 1.2em;
    margin-top: 10px;
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
        <br>
        </div>
        <!--shop-->
        <div id="shop_container">
            <p>Shop</p>
            <div class="upgrade">
                <button id="buy-cursor">Buy Cursor (Cost: 10 Cookies)</button>
                <p>Cursors: <span id="cursor-count">0</span></p>
            </div>
            <div class="upgrade">
                <button id="buy-grandma">Buy Grandma (Cost: 50 Cookies)</button>
                <p>Grandmas: <span id="grandma-count">0</span></p>
            </div>
        </div>
        <br>
        <button id="reset">Reset Score</button>
    </div>
    <audio id="click-sound" src="{{site.baseurl}}/sounds/sprint1/cookie_sound.mp3" preload="auto"></audio>
    <!--break between HTML and Javascript-->
    <script>
        let score = 0;
        let cursors = 0;
        let grandmas = 0;
        let cursorCost = 10;
        let grandmaCost = 50;
        //const
        const cookie = document.getElementById('cookie');
        const scoreDisplay = document.getElementById('score');
        const clickSound = document.getElementById('click-sound');
        const resetButton = document.getElementById('reset');
        //
        const buyCursorButton = document.getElementById('buy-cursor');
        const buyGrandmaButton = document.getElementById('buy-grandma');
        const cursorCountDisplay = document.getElementById('cursor-count');
        const grandmaCountDisplay = document.getElementById('grandma-count');
        //
        cookie.addEventListener('click', () => {
        score++;
        updateScore();
        // Play sound on click
        clickSound.currentTime = 0;
        playClickSound();
        });
        resetButton.addEventListener('click', () => {
            score = 0;
            cursors = 0;
            grandmas = 0;
            cursorCost = 10;
            grandmaCost = 50;
            updateScore();
            updateUpgrades();    
        }); 
        // Buy cursor (1 point per second)
        buyCursorButton.addEventListener('click', () => {
            if (score >= cursorCost) {
                score -= cursorCost;
                cursors++;
                cursorCost = Math.floor(cursorCost * 1.2); // Increase cost by 20%
                updateScore();
                updateUpgrades();
            }
        });
        // Buy grandma (5 points per second)
        buyGrandmaButton.addEventListener('click', () => {
            if (score >= grandmaCost) {
                score -= grandmaCost;
                grandmas++;
                grandmaCost = Math.floor(grandmaCost * 1.3); // Increase cost by 30%
                updateScore();
                updateUpgrades();
            }
        });
        // Update score display
        function updateScore() {
        scoreDisplay.textContent = score;
        }
        // Update upgrade counts and costs
        function updateUpgrades() {
            cursorCountDisplay.textContent = cursors;
            grandmaCountDisplay.textContent = grandmas;
            buyCursorButton.textContent = `Buy Cursor (Cost: ${cursorCost} Cookies)`;
            buyGrandmaButton.textContent = `Buy Grandma (Cost: ${grandmaCost} Cookies)`;
        // Disable buttons if score is insufficient
            buyCursorButton.disabled = score < cursorCost;
            buyGrandmaButton.disabled = score < grandmaCost;
        }
        // Passive income (Cursors: 1 cookie per second, Grandmas: 5 cookies per second)
        setInterval(() => {
            score += cursors + grandmas * 5;
            updateScore();
            updateUpgrades();
        }, 1000);
        // Play click sound
        function playClickSound() {
            clickSound.currentTime = 0;
            clickSound.play();
        }
    </script>
</body>
</html>
