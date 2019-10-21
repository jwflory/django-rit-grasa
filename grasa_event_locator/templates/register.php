{% include "header.php" %}


<div class="form-register">
  
  <h1 class="h3 mb-3 font-weight-normal text-center top-20">Register as a Provider</h1>
  <form action="register.php" method="post">
  
  {% csrf_token %}
  
    <label for="name">Organization Name</label>
	<input type="text" id="resetPW" class="form-control" name="orgName" required autofocus>
    
	<div class="alert">
		Organization name already exist !
    </div>

	<label for="resetPW">Email address</label>
	<input type="email" id="resetPW" class="form-control" name="emailAddr" required autofocus>
	
	<div class="alert">
		Email already exist !
    </div>
	
    <label for="myPW">Password</label>
    <input type="password" id="myPW" class="form-control" name="current" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
 
    <label for="confirmPW" class="top-20">Confirm Password</label>
	<input type="password" id="confirmPW" class="form-control" name="confirm" required>
	<input id="SPcheckbox" type="checkbox" onclick="myFunction()">
    <label for="SPcheckbox">&nbsp; Show Password</label>

	<!--Pop-up confirmation page after clicking submit button on Registration form-->
	<div class="row">
        <div class="col-12">
            <button type="button" class="btn btn-lg btn-success btn-block top-20" data-toggle="modal" data-target="#submitModal">Submit</button>
        </div>
        <!--Cancel Modal-->
        <div class="modal fade" id="submitModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Confirmation</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
               <p>An Administrator will look over your registration.</p>
			   More questions?<br>
			   Please Contact Us: <a href="mailto:first@email.address,second@email.address,third@email.address">johndoe@gmail.com</a>
              </div>
              <div class="modal-footer">
                
                <button type="button" class="btn btn-primary" id="cancelBtn">OK</button>
                
              </div>
            </div>
          </div>
        </div>
	</div>
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

	//Ok Button returns to provider page
    var cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.onclick = function(){
        window.location = 'provider.php'
    }
   
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

{% include "footer.php" %}
