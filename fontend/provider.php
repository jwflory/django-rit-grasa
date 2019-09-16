<?php include 'header.php';?>
<div class="container event-container">
    <div class="row">
    <!--Top Row-->
        <div class="col-sm-9 card">
            <div class="card-body">
                <h1>Rochester Middle School</h1>
                <hr>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-envelope" aria-hidden="true"></i> admin@rms.org</h5>
                    </div>
                    <div class="col-sm-6">
                        <button type="button" class="btn btn-link">Change Password</button>
                    </div>
                </div>
                <div class="row twentyblock"></div>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-globe" aria-hidden="true"></i> rocmiddleschool.org</h5>
                    </div>
                    <div class="col-sm-6">
                         <button type="button" class="btn btn-link">Change URL</button>
                    </div>
                </div>
                <div class="row twentyblock"></div>
                <div class="row">
                    <div class="col-sm-6">
                         <h5 class="provider-info"><i class="fa fa-id-card" aria-hidden="true"></i> Rochester Middle School</h5>
                    </div>
                    <div class="col-sm-6">
                         <button type="button" class="btn btn-link">Change Name</button>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-sm-3">
            <div class="card event-page-card">
              <img src="https://via.placeholder.com/150" class="card-img-top" alt="Provider Logo">
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
    <div class="row">
    <!-- Bottom Row -->
        <h2 class="program-header w-100">Events and Programs<button type="button" class="btn btn-success float-right"> <i class="fa fa-plus" aria-hidden="true"></i> Add New Event</button></h2>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Program Name</th>
              <th scope="col">Status</th>
              <th scope="col" class="list-header-fix">Edit</th>
              <th scope="col" class="list-header-fix">Delete</th>
            </tr>
          </thead>
          <tbody class="provider-program-list">
            <tr>
              <th scope="row">Soccer Program</th>
              <td>Approved</td>
              <td><button type="button" class="btn btn-info">Edit</button></td>
              <td><button type="button" class="btn btn-danger">Delete</button></td>
            </tr>
            <tr class="warning">
              <th scope="row">Cooking Program</th>
              <td>Submitted for Approval</td>
              <td><button type="button" class="btn btn-info disabled">Edit</button></td>
              <td><button type="button" class="btn btn-danger disabled">Delete</button></td>
            </tr>
          </tbody>
        </table>
    
    </div>
</div>

<?php include 'footer.php';?>