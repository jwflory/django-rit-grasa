<?php include 'header.php';?>


  <div class="form-changePW">
	<form action="changePW.php">
		<label for="currentPW">Current Password</label>
		<input type="current" id="currentPW" class="form-control" name="current" required>
 
		<label for="newPW">New Password</label>
		<input type="new" id="newPW" class="form-control" name="new" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>

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

<?php include 'footer.php';?>

