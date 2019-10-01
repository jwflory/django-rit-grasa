<?php include 'header.php';?>

	
    <form class="form-signin">
      
      <h1 class="h3 mb-3 font-weight-normal text-center">GRASA Programs</h1>
      <label for="inputEmail" class="sr-only">Email address</label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus>
      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Password" required>
        
      
      <button class="btn btn-lg btn-success btn-block" type="submit">Login</button>
        <div class="twentyblock"></div>
      <div class="text-center">
          <p><a href="resetPW.php">Forgot Password?</a></p>
          <p>Don't have an account?<br><a href="register.php">Register</a></p>
      </div>
    </form>
 

<?php include 'footer.php';?>