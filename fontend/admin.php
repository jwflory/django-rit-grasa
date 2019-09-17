<?php include 'header.php';?>

<div class="container home-container">
    <div class="row">
    <!-- most outer row-->
        <div class="col-3">
        <!--Left Content-->
            
            <div class="row">
			
            <!-- Left outer row -->
            <div class="card filter-card" style="width:100%">				
				
            <div class="card event-page-card">            
				
                  <div class="input-group">
						
                      <div class="custom-file">
                        <input type="file" class="custom-file-input" id="inputGroupFile01"
                          aria-describedby="inputGroupFileAddon01">
						  
                        <label class="custom-file-label" for="inputGroupFile01"> Choose Logo to change! </label>
                      </div>
                    </div>              
              
            </div>
        			
				</br>
			<div class="card-body text-center d-flex justify-content-center align-items-center flex-column">
				<p>Change Color [P]
					<input type="color" value="#ff0000">
				</p>  
				
				<p>Change Color [S] 
					<input type="color" value="#ff0000">
				</p>				
				
				<p>Change Color [T]
					<input type="color" value="#ff0000">
				</p>
				</br>
				<div>
                        <button type="button" class="btn btn-link">Change Password? </button>
                    </div>
			</div>		
			
				<input class="btn btn-primary" type="submit" value="Submit">				
					 
		</div>
	</div>
			        
</div>
	
	<div class="col-9">
        <!--Right Content-->
            <div class="card program-list-card">
              <div class="card-header">                
              </div>
              <div class="card-body program-list-card-body">
                <!--New User Approval-->
					<div class="card event-card" id="event1">
                      <div class="card-body">
                        <h5 class="card-title">New User</h5>
                        <table class="table table-hover">
							<thead>
							<tr>
							  <th scope="col">User Name</th>
							  <th scope="col">Status</th>
							  <th scope="col" class="list-header-fix">Approve</th>
							  <th scope="col" class="list-header-fix">Deny</th>
							</tr>
						  </thead>
						  <tbody class="provider-program-list">
							<tr>
							  <th scope="row">Post Malone</th>
							  <td>Approved</td>
							  <td><button type="button" class="btn btn-info">Approve</button></td>
							  <td><button type="button" class="btn btn-danger">Deny</button></td>
							</tr>
							<tr class="warning">
							  <th scope="row">Drake</th>
							  <td>Pending</td>
							  <td><button type="button" class="btn btn-info disabled">Approve</button></td>
							  <td><button type="button" class="btn btn-danger disabled">Deny</button></td>
							</tr>
						  </tbody>
						</table>
					
					<!--New Events Approval-->
                        <h5 class="card-title">New Events</h5>
                        <table class="table table-hover">
							<thead>
							<tr>
							  <th scope="col">Events Name</th>
							  <th scope="col">Status</th>
							  <th scope="col" class="list-header-fix">Approve</th>
							  <th scope="col" class="list-header-fix">Deny</th>
							</tr>
						  </thead>
						  <tbody class="provider-program-list">
							<tr>
							  <th scope="row">Cooking</th>
							  <td>Approved</td>
							  <td><button type="button" class="btn btn-info">Approve</button></td>
							  <td><button type="button" class="btn btn-danger">Deny</button></td>
							</tr>
							<tr class="warning">
							  <th scope="row">Swimming</th>
							  <td>Pending</td>
							  <td><button type="button" class="btn btn-info disabled">Approve</button></td>
							  <td><button type="button" class="btn btn-danger disabled">Deny</button></td>
							</tr>
						  </tbody>
						</table>
					
					<!--Edit Events-->	
						<h5 class="card-title">Edit Events</h5>
                        <table class="table table-hover">
							<thead>
							<tr>
							  <th scope="col">Events Name</th>
							  <th scope="col">Status</th>
							  <th scope="col" class="list-header-fix">Approve</th>
							  <th scope="col" class="list-header-fix">Deny</th>
							</tr>
						  </thead>
						  <tbody class="provider-program-list">
							<tr>
							  <th scope="row">Martial Arts</th>
							  <td>Approved</td>
							  <td><button type="button" class="btn btn-info">Approve</button></td>
							  <td><button type="button" class="btn btn-danger">Deny</button></td>
							</tr>
							<tr class="warning">
							  <th scope="row">Sports</th>
							  <td>Pending</td>
							  <td><button type="button" class="btn btn-info disabled">Approve</button></td>
							  <td><button type="button" class="btn btn-danger disabled">Deny</button></td>
							</tr>
						  </tbody>
						</table>
						
               </div>
            </div>
        </div>
		
	</div>	

		
<?php include 'footer.php';?>
