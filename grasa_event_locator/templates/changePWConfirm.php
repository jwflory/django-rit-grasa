{% include "header.php" %}


  <div class="form-changePWConfirm">
	<form action="changePWConfirm.php" method="post">
	{% csrf_token %}
		
	</form>
  </div>

<div id="message">
  <h1>Changed Password Confirmation. </h1>
  <h3>Your password has been changed. Please click here to log in.</h3>
  
</div>



{% include "footer.php" %}

