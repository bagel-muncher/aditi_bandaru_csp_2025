---
layout: page
title: Snake Game
description: hit the wall
permalink: /sprints/sprint1/javascripts_playground/snake/
---
<style>
    #game-board {
        position: relative;
        width: 400px;
        height: 400px;
        background-color: #333;
        border: 1px solid #000;
    }

    #score {
        margin: 20px;
        font-size: 24px;
    }

    #new-game {
        padding: 10px 20px;
        font-size: 16px;
        cursor: pointer;
    }
</style>
<!--html-->
<html>
    <body>
        <div id="game-board"></div>
        <div id="score">Score: 0</div>
        <button id="new-game">Start New Game</button>
    </body>
<!--javascript-->
<script>
    const boardSize = 20; // 20x20 grid
    const tileSize = 20; // Each tile is 20px by 20px
    let snake = [{ x: 10, y: 10 }];
    let direction = { x: 0, y: 0 };
    let food = { x: 5, y: 5 };
    let score = 0;
    let immunity = false;
    let immunityTimer;
    let gameInterval;
    //constants
    const board = document.getElementById('game-board');
    const scoreElement = document.getElementById('score');
    const newGameButton = document.getElementById('new-game');
    // Create the game grid
    for (let i = 0; i < boardSize * boardSize; i++) {
        const div = document.createElement('div');
        div.style.width = `${tileSize}px`;
        div.style.height = `${tileSize}px`;
        div.style.float = 'left';
        div.style.boxSizing = 'border-box';
        board.appendChild(div);
    }
    const tiles = board.children;
    //
    function updateBoard() {
    // Clear the board
    for (let i = 0; i < tiles.length; i++) {
        tiles[i].style.backgroundColor = '#333';
    }
    // Render the snake
    snake.forEach(segment => {
        const index = segment.y * boardSize + segment.x;
        tiles[index].style.backgroundColor = '#0f0';
    });
    // Render the food
    const foodIndex = food.y * boardSize + food.x;
    tiles[foodIndex].style.backgroundColor = '#f00';
    scoreElement.textContent = `Score: ${score}`;
    }
    function moveSnake() {
        const head = { ...snake[0] };
        head.x += direction.x;
        head.y += direction.y;
        // Check for wall collision
        if (head.x < 0 || head.x >= boardSize || head.y < 0 || head.y >= boardSize) {
            if (!immunity) {
                endGame();
                return;
            }
        }
        // Wrap around if immunity is active
        if (immunity) {
            head.x = (head.x + boardSize) % boardSize;
            head.y = (head.y + boardSize) % boardSize;
        }
        // Check for food
        if (head.x === food.x && head.y === food.y) {
            score++;
            snake.push({ ...snake[snake.length - 1] });
            spawnFood();
            maybeSpawnImmunity();
        } else {
            snake.pop();
        }
        // Move the snake forward
        snake.unshift(head);
        updateBoard();
    }
    function spawnFood() {
        food.x = Math.floor(Math.random() * boardSize);
        food.y = Math.floor(Math.random() * boardSize);
    }
    function maybeSpawnImmunity() {
        if (Math.random() < 0.1) { // 10% chance to spawn immunity
            startImmunity();
        }
    }
    function startImmunity() {
        immunity = true;
        clearTimeout(immunityTimer);
        immunityTimer = setTimeout(() => {
            immunity = false;
        }, 20000); // 20 seconds immunity
    }
    function endGame() {
        clearInterval(gameInterval);
        alert('Game Over! Your score was: ' + score);
    }
    function resetGame() {
        snake = [{ x: 10, y: 10 }];
        direction = { x: 0, y: 0 };
        score = 0;
        immunity = false;
        updateBoard();
        spawnFood();
        gameInterval = setInterval(moveSnake, 100);
    }
    window.addEventListener('keydown', (e) => {
        switch (e.key) {
            case 'ArrowUp':
                if (direction.y === 0) direction = { x: 0, y: -1 };
                break;
            case 'ArrowDown':
                if (direction.y === 0) direction = { x: 0, y: 1 };
                break;
            case 'ArrowLeft':
                if (direction.x === 0) direction = { x: -1, y: 0 };
                break;
            case 'ArrowRight':
                if (direction.x === 0) direction = { x: 1, y: 0 };
                break;
        }
    });
    newGameButton.addEventListener('click', resetGame);
    resetGame(); 
    // Start the game initially
</script>
</html>