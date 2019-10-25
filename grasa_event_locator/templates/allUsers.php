{% include "header.php" %}
<div class="row allUsersContainer">
    <div class="col-sm-12">
        <div class="twentyblock"></div>
        <h2 class="text-center">All Providers</h2>
        <button type="button" class="btn btn-info float-left" style="margin-bottom: 10px;" id="backBtn"> <i class="fa fa-chevron-left" aria-hidden="true" ></i> Back to Admin Portal</button>
        <button type="button" class="btn btn-primary float-right" id="addAdmin" data-toggle="modal" data-target="#inviteModal"><i class="fa fa-paper-plane" aria-hidden="true"></i> Invite Provider</button>
        <table class="table table-bordered">
              <thead class="thead-light">
                <tr>
                  <th scope="col">Organization Name</th>
                  <th scope="col">Email</th>
                  <th scope="col">Alternative Contact</th>
                  <th scope="col">Number of Events</th>
                  <th scope="col" class="list-header-fix">Delete</th>
                </tr>
              </thead>
              <tbody class="provider-program-list">
                {% for user in userList %}
                <tr>
                  <th scope="row">{{ user.org_name }}</th>

                  <td><a href="mailto:{{ user.user }}">{{ user.user }}</a></td>
                  <td> 
                      <i class="fa fa-user fa-fw" aria-hidden="true"></i> {{         user.contact_name }}<br>
                      <i class="fa fa-envelope fa-fw" aria-hidden="true"></i> <a href="mailto:{{ pendingUser.contact_email }}">{{ user.contact_email }}</a><br>
                      <i class="fa fa-phone fa-fw" aria-hidden="true"></i> {{ user.contact_phone }}
                    
                    </td>

                  <td> TBD </td>
                  <!--Set target to correct modal so it deletes the correct user-->
                  <td><button type="button" class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteModal{{ user.id }}">Delete</button></td>
                </tr>
                <!--Delete Modal-->
                <!--Set delete modal to have an ID equivalent to it's row so it deletes the correct user-->
                <div class="modal fade" id="deleteModal{{ user.id }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Are You Sure?</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                       Are you sure you want to delete this user? This cannot be undone.<br><br><b>THIS WILL REMOVE ALL EVENTS ASSOCIATED WITH THE USER</b>.
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Never Mind</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal" onclick="window.location.href='{% url 'deny_user' user.id %}'">Confirm Delete</button>

                      </div>
                    </div>
                  </div>
                </div>

                {% endfor %}
              </tbody>
            </table>
    </div>
</div>
<!-- Invite Modal -->
<div class="modal fade" id="inviteModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Invite Provider</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
          <form>
      <div class="form-group">
        <label for="exampleInputEmail1">Send an email to an organization you would like to invite as a provider:</label>
        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter Email...">
      </div>
              <div class="twentyblock"></div>
       <button type="submit" class="btn btn-primary w-100">Send Invite</button>
    </form>
      </div>
    </div>
  </div>
</div>

<script>
    var backBtn = document.getElementById('backBtn');
    backBtn.onclick = function(){
        window.location = 'admin.php'
    }

</script>
{% include "footer.php" %}
