{% include "header.php" %}
<div class="container event-container">
    <div class="changeName-alert alert alert-success alert-dismissible fade show" role="alert">
              Organization Name Saved
    </div>
    <div class="row">
    <!--Top Row-->
        <div class="col-sm-9 card">
            <div class="card-body">
                <h2>Provider Portal</h2>
                <hr>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-envelope" aria-hidden="true"></i> {{ user }}</h5>
                    </div>
                    <div class="col-sm-6">
                        <a href="changePW.php"><button type="button" class="btn btn-link">Change Password</button></a>
                    </div>
                </div>
                <div class="row twentyblock"></div>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-id-card" aria-hidden="true"></i> {{ user.userinfo.org_name }}</h5>
                    </div>
                    <div class="col-sm-6">
                         <button type="button" class="btn btn-link changeNameLink">Change Name</button>
                        
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
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <p>Change Provider Logo:</p>
            <div class="card event-page-card">
              <img src="https://via.placeholder.com/150" class="card-img-top provider-logo-change" alt="Provider Logo">
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  <div class="input-group">

                      <div class="custom-file">
                        <input type="file" class="custom-file-input" id="inputGroupFile01">
                        <label class="custom-file-label" for="inputGroupFile01">Choose file...</label>
                      </div>
                    </div>

                </li>
              </ul>
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
    changeLink.onclick = function(){
        changeLink.style.display = "none";
        changeBox.style.visibility="visible";
    }
    changeSaveBtn.onclick = function(){
        changeLink.style.display = "block";
        changeBox.style.display="hidden";
        //Change Name popup
        $(".changeName-alert").show()
        setTimeout(function() {
            $(".changeName-alert").hide();
        }, 2000);
    }
    

</script>
{% include "footer.php" %}
