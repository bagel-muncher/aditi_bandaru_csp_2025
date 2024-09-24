---
layout: page
title: Tic Tac Toe
description: XoX
permalink: /sprints/sprint1/javascripts_playground/tic_tac_toe/
---
<style>
    body {  
        font-family: 'Poppins', sans-serif;
        color: #000000;
    }
    .container {
        background-color: #d1fbff;
        padding: 20px;
    }
    .game_button {
        color: white;
        background-color: #71BC78;
        border: none;
        border-radius: 5px;
        padding: 10px;
    }
    #board {
        margin-left: auto;
        margin-right: auto;
        width: 375px;
        height: 375px;
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        grid-gap: 5px;
    }
    .square {
        width: 120px;
        height: 120px;
        border: 1px solid #D3D3D3;
        background-color: #F5F5F5;
        ont-size: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .square:hover {
        background-color: #FFFFE0;
    }
    #restartButton {
        display: block;
        margin-left: auto;
        margin-right: auto;
        height: 40px;
        width: 150px;
        background-color: #FFFFFF;
        border: 1px solid #000000;
        border-radius: 40px;
        font-size: 18px;
    }
    #restartButton:hover {
        background-color: #000000;
        color: #FFFFFF;
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
                <!--<td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/snake/index"><button class="game_button">Snake</button></a></td>-->
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/tic_tac_toe/index"><button class="game_button">Tic Tac Toe</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/api_music/index"><button class="game_button">API</button></a></td>
            </tr>
        </table>
    </div>
    <br>
    <div class="container">
    <div id="board">
        <div class="square" id="square0"></div>
        <div class="square" id="square1"></div>
        <div class="square" id="square2"></div>
        <div class="square" id="square3"></div>
        <div class="square" id="square4"></div>
        <div class="square" id="square5"></div>
        <div class="square" id="square6"></div>
        <div class="square" id="square7"></div>
        <div class="square" id="square8"></div>
    </div>
    <div id="endGame">
        <input type="button" value="Restart" id="restartButton" onclick="restartButton()"/>
    </div>
    </div>
<!--javascript-->
<script>
    const board = document.getElementById('board')
    const squares = document.getElementsByClassName('square')
    const players = ['X', 'O']
    let currentPlayer = players[0]
    //
    const endMessage = document.createElement('h2')
    endMessage.textContent = `X's turn!`
    endMessage.style.marginTop = '30px'
    endMessage.style.textAlign='center'
    board.after(endMessage)
    //
    const winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for(let i = 0; i < squares.length; i++){
        squares[i].addEventListener('click', () => {
            if(squares[i].textContent !== ''){
                return
            }
            squares[i].textContent = currentPlayer
            if(checkWin(currentPlayer)) {
                endMessage.textContent=`Game over! ${currentPlayer} wins!`
                return
            }
            if(checkTie()) {
                endMessage.textContent= `Game is tied!`
                return
            }
            currentPlayer = (currentPlayer === players[0]) ? players[1] : players[0] 
            if(currentPlayer == players[0]) {
            endMessage.textContent= `X's turn!`
            } else {
                endMessage.textContent= `O's turn!`
            }     
        })   
    }
    //
    function checkWin(currentPlayer) {
        for(let i = 0; i < winning_combinations.length; i++){
            const [a, b, c] = winning_combinations[i]
            if(squares[a].textContent === currentPlayer && squares[b].textContent === currentPlayer && squares[c].textContent === currentPlayer){
                return true
            }
        }
        return false
    }
    function checkTie(){
        for(let i = 0; i < squares.length; i++) {
            if(squares[i].textContent === '') {
                return false;
            }
        }
        return true
    }
    function restartButton() {
        for(let i = 0; i < squares.length; i++) {
            squares[i].textContent = ""
        }
        endMessage.textContent=`X's turn!`
        currentPlayer = players[0]
    }
</script>  
</body>
</html>