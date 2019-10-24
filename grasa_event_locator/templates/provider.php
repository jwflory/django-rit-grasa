{% include "header.php" %}
<div class="container event-container">
    <div class="row">
    <!--Top Row-->
        <div class="col-sm-9 card">
            <div class="card-body">
                <div class="dropdown">
                  <a class="btn btn-link dropdown-toggle float-right " href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <i class="fa fa-cog" aria-hidden="true"></i>Settings
                  </a>

                  <div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuLink">
                    <a class="dropdown-item changeNameLink" href="#">Change Name</a>
                    <a class="dropdown-item changeNameLink" href="#">Change Logo</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Change Email</a>
                    <a class="dropdown-item" data-toggle="modal" data-target="#changePWModal">Change Password</a>
                    <div class="dropdown-divider"></div>
                    <a class="dropdown-item" href="#">Edit Additional Contact Info</a>
                  </div>
                </div>
                <h2>Provider Portal</h2>
                <hr>
                <div class="row"> <!-- card body row-->
                    <div class="col-sm-6">
                        <!--email-->
                         <h5 class="provider-info">
                             <i class="fa fa-envelope" aria-hidden="true"></i>
                             {{ user }}
                        </h5>
                        <div class="twentyblock"></div>
                        <!--name-->
                         <span id="pName">
                             <h5 class="provider-info">
                                 <i class="fa fa-id-card" aria-hidden="true"></i>{{ user.userinfo.org_name }}
                             </h5>
                        </span>
                        <!-- edit name-->
                        <form action="provider.php" method="post">
                            {% csrf_token %}
                             <div class="input-group mb-3 changeNameInput">
                                <input type="text" class="form-control" placeholder="{{ user.userinfo.org_name }}" aria-label="{{ user.userinfo.org_name }}" value="{{ user.userinfo.org_name }}" name="changename">
                              <div class="input-group-append">
                                <button class="btn btn-outline-primary changeNameSave" type="submit" id="button-addon2">Save</button>
                              </div>
                            </div>
                        </form>
                    </div>
                    <div class="col-sm-6">
                    
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <p>Logo:</p>
            <div class="card event-page-card">
              <img src="https://via.placeholder.com/150" class="card-img-top provider-logo-change" alt="Provider Logo">
            </div>
        </div>
        </div>
    
    <div class="row">
    <!-- Bottom Row -->
        <h2 class="program-header w-100">Events and Programs<button type="button" class="btn btn-success float-right" id="createEvent"> <i class="fa fa-plus" aria-hidden="true"></i> Add New Event</button></h2>
        <table class="table table-bordered">
          <thead class="thead-light">
            <tr>
              <th scope="col">Program Name</th>
              <th scope="col">Status</th>
              <th scope="col" class="list-header-fix">View</th>
              <th scope="col" class="list-header-fix">Edit</th>
              <th scope="col" class="list-header-fix">Delete</th>
            </tr>
          </thead>
          <tbody class="provider-program-list">
            {% for myEvent in myEventList %}
            <tr>
              <th scope="row">{{ myEvent.title }}</th>
              {% if myEvent.isPending == 1 %}
              <td>Submitted for Approval</td>
              {% else %}
              <td>Approved</td>
              {% endif %}
              {% if myEvent.isPending == 1 %}
                <td><a href="{% url 'event_page' myEvent.id %}"><button type="button" class="btn btn-outline-info view-event" disabled>View</button></a></td>
                <td><a href="{% url 'edit_page' myEvent.id %}"><button type="button" class="btn btn-outline-info editBtn" disabled>Edit</button></a></td>
                <td><button type="button" class="btn btn-outline-danger" >Delete</button></td> 
              {% else %}
              
              <td><a href="{% url 'event_page' myEvent.id %}"><button type="button" class="btn btn-outline-info view-event">View</button></a></td>
              <td><a href="{% url 'edit_page' myEvent.id %}"><button type="button" class="btn btn-outline-info editBtn">Edit</button></a></td>
              <td><button type="button" class="btn btn-outline-danger">Delete</button></td>
              {% endif %}
            </tr>
            {% endfor %}
          </tbody>
        </table>

    </div>

</div>
    <!-- Change Password Modal -->
    <div class="modal fade" id="changePWModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Change Password</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
              <form id="theForm" class="needs-validation" novalidate>
      <div class="modal-body">

        <div class="row">
            <div class="col-sm-12">

                <div class="form-group col-md-12">
                    <label for="resetPW">Current Password</label>
                    <input type="password" id="currPW" class="form-control" name="emailAddr" placeholder="" required autofocus>
                    <div class="invalid-feedback">
                        For security purposes please provide your current password.
                    </div>
                </div>

                <div class="form-group col-md-12">
                    <label for="myPW">New Password</label>
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
                    <label for="confirmPW">Confirm New Password</label>

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
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="submit" class="btn btn-primary" value="Submit">Save Changes</button>
      </div>
    </form>
        </div>
      </div>
    </div>
<script>
    //create new event button
    var createBtn = document.getElementById('createEvent');
    createBtn.onclick = function(){
        window.location = 'createEvent.php'
    }

    //edit event button
    var editBtns = document.getElementsByClassName('editBtn');
    for(var i=0; i<editBtns.length; i++){
        //check for disabled button
        if(!$(editBtns[i]).hasClass("disabled")){
            editBtns[i].onclick = function(){
                window.location = 'editEvent.php'
            }
        }
    }
    
    //Change Name
    var changeLink = document.getElementsByClassName('changeNameLink')[0];
    var changeSaveBtn = document.getElementsByClassName('changeNameSave')[0];
    var changeBox = document.getElementsByClassName('changeNameInput')[0];
    var nameBox = document.getElementById('pName');
    changeLink.onclick = function(){
        nameBox.style.display ="none";
        changeBox.style.visibility="visible";
    }
    changeSaveBtn.onclick = function(){
        changeBox.style.display = "hidden";
        nameBox.style.display ="block";
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
