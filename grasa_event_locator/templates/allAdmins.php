{% include "header.php" %}
<div class="row allUsersContainer">
    <div class="col-sm-12">
        <div class="twentyblock"></div>
        <h2 class="text-center">All Admins</h2>
        <button type="button" class="btn btn-info float-left" style="margin-bottom: 10px;" id="backBtn"> <i class="fa fa-chevron-left" aria-hidden="true" ></i> Back to Admin</button>
        
        <button type="button" class="btn btn-success float-right" id="addAdmin" data-toggle="modal" data-target="#addadminModal"><i class="fa fa-user-plus" aria-hidden="true"></i> Add Admin</button>
        
        <table class="table table-bordered">
              <thead class="thead-light">
                <tr>
                  <th scope="col">Email</th>
                  <th scope="col">Last Login</th>
                  <th scope="col" class="list-header-fix">Delete</th>
                </tr>
              </thead>
              <tbody class="provider-program-list">
                <tr>
                {% for user in userList %}
                  <th scope="row"><a href="mailto:{{ user.user }}">{{ user.user }}</a></th>
                  <th scope="row">time</th>
                  <td><button type="button" class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteModal">Delete</button></td>
                </tr>
                {% endfor %}

                <!--Delete Modal-->
                <div class="modal fade" id="deleteModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Are You Sure?</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                       Are you sure you want to delete this Admin? This cannot be undone.
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Never Mind</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal" onclick="">Confirm Delete</button>

                      </div>
                    </div>
                  </div>
                </div>

              </tbody>
            </table>
    </div>
</div>
<!-- add admin modal-->
<div class="modal fade" id="addadminModal" tabindex="-1" role="dialog" aria-labelledby="addadminModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="addadminModalLabel">Add New Admin</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
    <form id="theForm" class="needs-validation" novalidate>
      <div class="modal-body">

        <div class="row">
            <div class="col-sm-12">

                <div class="form-group col-md-12">
                    <label for="resetPW">Email Address</label>
                    <input type="email" id="resetPW" class="form-control" name="emailAddr" placeholder="" required autofocus>
                    <div class="invalid-feedback">
                        Please provide the new Admin's email.
                    </div>
                </div>

                <div class="form-group col-md-12">
                    <label for="myPW">Password</label>
                    <input type="password" id="myPW" class="form-control" name="current" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
                    <div class="invalid-feedback">
                      <p>Password must contain the following:</p>
                        <ul>
                          <li>A <b>lowercase</b> letter</li>
                          <li>A <b>capital (uppercase)</b> letter</li>
                          <li>A <b>number</b></li>
                          <li>Minimum <b>8 characters</b></li>
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
        </div>
      </div> 

      <div class="modal-footer">
        <button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
        <button type="submit" class="btn btn-success" value="Submit">Create Admin</button>
      </div>
    </form>
    </div>
  </div>
</div>


<script>
    var backBtn = document.getElementById('backBtn');
    backBtn.onclick = function(){
        window.location = 'admin.php'
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
            }
            form.classList.add('was-validated');
            
          }, false);
        });
      }, false);
    })();

</script>
{% include "footer.php" %}
