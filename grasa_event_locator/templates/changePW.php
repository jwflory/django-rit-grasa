{% include "header.php" %}


  <div class="form-changePW">
	<form action="changePW.php" method="post">
	{% csrf_token %}
		<label for="currentPW">Current Password</label>
		<input type="password" id="currentPW" class="form-control" name="current" required>
		</br>
		<label for="newPW">New Password</label>
		<input type="password" id="newPW" class="form-control" name="new" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
		<input type="checkbox" onclick="myFunction()"> &nbsp; Show Password
		</br>
		
		<input class="btn btn-lg btn-primary btn-block" type="submit" value="Submit"><a href="changePWConfirm.php>submit</a>
		
	</form>
  </div>


<script>
function myFunction() {
  var x = document.getElementById("currentPW");
  var y = document.getElementById("newPW");
  if (x.type === "password" || y.type === "password") {
    x.type = "text";
	y.type = "text";
  } else {
    x.type = "password";
	y.type = "password";
  }
}
</script>

{% include "footer.php" %}

