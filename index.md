---
layout: landing
permalink: /index.html

title: "Making Making Machines for Makers"
excerpt: "Application required. Deadline to apply is Fri, Mar 29 at 11:59 pm."
image:
  feature: jeff-wade-736518-unsplash.jpg
  credit: Jeff Wade #name of the person or site you want to credit
  creditlink: https://unsplash.com/photos/2mzYh2Qu-ek #url to their site or licensing

---

##### Course Description:
An introductory, project-based exploration of systems and processes for making things using computer-aided design and manufacturing, and an introduction to machines and machine tools. Emphasis will be placed on building novel machines and related software for use by "makers". Course projects will encourage students to understand, build and modify/hack a sequence of machines: 
(1) an embroidery machine for custom textiles, (2) a paper cutting machine (with drag knife) for ornamental design, and (3) an XY plotter with Arduino controller. Through these projects students explore both (i) principles of operation (mechanical, stepper motors and servos, electrical control, computer software), and (ii) computer algorithms (trajectory, tool path, design). Current trends in interactive machines will be surveyed. The course will culminate in a final student-selected project.  

##### Basic Logistics
**Lectures:**   Tue, Thu 10:30 AM - 11:50 AM, Gayes 392.  
**Instructors:**   [Pat Hanrahan](https://graphics.stanford.edu/~hanrahan/), [Doug James](https://graphics.stanford.edu/~djames/)  
For more detailed course logistics and policies, see the [course info](/course_info.html) page.


##### Schedule:
<table id="schedule">
<tbody>
	<tr><td>Apr 2</td><td><a href="/lectures/intro/making.pdf"><b>Introduction to Making</b></a></td></tr>
    <tr><td>Apr 4</td><td><b><a href="/lectures/embroidery/embroidery.pdf"><b>Embroidery Machines</b></a> and <a href="/lectures/papercutting/papercutting.pdf">Paper Cutters</a></b>
    	<br><span class="assigned"><i>Assigned:</i>
    			<br><a href="/assignments/howitsmade/"> &emsp;<b>Assignment 0:</b> How Things are Made</a><b>(due Mon, Apr 8 at 12:00PM)</b>
    			<br><a href="/assignments/making/">&emsp;<b>Assignment 1:</b> Make Something!</a> <b>(due Thu, Apr 18)</b>
    	</span></td></tr>
    <tr><td>Apr 9</td><td><b>How Things are Made</b></td></tr>
    <tr><td>Apr 11</td><td><a href="/lectures/machines/machines.pdf"><b>What is a Machine?</b></a></td></tr>
    <tr><td>Apr 16 </td>
       <td><a href="/lectures/tbot/tbot1.pdf"><b>Plotter Principles of Operation 1</b></a></td>
   </tr> 
    <tr><td>Apr 18</td><td><a href="/lectures/tbot/tbot2.pdf"><b>Plotter Principles of Operation 2</b></a>
    	<br><span class="assigned"><i>Assigned:</i>
    			<br><a href="/assignments/tbot/"> &emsp;<b>Assignment 2:</b> Assemble a T-Bot plotter</a> <b>(due Thu, May 2)</b>
    	</span></td></tr>
    <tr><td>Apr 23</td><td><a href="/lectures/gcode/gcode.pdf"><b>G-Code</b></a> (and <a href="/lectures/gcode/stepperMusic/README.md">stepper-motor music</a>)</td></tr>
    <tr><td>Apr 25</td><td><b>Overview of CAM</b></td></tr>
    <tr><td>Apr 30</td><td><b>Project Pitches</b></td></tr>
    <tr><td>May 2</td><td><b>Knitting Machines</b>
    	<br><span class="assigned"><i>Assigned:</i>
    			<br>&emsp;<b>Final Project (Project Proposals due May 9; Project Due June 10 at 8:30AM)</b>
    	</span></td></tr>
    <tr><td>May 7</td><td><b>Jigs and Fixtures</b></td></tr>
    <tr><td>May 9</td><td><b>Interactive Machines </b></td></tr>
    <tr><td>May 14</td><td><b>Project Discussions</b></td></tr>
    <tr><td>May 16</td><td><b>Project Discussions</b></td></tr>
    <tr><td>May 21</td><td><b>Guest Lecture </b></td></tr>
    <tr><td>May 23</td><td><b>Guest Lecture</b></td></tr>
    <tr><td>May 28</td><td><b>Silly Machines and Kinetic Art  </b></td></tr>
    <tr><td>May 30</td><td><b>Work Session</b></td></tr>
    <tr><td>June 4</td><td><b>Work Session</b></td></tr>
    <tr><td>June 6</td><td><b>Work Session</b></td></tr>
    <tr><td>June 10</td><td><b>**Mon 8:30 - 11:30** Project Demonstrations</b></td></tr>
</tbody>
</table>

##### Things We've Made:
We consider ourselves "makers" and here are some examples of things that we've made. Check out [this page](/craft_inspiration.html) for other inspiration of things you can make (disclaimer, we didn't make these!) :)
<div class="tiles">
{% for post in site.posts %} {% include post-grid.html %} {% endfor %}
</div>
