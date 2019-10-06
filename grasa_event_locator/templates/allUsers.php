{% include "header.php" %}
<div class="row allUsersContainer">
    <div class="col-sm-12">
        <div class="twentyblock"></div>
        <h2 class="text-center">All Users</h2>
        <button type="button" class="btn btn-info float-left" style="margin-bottom: 10px;" id="backBtn"> <i class="fa fa-chevron-left" aria-hidden="true" ></i> Back to Admin</button>
        <table class="table table-hover table-bordered">
              <thead class="thead-light">
                <tr>
                  <th scope="col">Organization Name</th>
                  <th scope="col">Email</th>
                  <th scope="col">Number of Events</th>
                  <th scope="col" class="list-header-fix">Delete</th>
                </tr>
              </thead>
              <tbody class="provider-program-list">
                {% for user in userList %}
                <tr>
                  <th scope="row">{{ user.org_name }}</th>
                  <td><a href="mailto:{{ user.user }}">{{ user.user }}</a></td>

                  <td> TBD </td>
                  <td><button type="button" class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteModal">Delete</button></td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
    </div>
</div>

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
               Are you sure you want to delete this user? This cannot be undone.<br><br><b>THIS WILL REMOVE ALL EVENTS ASSOCIATED WITH THE USER</b>.
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Nevermind</button>
                <button type="button" class="btn btn-danger" data-dismiss="modal">Confirm Delete</button>

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
