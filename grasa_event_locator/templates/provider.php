{% include "header.php" %}
<div class="container event-container">
    <div class="row">
    <!--Top Row-->
        <div class="col-sm-12 card">
            <div class="card-body">
                <div class="dropdown">
                  <a class="btn btn-link dropdown-toggle float-right " href="#" role="button" id="dropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <i class="fa fa-cogs" aria-hidden="true"></i>Settings
                  </a>

                  <div class="dropdown-menu dropdown-menu-right" aria-labelledby="dropdownMenuLink">
                    <a class="dropdown-item changeNameLink" href="#">Change Organization Name</a>
                      
                    <div class="dropdown-divider"></div>
                      
                    <a class="dropdown-item changeEmailLink" href="#">Change Email</a>
                    <a class="dropdown-item" data-toggle="modal" data-target="#changePWModal" href="#">Change Password</a>
                      
                    <div class="dropdown-divider"></div>
                     
                    <a class="dropdown-item" data-toggle="collapse" href="#collapseExample" role="button" aria-expanded="false" aria-controls="collapseExample">View Alternative Contact Info</a>
                    <a class="dropdown-item disabled" href="#">Edit Alternative Contact Info</a>
                  </div>
                </div>
                <h2>Provider Portal</h2>
                <hr>
                <div class="row"> <!-- card body row-->
                    <div class="col-sm-12">
                        <!--name-->
                         <span id="pName">
                             <h5 class="provider-info">
                                 <i class="fa fa-id-card fa-fw" aria-hidden="true"></i> {{ user.userinfo.org_name }}
                             </h5>
                        </span>
                        <!-- edit name-->
                        <form action="provider.php" method="post">
                            {% csrf_token %}
                             <div class="input-group mb-3 changeNameInput">
                                <input type="text" name="changename" class="form-control" placeholder="{{ user.userinfo.org_name }}" aria-label="{{ user.userinfo.org_name }}" value="{{ user.userinfo.org_name }}">
                              <div class="input-group-append">
                                <button class="btn btn-outline-primary changeNameSave" type="submit" id="button-addon2">Save</button>
                              </div>
                            </div>
                        </form>
                        <!--email-->
                         <span id="pEmail">
                             <h5 class="provider-info">
                                 <i class="fa fa-envelope fa-fw" aria-hidden="true"></i> {{ user }}
                             </h5>
                        </span>
                        <!-- edit email-->
                        <form method="POST" action="provider.php">{% csrf_token %}
                             <div class="input-group mb-3 changeEmailInput">
                                <input type="text" name="changeemail" class="form-control" placeholder="{{ user }}" aria-label="{{ user }}" value="{{ user }}">
                              <div class="input-group-append">
                                <button class="btn btn-outline-primary changeEmailSave" type="submit" id="button-addon2">Save</button>
                              </div>
                            </div>
                        </form>
                    </div>
                    <div class="collapse col-sm-12" id="collapseExample">
                          <hr>
                          <h5>Alternative Contact Information:
                              <button type="button" class="btn btn-link float-right regHelpBtn" data-toggle="modal" data-target="#HelpModal">What's this?</button>
                         </h5>
                          <i class="fa fa-user fa-fw" aria-hidden="true"></i> {{ user.userinfo.contact_name }}<br>
                          <i class="fa fa-envelope fa-fw" aria-hidden="true"></i> {{ user.userinfo.contact_email }}<br>
                          <i class="fa fa-phone fa-fw" aria-hidden="true"></i> {{ user.userinfo.contact_phone }}
                         
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
                <td><button type="button" class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteModal{{ myEvent.id }}" >Delete</button></td> 
              {% else %}
              
              <td><a href="{% url 'event_page' myEvent.id %}"><button type="button" class="btn btn-outline-info view-event">View</button></a></td>
              <td><a href="{% url 'edit_page' myEvent.id %}"><button type="button" class="btn btn-outline-info editBtn">Edit</button></a></td>
              <td><button type="button" class="btn btn-outline-danger"  data-toggle="modal" data-target="#deleteModal{{ myEvent.id }}">Delete</button></td>
              {% endif %}
              <!--Delete Modal-->
                <div class="modal fade" id="deleteModal{{ myEvent.id }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel3" aria-hidden="true">
                  <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel3">Are You Sure?</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                       Are you sure you want to delete this Event? This cannot be undone.
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Never Mind</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal" onclick="window.location.href='{% url 'deny_event' myEvent.id %}'">Confirm Delete</button>

                      </div>
                    </div>
                  </div>
                </div>
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
              <form id="theForm" method="POST" action="provider.php" class="needs-validation" novalidate>{% csrf_token %}
                  `<div class="modal-body">

                    <div class="row">
                        <div class="col-sm-12">

                            <div class="form-group col-md-12">
                                <label for="resetPW">Current Password</label>
                                <input type="password" id="currPW" class="form-control" name="current" placeholder="" required autofocus>
                                <div class="invalid-feedback">
                                    For security purposes please provide your current password.
                                </div>
                            </div>

                            <div class="form-group col-md-12">
                                <label for="myPW">New Password</label>
                                <input type="password" id="myPW" class="form-control" name="new" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>
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
    addSettings('changeNameLink', 'changeNameSave', 'changeNameInput', 'pName')
    //Change Email
    addSettings('changeEmailLink', 'changeEmailSave', 'changeEmailInput', 'pEmail')
    
    function addSettings(editBtn, saveBtn, inputBox, label){
        var editBtn = document.getElementsByClassName(editBtn)[0]
        var saveBtn = document.getElementsByClassName(saveBtn)[0]
        var inputBox = document.getElementsByClassName(inputBox)[0]
        var label = document.getElementById(label);
        editBtn.onclick = function(){
            label.style.display ="none";
            inputBox.style.visibility="visible";
            inputBox.style.height = "auto"
        }
        saveBtn.onclick = function(){
            inputBox.style.visibility = "hidden";
            setTimeout(function(){
                inputBox.style.height = "0px"
                label.style.display ="block";
            }, 500);

        }
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
