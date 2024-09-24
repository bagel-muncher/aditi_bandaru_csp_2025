---
layout: page
title: Calculator
description: Not the God given one Lanzi-Sheaman wants 😔
permalink: /sprints/sprint1/javascripts_playground/calculator/
---
<style>
    /*Fix game buttons problems*/
    .game_button {
        color: white;
        background-color: #71BC78;
        border: none;
        border-radius: 5px;
        padding: 10px;
    }
    .calc_container {
        background-color: black;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        font-family: Arial, sans-serif;
    }
    .calculator {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }

    input#display {
        width: 100%;
        height: 60px;
        font-size: 2em;
        text-align: right;
        margin-bottom: 10px;
        border: none;
        background-color: #f4f4f4;
        padding: 10px;
        border-radius: 5px;
    }

    .buttons {
        display: grid;
        grid-template-columns: repeat(4, 80px);
        grid-gap: 10px;
    }

    .n {
        width: 80px;
        height: 80px;
        font-size: 1.5em;
        border: none;
        background-color: #e0e0e0;
        border-radius: 10px;
        transition: background-color 0.2s;
    }
    .n:hover {
        background-color: #b1b9bf;
    }

    button:active {
        background-color: #ccc;
    }
    
    .history {
    display: none;
    background-color: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    width: 320px;
    text-align: center;
    }

    ul {
    list-style-type: none;
    padding: 0;
    font-size: 1.2em;
    }
</style>

<html>
<body>
    <div>
        <table>
            <tr>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/homepage/index"><img src="{{site.baseurl}}/images/sprints/sprint1_images/javascript_logo.jpg" height="60" title="GH Pages" alt="javascript_logo"></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/cookie_clicker/index"><button class="game_button">Cookie Clicker</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/calculator/index"><button class="game_button">Calculator</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/tic_tac_toe/index"><button class="game_button">Tic Tac Toe</button></a></td>
                <td><a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/api_music/index"><button class="game_button">API</button></a></td>
            </tr>
        </table>
    </div>
    <br>
    <!--calculator html-->
    <div class="calc_container">
    <div class="calculator">
        <input type="text" id="display" disabled>
        <div class="buttons">
            <button class="n" onclick="clearDisplay()">A/C</button>
            <button class="n" onclick="squareRoot()">√</button>
            <button class="n" onclick="square()">x²</button>
            <button class="n" onclick="insertOperator('/')">÷</button>
            <button class="n" onclick="insertNumber(7)">7</button>
            <button class="n" onclick="insertNumber(8)">8</button>
            <button class="n" onclick="insertNumber(9)">9</button>
            <button class="n" onclick="insertOperator('*')">×</button>
            <button class="n" onclick="insertNumber(4)">4</button>
            <button class="n" onclick="insertNumber(5)">5</button>
            <button class="n" onclick="insertNumber(6)">6</button>
            <button class="n" onclick="insertOperator('-')">−</button>
            <button class="n" onclick="insertNumber(1)">1</button>
            <button class="n" onclick="insertNumber(2)">2</button>
            <button class="n" onclick="insertNumber(3)">3</button>
            <button class="n" onclick="insertOperator('+')">+</button>
            <button class="n" onclick="insertNumber(0)">0</button>
            <button class="n" onclick="insertOperator('.')">.</button>
            <button class="n" onclick="calculate()">=</button>
            <button class="n" onclick="showHistory()">🕑</button>
        </div>
    </div>
        <div class="history" id="historyDisplay">
            <h3>History</h3>
            <ul id="historyList"></ul>
        </div>
    </div>
<script>
    // Insert a number or operator into the display
    function insertNumber(number) {
        document.getElementById('display').value += number;
    }
    // Insert an operator into the display
    function insertOperator(operator) {
        document.getElementById('display').value += operator;
    }
    // Clear the display
    function clearDisplay() {
        document.getElementById('display').value = '';
    }
    // Calculate the expression in the display
    function calculate() {
        let expression = document.getElementById('display').value;
        if (expression) {
            try {
                //let result = eval(expression);
                //document.getElementById('display').value = result;
                document.getElementById('display').value = eval(expression);
                //
                //Store the calculation in the history
                //addToHistory(expression + ' = ' + result);
            } catch (e) {
                document.getElementById('display').value = 'Error';
            }
        }
    }
    // Calculate square root
    function squareRoot() {
        let number = document.getElementById('display').value;
        if (number) {
            //let result = Math.sqrt(number);
            //document.getElementById('display').value = result;
            document.getElementById('display').value = Math.sqrt(number);
            // Store in history
            //addToHistory('√' + number + ' = ' + result);
        }
    }
    // Calculate square of a number
    function square() {
        let number = document.getElementById('display').value;
        if (number) {
            document.getElementById('display').value = Math.pow(number, 2);
            //let result = Math.pow(number, 2);
            //document.getElementById('display').value = result;
            // Store in history
            //addToHistory(number + '² = ' + result);
        }
    }
    // Add the equation to history and maintain only 5 entries
    function addToHistory(entry) {
        if (history.length === 5) {
            history.shift(); // Remove the oldest entry if there are 5
        }
        history.push(entry);
        updateHistoryDisplay();
    }
    // Update the history display
    function updateHistoryDisplay() {
        let historyList = document.getElementById('historyList');
        historyList.innerHTML = '';
        for (let i = 0; i < history.length; i++) {
            let listItem = document.createElement('li');
            listItem.textContent = history[i];
            historyList.appendChild(listItem);
        }
    }
    // Show or hide the history display
    function showHistory() {
        let historyDiv = document.getElementById('historyDisplay');
        if (historyDiv.style.display === 'none' || historyDiv.style.display === '') {
        historyDiv.style.display = 'block';
        } else {
            historyDiv.style.display = 'none';
        }
    }
</script>
</body>
</html>