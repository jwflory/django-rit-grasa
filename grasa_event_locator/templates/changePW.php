{% include "header.php" %}


  <div class="form-changePW">
	<form action="changePW.php" method="post">
	{% csrf_token %}
		<label for="currentPW">Current Password</label>
		<input type="password" id="currentPW" class="form-control" name="current" required autofocus>
		</br>
		<label for="newPW">New Password</label>
		<input type="password" id="newPW" class="form-control" name="new" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
		<input type="checkbox" onclick="myFunction()"> &nbsp; Show Password
		</br>
		
				
	<!--Pop-up confirmation page after clicking submit button on Registration form-->
	<div class="row">
        <div class="col-12">
            <button type="submit" class="btn btn-lg btn-primary btn-block" data-toggle="modal" data-target="#submitModal">Submit</button>
        </div>
        <!--Cancel Modal-->
        <div class="modal fade" id="submitModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Change Password Confirmation</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
               <p>Your Password has been changed!</p>
			   
			   Please <a href="login.php">click here to login</a>
              </div>
              
            </div>
          </div>
        </div>
	</div>
		
	</form>
  </div>


<script>

//Ok Button returns to provider page
    var cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.onclick = function(){
        window.location = 'provider.php'
    }
	
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

