<?php include 'header.php';?>

<div class="container home-container">

	<div class="row">
    <!--Top Row-->
        <div class="col-sm-9 card">
            <div class="card-body">
                <h2>Admin Portal</h2>
                <hr>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-envelope" aria-hidden="true"></i> admin@grasa.org</h5>
                    </div>
                    <div class="col-sm-6">
                        <button type="button" class="btn btn-link">Change Password</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <p class="">Change Site Logo:</p>
            <div class="card event-page-card">
              <img src="media/grasalogo.png" class="card-img-top admin-logo-change" alt="Site Logo">
              <ul class="list-group list-group-flush">
                <li class="list-group-item">
                  <div class="input-group">

                      <div class="custom-file">
                        <input type="file" class="custom-file-input" id="inputGroupFile01"
                          aria-describedby="inputGroupFileAddon01">
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
            <h4 class="top-20">New Users</h4>
                <table class="table table-hover table-bordered">
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
                      <th scope="row">Monroe Middle School</th>
                      <td>Approved</td>
                      <td><button type="button" class="btn btn-outline-success">Approve</button></td>
                      <td><button type="button" class="btn btn-outline-danger">Deny</button></td>
                    </tr>
                    <tr>
                      <th scope="row">Rush Lower School</th>
                      <td>Pending</td>
                      <td><button type="button" class="btn btn-outline-success">Approve</button></td>
                      <td><button type="button" class="btn btn-outline-danger">Deny</button></td>
                    </tr>
                  </tbody>
                </table>
        <!--New Event Approval-->
            <h4 class="top-20">New Events</h4>
                <table class="table table-hover table-bordered">
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
                    <tr>
                      <th scope="row">Soccer Program</th>
                      <td>Rochester Middle School</td>
                      <td>Approved</td>
                      <td><button type="button" class="btn btn-outline-info view-event">View</button></td>
                      <td><button type="button" class="btn btn-outline-success">Approve</button></td>
                      <td><button type="button" class="btn btn-outline-danger">Deny</button></td>
                    </tr>
                    <tr>
                      <th scope="row">Cooking for Kids!</th>
                      <td>Henrietta Elementary School</td>
                      <td>Pending</td>
                      <td><button type="button" class="btn btn-outline-info view-event">View</button></td>
                      <td><button type="button" class="btn btn-outline-success">Approve</button></td>
                      <td><button type="button" class="btn btn-outline-danger">Deny</button></td>
                    </tr>
                  </tbody>
                </table>
        <!--New Event Approval-->
            <h4 class="top-20">Updated Events</h4>
                <table class="table table-hover table-bordered">
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
                    <tr>
                      <th scope="row">Better Soccer Program</th>
                      <td>Rochester Middle School</td>
                      <td>Approved</td>
                      <td><button type="button" class="btn btn-outline-info view-event">View</button></td>
                      <td><button type="button" class="btn btn-outline-success">Approve</button></td>
                      <td><button type="button" class="btn btn-outline-danger">Deny</button></td>
                    </tr>
                    <tr>
                      <th scope="row">Cooking for Adults!</th>
                      <td>Henrietta Elementary School</td>
                      <td>Pending</td>
                      <td><button type="button" class="btn btn-outline-info view-event">View</button></td>
                      <td><button type="button" class="btn btn-outline-success">Approve</button></td>
                      <td><button type="button" class="btn btn-outline-danger">Deny</button></td>
                    </tr>
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
        
    
</script>
		
<?php include 'footer.php';?>
