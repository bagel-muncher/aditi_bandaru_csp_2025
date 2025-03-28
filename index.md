---
layout: base
title: Student Home 
description: Home Page
image: /images/mario_animation.png
hide: true
---

<strong class="journey">My journey starts here.</strong>

<style>
  .journey {
    color: #008080;
  }
</style>


<!-- Liquid:  statements -->

<!--- Concatenation of site URL to frontmatter image  --->
{% assign sprite_file = site.baseurl | append: page.image %}
<!--- Has is a list variable containing mario metadata for sprite --->
{% assign hash = site.data.mario_metadata %}  
<!--- Size width/height of Sprit images --->
{% assign pixels = 256 %}

<!--- HTML for page contains <p> tag named "Mario" and class properties for a "sprite"  -->

<p id="mario" class="sprite"></p>
  
<!--- Embedded Cascading Style Sheet (CSS) rules, 
        define how HTML elements look 
--->
<style>

  /*CSS style rules for the id and class of the sprite...
  */
  .sprite {
    height: {{pixels}}px;
    width: {{pixels}}px;
    background-image: url('{{sprite_file}}');
    background-repeat: no-repeat;
  }

  /*background position of sprite element
  */
   #mario {
    background-position: calc({{animations[0].col}} * {{pixels}} * -1px) calc({{animations[0].row}} * {{pixels}}* -1px);
  }
</style>

<!--- Embedded executable code--->
<script>
  ////////// convert YML hash to javascript key:value objects /////////

  var mario_metadata = {}; //key, value object
  {% for key in hash %}  
  
  var key = "{{key | first}}"  //key
  var values = {} //values object
  values["row"] = {{key.row}}
  values["col"] = {{key.col}}
  values["frames"] = {{key.frames}}
  mario_metadata[key] = values; //key with values added

  {% endfor %}

  ////////// game object for player /////////

  class Mario {
    constructor(meta_data) {
      this.tID = null;  //capture setInterval() task ID
      this.positionX = 0;  // current position of sprite in X direction
      this.currentSpeed = 0;
      this.marioElement = document.getElementById("mario"); //HTML element of sprite
      this.pixels = {{pixels}}; //pixel offset of images in the sprite, set by liquid constant
      this.interval = 100; //animation time interval
      this.obj = meta_data;
      this.marioElement.style.position = "absolute";
    }

    animate(obj, speed) {
      let frame = 0;
      const row = obj.row * this.pixels;
      this.currentSpeed = speed;

      this.tID = setInterval(() => {
        const col = (frame + obj.col) * this.pixels;
        this.marioElement.style.backgroundPosition = `-${col}px -${row}px`;
        this.marioElement.style.left = `${this.positionX}px`;

        this.positionX += speed;
        frame = (frame + 1) % obj.frames;

        const viewportWidth = window.innerWidth;
        if (this.positionX > viewportWidth - this.pixels) {
          document.documentElement.scrollLeft = this.positionX - viewportWidth + this.pixels;
        }
      }, this.interval);
    }

    startWalking() {
      this.stopAnimate();
      this.animate(this.obj["Walk"], 3);
    }

    startRunning() {
      this.stopAnimate();
      this.animate(this.obj["Run1"], 6);
    }

    startPuffing() {
      this.stopAnimate();
      this.animate(this.obj["Puff"], 0);
    }

    startCheering() {
      this.stopAnimate();
      this.animate(this.obj["Cheer"], 0);
    }

    startFlipping() {
      this.stopAnimate();
      this.animate(this.obj["Flip"], 0);
    }

    startResting() {
      this.stopAnimate();
      this.animate(this.obj["Rest"], 0);
    }

    stopAnimate() {
      clearInterval(this.tID);
    }
  }

  const mario = new Mario(mario_metadata);

  ////////// event control /////////

  window.addEventListener("keydown", (event) => {
    if (event.key === "ArrowRight") {
      event.preventDefault();
      if (event.repeat) {
        mario.startCheering();
      } else {
        if (mario.currentSpeed === 0) {
          mario.startWalking();
        } else if (mario.currentSpeed === 3) {
          mario.startRunning();
        }
      }
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      if (event.repeat) {
        mario.stopAnimate();
      } else {
        mario.startPuffing();
      }
    }
  });

  //touch events that enable animations
  window.addEventListener("touchstart", (event) => {
    event.preventDefault(); // prevent default browser action
    if (event.touches[0].clientX > window.innerWidth / 2) {
      // move right
      if (currentSpeed === 0) { // if at rest, go to walking
        mario.startWalking();
      } else if (currentSpeed === 3) { // if walking, go to running
        mario.startRunning();
      }
    } else {
      // move left
      mario.startPuffing();
    }
  });

  //stop animation on window blur
  window.addEventListener("blur", () => {
    mario.stopAnimate();
  });

  //start animation on window focus
  window.addEventListener("focus", () => {
     mario.startFlipping();
  });

  //start animation on page load or page refresh
  document.addEventListener("DOMContentLoaded", () => {
    // adjust sprite size for high pixel density devices
    const scale = window.devicePixelRatio;
    const sprite = document.querySelector(".sprite");
    sprite.style.transform = `scale(${0.2 * scale})`;
    mario.startResting();
  });

</script>

<html>
  <!--List of my school year projects and stuff-->
  <div class="pages">
    <h3 class="page_title">AP Exam Team Teaches</h3>
    <a href="{{site.baseurl}}/sprints/sprint7/team_teach_index"><button class="page_button">CW and HW for Lessons</button></a>
  </div>
  <br>
  <div class="pages">
    <h3 clss="page_title">Sprint 2: Big Ideas 3</h3>
    <a href="{{site.baseurl}}/sprints/sprint2/sprint2_homepage/index"><button class="page_button">Big Ideas 3</button></a>
  </div>
  <br>
  <div class="pages">
    <h3 class="page_title">Javascript Playground</h3>
    <a href="{{site.baseurl}}/sprints/sprint1/javascripts_playground/homepage/index"><button class="page_button">Playground</button></a>
  </div>
  <br>
  <div class="pages"> 
    <a href="https://nighthawkcoders.github.io/portfolio_2025/frontend/basics/playground" target="_blank" rel="noopener noreferrer">HTML Hacks</a>
    <a href="https://nighthawkcoders.github.io/portfolio_2025/sass_basics/intro" target="_blank" rel="noopener noreferrer">SASS Basics</a>
    <h3 class="page_title">Frontend Development</h3>
    <p>These links go to the nighthawk pages that teach the basics of HTML and SASS</p>
  </div>
  <br>
  <div class="pages">
    <h3><a href="{{site.baseurl}}/github/pages/intro">GitHub Pages Playground</a></h3>
    <p>This is a little blog about my favorite movies</p>
    <br>
    <a href="{{site.baseurl}}/sprint1_miniproject/index"><button class="page_button">Mini-Project: Blog</button></a>
  </div>
  <br>
</html>

<style>

  /**This is for Nighthawk Pages**/
.pages {
  border-style: solid;
  border-width: 3px;
  border-radius: 5px;
  padding: 15px;
  border-color:#008080;
}

.page_button {
  color: white;
  border-radius: 5px;
  border: none;
  background-color: #ace3e3;
  padding: 15px;
}
</style>
