{% include "header.php" %}
{% load static %}

<div class="container home-container">

	<div class="row">
    <!--Top Row-->
        <div class="col-sm-9 card">
            <div class="card-body">
                <h2>Admin Portal</h2>
                <hr>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-envelope" aria-hidden="true"></i> {{ user }} </h5>
                    </div>
                    <div class="col-sm-6">
                        <a href="changePW.php"><button type="button" class="btn btn-link float-right">Change Password</button></a>
                    </div>
                </div>
                <div class="twentyblock"></div>
                <hr>
                <button type="button" class="btn btn-secondary" id="allUsers"><i class="fa fa-user" aria-hidden="true"></i> View Providers</button>
                <button type="button" class="btn btn-warning" id="allAdmins"><i class="fa fa-user-secret" aria-hidden="true"></i> View Admins</button>
                <button type="button" class="btn btn-info float-right" id="allEvents"><i class="fa fa-calendar" aria-hidden="true"></i> View All Events</button>
                
            </div>
        </div>
        <div class="col-sm-3">
            <p class="">Change Site Logo:</p>
            <div class="card event-page-card">
              <img src="{% static "img/grasalogo.png" %}" class="card-img-top admin-logo-change" alt="Site Logo">
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
    

	<div class="twentyblock"></div>
	<div class="row">
        <div class="col-sm-12">
        <h2 class="row col-sm-12 top-20">Approval Requests</h2>
            <hr>
            
        
        <!--New User Approval-->
            <h4 class="top-20">Pending Users </h4>
                <table class="table table-bordered">
                  <thead class="thead-light">
                    <tr>
                      <th scope="col">Organization Name</th>
                      <th scope="col">Status</th>
                      <th scope="col" class="list-header-fix">Approve</th>
                      <th scope="col" class="list-header-fix">Deny</th>
                    </tr>
                  </thead>
                  <tbody class="provider-program-list">
                    <tr>
                    {% for pendingUser in pendingUserList %}
                      <th scope="row">{{ pendingUser.org_name }} - <a href="mailto:{{ pendingUser.user }}">{{ pendingUser.user }}</a></th>
                      <td>Pending</td>
                      <td><a href="{% url 'approve_user' pendingUser.id %}"><button type="button" class="btn btn-outline-success">Approve</button></a></td>
                      <td><a href="{% url 'deny_user' pendingUser.id %}"><button type="button" class="btn btn-outline-danger">Deny</button></a></td>
                    </tr>
                    {% endfor %}
                  </tbody>
                </table>
        <!--New Event Approval-->
            <div class="twentyblock"></div>
            <h4 class="top-20">New Events</h4>
                <table class="table  table-bordered">
                  <thead class="thead-light">
                    <tr>
                      <th scope="col">Event Name</th>
                      <th scope="col">Organization</th>
                      <th scope="col">Status</th>
                      <th scope="col" class="list-header-fix">View</th>
                      <th scope="col" class="list-header-fix">Approve</th>
                      <th scope="col" class="list-header-fix">Deny</th>
                    </tr>
                  </thead>
                  <tbody class="provider-program-list">
                    {% for pendingEvent in pendingEventList %}
                    <tr>
                      <th scope="row">{{ pendingEvent.title }}</th>
                      <td>{{ pendingEvent.user_id.org_name }}</td>
                      <td>Pending</td>
                      <td><a href="{% url 'event_page' pendingEvent.id %}"><button type="button" class="btn btn-outline-info view-event">View</button></a></td>
                      <td><a href="{% url 'approve_event' pendingEvent.id %}"><button type="button" class="btn btn-outline-success">Approve</button></a></td>
                      <td><a href="{% url 'deny_event' pendingEvent.id %}"><button type="button" class="btn btn-outline-danger">Deny</button></a></td>
                    </tr>
                    {% endfor %}
                  </tbody>
                </table>
        <!--New Event Approval-->
            <div class="twentyblock"></div>
            <h4 class="top-20">Updated Events</h4>
                <table class="table table-bordered">
                  <thead class="thead-light">
                    <tr>
                      <th scope="col">Event Name</th>
                      <th scope="col">Organization</th>
                      <th scope="col">Status</th>
                      <th scope="col" class="list-header-fix">View</th>
                      <th scope="col" class="list-header-fix">Approve</th>
                      <th scope="col" class="list-header-fix">Deny</th>
                    </tr>
                  </thead>
                  <tbody class="provider-program-list">
                    {% for pendingEdit in pendingEditList %}
                    <tr>
                      <th scope="row">{{ pendingEdit.title }}</th>
                      <td>{{ pendingEdit.user_id.org_name }}</td>
                      <td>Pending</td>
                      <td><a href="{% url 'event_page' pendingEdit.id %}"><button type="button" class="btn btn-outline-info view-event">View</button></a></td>
                      <td><a href="{% url 'approve_event' pendingEdit.id %}"><button type="button" class="btn btn-outline-success">Approve</button></a></td>
                      <td><a href="{% url 'deny_event' pendingEdit.id %}"><button type="button" class="btn btn-outline-danger">Deny</button></a></td>
                    </tr>
                    {% endfor %}
                  </tbody>
                </table>
        </div><!-- col-->
    </div><!--row-->
    <div class="twentyblock"></div>
	
</div>
<script>
    var viewBtns = document.getElementsByClassName('view-event')
    for(var i=0; i<viewBtns.length; i++){
        viewBtns[i].onclick = function(){
            window.location = 'event.php'
        }
    }
    
    //Toolbar Links
    var allUsersBtn = document.getElementById('allUsers');
    allUsersBtn.onclick = function(){
        window.location = 'allUsers.php'
    }
    var allUsersBtn = document.getElementById('allAdmins');
    allUsersBtn.onclick = function(){
        window.location = 'allAdmins.php'
    }
    var allEventsBtn = document.getElementById('allEvents');
    allEventsBtn.onclick = function(){
        window.location = 'allEvents.php'
    }
    
</script>
		
{% include "footer.php" %}
