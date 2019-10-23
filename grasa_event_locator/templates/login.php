{% include "header.php" %}
{% load static %}
	
    <form class="form-signin" method="post">{% csrf_token %}
      
    
      <h1 class="h3 mb-3 font-weight-normal text-center">GRASA Programs Login</h1>
      <p class="text-muted text-center">You do not need an account to browse events, only if you would like to add your own event.</p>
      <!-- These are used to check for pending users or failed logins and give feedback -->
      {% if pendingUser %}
      <div class="alert alert-warning" role="alert">
          Account has yet to be approved
      </div>
      {% endif %}
      {% if wrongCredentials %}
      <div class="alert alert-danger" role="alert">
          Incorrect Email or Password
      </div>
      {% endif %}
      <label for="inputEmail" class="sr-only">Email Address</label>
      <input type="email" id="inputEmail" class="form-control" placeholder="Email Address" name="email" required autofocus>

      <label for="inputPassword" class="sr-only">Password</label>
      <input type="password" id="inputPassword" class="form-control" placeholder="Password" name="password" required>
      
      <button class="btn btn-lg btn-success btn-block" type="submit">Login</button>
        <div class="twentyblock"></div>
      <div class="text-center">
          <p><a href="resetPW.php">Forgot Password?</a></p>
          <p>Don't have an account?<br><a href="register.php">Register</a></p>
      </div>
    </form>
 

{% include "footer.php" %}