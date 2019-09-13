<?php include 'header.php';?>


<div class="form-register">
  <h1 class="h3 mb-3 font-weight-normal">Register your account</h1>
  <form action="register.php">
  
	<label for="resetPW">Email address</label>
	<input type="email" id="resetPW" class="form-control" required autofocus>
	
    <label for="currentPW">Current Password</label>
    <input type="current" id="currentPW" class="form-control" name="current" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
 
    <label for="confirmPW">Confirm Password</label>
	<input type="confirm" id="confirmPW" class="form-control" name="confirm" required>

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

