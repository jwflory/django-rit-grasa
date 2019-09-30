{% include "header.php" %}


  <div class="form-changePW">
	<form action="changePW.php">
		<label for="currentPW">Current Password</label>
		<input type="password" id="currentPW" class="form-control" name="current" required>
		</br>
		<label for="newPW">New Password</label>
		<input type="password" id="newPW" class="form-control" name="new" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
		<input type="checkbox" onclick="myFunction()"> &nbsp; Show Password
		</br>
		
		<input class="btn btn-lg btn-primary btn-block" type="submit" value="Submit">
	</form>
  </div>

<div id="message">
  <h3>Password must contain the following:</h3>
  <p id="letter" class="invalid">A <b>lowercase</b> letter</p>
  <p id="capital" class="invalid">A <b>capital (uppercase)</b> letter</p>
  <p id="number" class="invalid">A <b>number</b></p>
  <p id="length" class="invalid">Minimum <b>8 characters</b></p>
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

