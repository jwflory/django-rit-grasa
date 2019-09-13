<?php include 'header.php';?>


  <div class="form-reset">
	<h1 class="h3 mb-3 font-weight-normal">Reset your password</h1>
	<form action="resetPW.php">
    
		<label for="resetPW" class="sr-only">Email address</label>
		<input type="email" id="resetPW" class="form-control" placeholder="Email address" required autofocus>
		
		</br>
		<input class="btn btn-lg btn-primary btn-block" type="submit" value="Submit">
	</form>
  </div>


<?php include 'footer.php';?>

