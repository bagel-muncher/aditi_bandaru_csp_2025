---
toc: False 
layout: tailwindPost
infoGraph: tools_infograph
questions: tools_questions
title: Tools and Equipment
description: Tech has reshaped our lives, from the internet to the smartphone in your pocket, or the advent of AI. This course is opening new technology possibilities by equipping you with the developer tools that are the keys to boundless technology possibilities.
courses: {'csse': {'week': 1}, 'csp': {'week': 1}, 'csa': {'week': 1}}
type: ccc
categories: [DevOps]
permalink: /tools/
sticky_rank: 1
---

<!-- Infographic - this depends on page.infoGraph frontmatter being set -->
{%- include tailwind/infograph.html -%}
<div>
  {% assign data = site.data[page.infoGraph] %}
  <div class="container">
    <!-- Header Section -->
    <div class="p-6 rounded-lg shadow-md">
      <h1 class="text-5xl mb-4">{{ data.Title }}</h1>
      <p class="text-lg mb-4">{{ data.Description }}</p>
    </div>
