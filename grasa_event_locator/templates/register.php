{% include "header.php" %}

<div class="container register-container">
	<div class="row">
		<div class="col-sm-12">
					
			<div class="form-register">

        {% if emailTaken %}
        <div class="alert alert-warning" role="alert">
          An account has already been registered with this email address, please use another.
        </div>
        {% endif %}
  
				<h1 class="h3 mb-3 font-weight-normal text-center top-20">Register as a Provider</h1>
                <p class="text-muted text-center">Provider accounts must be approved by administrators before events can be made.</p>
                
				<form id="theForm" action="register.php" method="post" class="needs-validation" novalidate>
				{% csrf_token %}
                    <div class="row">
                        <div class="col-sm-6">
                            <div class="form-group col-md-12">
                                <label for="name">Organization Name</label>
                                <input type="text" id="resetPW" class="form-control" name="orgName" required placeholder="Organization Name..." autofocus>
                                <div class="invalid-feedback">
                                    Please provide the name of your organization. 
                                </div>
                                <!--<div class="invalid-feedback">
                                    An organization with this name is already registered.
                                </div>-->
                            </div>

                            <div class="form-group col-md-12">
                                <label for="resetPW">Email Address</label>
                                <input type="email" id="resetPW" class="form-control" name="emailAddr" placeholder="Email..." required autofocus>
                                <div class="invalid-feedback">
                                    Please provide an email your organization.
                                </div>
                                <!--<div class="invalid-feedback">
                                    An organization with this email is already registered.
                                </div>-->
                            </div>
                            
                            <div class="form-group col-md-12">
                                <label for="myPW">Password</label>
                                <input type="password" id="myPW" class="form-control" name="current" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
                                <div class="invalid-feedback">
                                  <p>Password must contain the following:</p>
                                    <ul>
                                      <li id="letter">A <b>lowercase</b> letter</li>
                                      <li id="capital">A <b>capital (uppercase)</b> letter</li>
                                      <li id="number">A <b>number</b></li>
                                      <li id="length">Minimum <b>8 characters</b></li>
                                    </ul>
                                </div>
                            </div>

                            <div class="form-group col-md-12">
                                <label for="confirmPW">Confirm Password</label>

                                <input type="password" id="confirmPW" class="form-control" name="confirm" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" required>
                                <div class="invalid-feedback">
                                    Passwords must match.
                                </div>
                                <input id="SPcheckbox" type="checkbox" onclick="myFunction()">
                                <label for="SPcheckbox">&nbsp; Show Password</label>
                            </div>

                        </div>
                        <div class="col-sm-6">
                            <fieldset class="pocFieldset">
                                <legend>Alternative Contact Information</legend>
                                   <div class="form-row">
                                        <div class="form-group col-md-12">
                                          <label for="contactname">Name</label>
                                          <input type="text" class="form-control" id="contactname" placeholder="Name..." name="contact_name" required>
                                            <div class="invalid-feedback">
                                                Please provide your alternative contact's name.
                                            </div>
                                        </div>
                                        <div class="form-group col-md-12">
                                          <label for="email">Email</label>
                                          <input type="email" class="form-control" id="email" placeholder="Email..." name="contact_email" required>
                                            <div class="invalid-feedback">
                                                Please provide your alternative contact's  email. This must be different from your Organization's email.
                                            </div>
                                        </div>
                                        <div class="form-group col-md-12">
                                          <label for="phone">Phone</label>
                                          <input type="tel" class="form-control" id="phone" placeholder="xxx-xxx-xxxx" name="contact_phone" pattern="^\d{3}-\d{3}-\d{4}$" required>
                                            <div class="invalid-feedback">
                                                Please provide your alternative contact's phone number and format as xxx-xxx-xxxx.
                                            </div>
                                        </div>
                                      </div>
                                 </fieldset>
                                <button type="button" class="btn btn-link float-right regHelpBtn" data-toggle="modal" data-target="#HelpModal">What's this?</button>
                                <!-- Help Modal -->
                                <div class="modal fade" id="HelpModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel2" aria-hidden="true">
                                  <div class="modal-dialog" role="document">
                                    <div class="modal-content">
                                      <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel2">Alternative Contact Information</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                          <span aria-hidden="true">&times;</span>
                                        </button>
                                      </div>
                                      <div class="modal-body">
                                        <p>Alternative Contact Information is information for someone else in your organization. This will be used by the administrators in the event that the person who created the account is unreachable, so that the organization will still have access to their events. This information will not be shown with your events.</p>
                                          <p>More Questions? Please contact us at <a href="mailto:johndoe@email.com">johndoe@email.com</a></p>
                                      </div>
                                      <div class="modal-footer">
                                        <button type="button" class="btn btn-primary" data-dismiss="modal">Ok</button>
                                      </div>
                                    </div>
                                  </div>
                                </div>

                        </div>
                    </div>
                    <div class="row">
                            <div class="col-12 registerBtnRow">
                                <button type="submit" class="btn btn-lg btn-success btn-block top-20" id="submitBtn">Submit</button>
                                <div class="text-center top-20">
                                  <p>Already have an account?<br><a href="login.php">Return to Login</a></p>
                                </div>
                            </div>
                            
                        
                        
                            <!--Ok Modal-->
                            <div class="modal fade" id="submitModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                              <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                  <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Registration Confirmation</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                      <span aria-hidden="true">&times;</span>
                                    </button>
                                  </div>
                                  <div class="modal-body">
                                   <p>An Administrator will look over your registration. You will not be able to add events until your account is approved. Are you sure you want to submit your registration?</p>
                                  </div>
                                  <div class="modal-footer">
                                      <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="fa fa-times" aria-hidden="true"></i> Cancel</button>
                                    <button type="button" class="btn btn-success" id="okBtn"><i class="fa fa-check" aria-hidden="true"></i> Register</button>

                                  </div>
                                </div>
                              </div>
                            </div>
                        </div>
	
				</form>
			</div>
		</div>
	</div>
