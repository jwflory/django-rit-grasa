<?php include 'header.php';?>


<div class="form-register">
  <h1 class="h3 mb-3 font-weight-normal text-center top-20">Register as a Provider</h1>
  <form action="register.php">
  
    <label for="name">Organization Name</label>
	<input type="text" id="resetPW" class="form-control" required autofocus>
      
	<label for="resetPW" class="top-20">Email address</label>
	<input type="email" id="resetPW" class="form-control" required autofocus>
	
    <label for="myPW" class="top-20">Password</label>
    <input type="password" id="myPW" class="form-control" name="current" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
 
    <label for="confirmPW" class="top-20">Confirm Password</label>
	<input type="password" id="confirmPW" class="form-control" name="confirm" required>
	<input id="SPcheckbox" type="checkbox" onclick="myFunction()">
    <label for="SPcheckbox">&nbsp; Show Password</label>
	
    <input class="btn btn-lg btn-success btn-block top-20" type="submit" value="Submit">
  </form>
     <div class="text-center top-20">
          <p>Already have an account?<br><a href="login.php">Return to Login</a></p>
      </div>
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
  var x = document.getElementById("myPW");
  var y = document.getElementById("confirmPW");
  if (x.type === "password" || y.type === "password") {
    x.type = "text";
	y.type = "text";
  } else {
    x.type = "password";
	y.type = "password";
  }
}
</script>

<?php include 'footer.php';?>

