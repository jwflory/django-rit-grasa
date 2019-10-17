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
                  <th scope="row">Put Name Here</th>
                  <th scope="row">time</th>
                  <td><button type="button" class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteModal">Delete</button></td>
                </tr>

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
                    <form action="" method="post">
                      <div class="modal-body">


                            <label for="resetPW" class="top-20">Email address</label>
                            <input type="email" id="resetPW" class="form-control" name="emailAddr" required autofocus>

                            <label for="myPW" class="top-20">Password</label>
                            <input type="password" id="myPW" class="form-control" name="current" pattern="(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}" title="Must contain at least one number and one uppercase and lowercase letter, and at least 8 or more characters" required>

                            <label for="confirmPW" class="top-20">Confirm Password</label>
                            <input type="password" id="confirmPW" class="form-control" name="confirm" required>
                            <input id="SPcheckbox" type="checkbox" onclick="myFunction()">
                            <label for="SPcheckbox">&nbsp; Show Password</label>



                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-danger" data-dismiss="modal">Cancel</button>
                        <button type="button" class="btn btn-success" type="submit" value="Submit">Create Admin</button>
                      </div>
                    </form>
                    </div>
                  </div>
                </div>

              </tbody>
            </table>
    </div>
</div>


<script>
    var backBtn = document.getElementById('backBtn');
    backBtn.onclick = function(){
        window.location = 'admin.php'
    }

</script>
{% include "footer.php" %}