</div>
	
			
<script>
    //ok on submit
    var okBtn = document.getElementById('okBtn');
    okBtn.onclick = function(){
        //SUBMITS the form
        $('form').submit()
        //window.location = 'index.php';
    }
    
    //confirm password extra validation
    $('#confirmPW').keyup(function() {
      if ( document.getElementById("confirmPW").value != document.getElementById("myPW").value ) {
          if(document.getElementById("theForm").classList.contains('was-validated')){
              $('#confirmPW').removeClass( "is-invalid" );
              $('#confirmPW').addClass( "is-valid" );
              $('#confirmPW').css('border', 'solid 1px #28a745');
          }
      }
    });
    
   
    //password validation - Lei
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

	
    //validation
    (function() {
      'use strict';
      window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
          form.addEventListener('submit', function(event) {
            if ( document.getElementById("confirmPW").value != document.getElementById("myPW").value ) {
                //if passwords don't match
                event.preventDefault();
                event.stopPropagation();
                $('#confirmPW').addClass( "is-invalid" );
                $('#confirmPW').css('border', 'solid 1px #dc3545')
                $('#confirmPW').css('background-image', 'none'); 
            }else if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
            }else{
                event.preventDefault();
                event.stopPropagation();
                $('#submitModal').modal('show');
            }
            form.classList.add('was-validated');
            
          }, false);
        });
      }, false);
    })();
	
	
	//password validation check mark
	var myInput = document.getElementById("myPW");
	var letter = document.getElementById("letter");
	var capital = document.getElementById("capital");
	var number = document.getElementById("number");
	var length = document.getElementById("length");

	// When the user clicks on the password field, show the message box
	myInput.onfocus = function() {
	  document.getElementById("message").style.display = "block";
	}

	// When the user clicks outside of the password field, hide the message box
	myInput.onblur = function() {
	  document.getElementById("message").style.display = "none";
	}

	// When the user starts to type something inside the password field
	myInput.onkeyup = function() {
	  // Validate lowercase letters
	  var lowerCaseLetters = /[a-z]/g;
	  if(myInput.value.match(lowerCaseLetters)) {  
		letter.classList.remove("invalid");
		letter.classList.add("valid");
	  } else {
		letter.classList.remove("valid");
		letter.classList.add("invalid");
	  }
	  
	  // Validate capital letters
	  var upperCaseLetters = /[A-Z]/g;
	  if(myInput.value.match(upperCaseLetters)) {  
		capital.classList.remove("invalid");
		capital.classList.add("valid");
	  } else {
		capital.classList.remove("valid");
		capital.classList.add("invalid");
	  }

	  // Validate numbers
	  var numbers = /[0-9]/g;
	  if(myInput.value.match(numbers)) {  
		number.classList.remove("invalid");
		number.classList.add("valid");
	  } else {
		number.classList.remove("valid");
		number.classList.add("invalid");
	  }
	  
	  // Validate length
	  if(myInput.value.length >= 8) {
		length.classList.remove("invalid");
		length.classList.add("valid");
	  } else {
		length.classList.remove("valid");
		length.classList.add("invalid");
	  }
	}
	
	//phone number auto-format
	//the dashes between phone numbers will auto fill while typing
	function phone_formatting(ele,restore) {
	  var new_number,
		  selection_start = ele.selectionStart,
		  selection_end = ele.selectionEnd,
		  number = ele.value.replace(/\D/g,'');
	  
	  // automatically add dashes
	  if (number.length > 2) {
		// matches: 123 || 123-4 || 123-45
		new_number = number.substring(0,3) + '-';
		if (number.length === 4 || number.length === 5) {
		  // matches: 123-4 || 123-45
		  new_number += number.substr(3);
		}
		else if (number.length > 5) {
		  // matches: 123-456 || 123-456-7 || 123-456-789
		  new_number += number.substring(3,6) + '-';
		}
		if (number.length > 6) {
		  // matches: 123-456-7 || 123-456-789 || 123-456-7890
		  new_number += number.substring(6);
		}
	  }
	  else {
		new_number = number;
	  }
	  
	  // if value is heigher than 12, last number is dropped
	  // if inserting a number before the last character, numbers
	  // are shifted right, only 12 characters will show
	  ele.value =  (new_number.length > 12) ? new_number.substring(0,12) : new_number;
	  
	  // restore cursor selection,
	  // prevent it from going to the end
	  // UNLESS
	  // cursor was at the end AND a dash was added
	  
	  if (new_number.slice(-1) === '-' && restore === false
		  && (new_number.length === 8 && selection_end === 7)
			  || (new_number.length === 4 && selection_end === 3)) {
		  selection_start = new_number.length;
		  selection_end = new_number.length;
	  }
	  else if (restore === 'revert') {
		selection_start--;
		selection_end--;
	  }
	  ele.setSelectionRange(selection_start, selection_end);

	}
	  
	function phone_number_check(field,e) {
	  var key_code = e.keyCode,
		  key_string = String.fromCharCode(key_code),
		  press_delete = false,
		  dash_key = 189,
		  delete_key = [8,46],
		  direction_key = [33,34,35,36,37,38,39,40],
		  selection_end = field.selectionEnd;
	  
	  // delete key was pressed
	  if (delete_key.indexOf(key_code) > -1) {
		press_delete = true;
	  }
	  
	  // only force formatting is a number or delete key was pressed
	  if (key_string.match(/^\d+$/) || press_delete) {
		phone_formatting(field,press_delete);
	  }
	  // do nothing for direction keys, keep their default actions
	  else if(direction_key.indexOf(key_code) > -1) {
		// do nothing
	  }
	  else if(dash_key === key_code) {
		if (selection_end === field.value.length) {
		  field.value = field.value.slice(0,-1)
		}
		else {
		  field.value = field.value.substring(0,(selection_end - 1)) + field.value.substr(selection_end)
		  field.selectionEnd = selection_end - 1;
		}
	  }
	  // all other non numerical key presses, remove their value
	  else {
		e.preventDefault();
	//    field.value = field.value.replace(/[^0-9\-]/g,'')
		phone_formatting(field,'revert');
	  }

	}

	document.getElementById('phone').onkeyup = function(e) {
	  phone_number_check(this,e);
	}

</script>

{% include "footer.php" %}
