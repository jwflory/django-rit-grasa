{% include "header.php" %}


  <div class="form-reset">
	<h1 class="h3 mb-3 font-weight-normal text-center">Reset Password</h1>
	<form action="resetPW.php">
    
		<label for="resetPW" class="sr-only">Email address</label>
		<input type="email" id="resetPW" class="form-control" placeholder="Enter Email..." required autofocus>
        <small id="emailHelp" class="form-text text-muted">Please provide the email connected to your account.</small>
		<input class="btn btn-lg btn-success btn-block top-20" type="submit" value="Submit">
        <p class="text-center top-20"><a href="login.php">Return to Login</a></p>
	</form>
  </div>


{% include "footer.php" %}

