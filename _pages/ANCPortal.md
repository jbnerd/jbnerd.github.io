---
layout: archive
permalink: /projects/ANCPortal/
author_profile: true
---

{{ page.excerpt | markdownify }}

# ANC Portal
<small>Oct 2016 - Mar 2017</small>

<p>ANC stands for the famous All Night Canteen of BITS Pilani, which serves a variety of good quality food items with the uniqueness of operating till late nights. It often sees much crowd pouring in at night resulting in large queues near the billing counter. To reduce this queue, the then President of the Students' Union (2016-17) proposed the idea of ANC Portal.</p>

<p>This website would automate the billing process reducing the size of queues near the billing counter. This website was developed and hosted under coding club after getting the project of developing such a system. The backend for the website based system was writtend in Django 1.9.1 in python 3.5.2.</p>

<p>Use Case
	<ul>
		<li>An online ordering website is hosted on a public server for students to order their food. The order is recorded on the server's database.</li>
		<li>A tablet is kept at the ANC where the user will have to confirm the order that they placed to generate the bill. The student shall not be charged for their orders until the bill is generated.</li>
		<li>Each student user can login to the website to place their orders using their college email accounts.</li>
		<li>Each of the student user is prompted for basic information which is not readily available via the gmail API.</li>
		<li>Each of them has to set a 6 digit personal pin which is used to verify the placed order and generate the bill.</li>
		<li>After each order a system generated mail is sent to the respective user's email account, stating the details of the order along with a 6 digit random number.</li>
		<li>A combination of the sent random number and the personal pin shall act as the verification model for confirming the order.</li>
		<li>If a user wishes to cancel the order, they can do so by returning the unused bill to the billing operator, who can then use his special credentials to cancel the order with the given bill number.</li>
	</ul>
</p>

<p>Find the complete code for the website <a href="https://github.com/jbnerd/Anc_Portal">here</a>, also check out the website <a href="https://ancportal.herokuapp.com">here</a>. (Don't forget to login with BITSMail!!)</p>

<p>My Contribution:
	<ul>
		<li>Developing the complete back-end of the website, integration with the front-end and hosting it on heroku using git.</li>
	</ul>
</p>

<p>Learning Outcomes:
	<ul>
		<li>Working with Google+ APIs for Google Login.</li>
		<li>Working with Google's SMTP email server.</li>
		<li>Scaling of softwares for production mode.</li>
	</ul>
</p>