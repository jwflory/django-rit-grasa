{% include "header.php" %}
<div class="row allUsersContainer">
    <div class="col-sm-12">
        <div class="twentyblock"></div>
        <h2 class="text-center">All Events</h2>
        <button type="button" class="btn btn-info float-left" style="margin-bottom: 10px;" id="backBtn"> <i class="fa fa-chevron-left" aria-hidden="true" ></i> Back to Admin Portal</button>
        
        
        <table class="table table-bordered">
              <thead class="thead-light">
                <tr>
                  <th scope="col">Name</th>
                  <th scope="col">Organization</th>
                  <th scope="col">Created By</th>
                  <th scope="col" class="list-header-fix">View</th>
                  <th scope="col" class="list-header-fix">Delete</th>
                </tr>
              </thead>
              <tbody class="provider-program-list">
                {% for p in programList %}
                <tr>
                  <td>{{ p.title }}</td>
                  <td>{{ p.user_id.org_name }}</td>
                  <td>{{ p.user_id.user.username }}</td>
                  <td><button type="button" class="btn btn-outline-info" onclick="window.location.href='{% url 'event_page' p.id %}'">View</button></td>
                  <td><button type="button" class="btn btn-outline-danger" data-toggle="modal" data-target="#deleteModal{{ p.id }}">Delete</button></td>
                </tr>

                <!--Delete Modal-->
                <div class="modal fade" id="deleteModal{{ p.id }}" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                  <div class="modal-dialog" role="document">
                    <div class="modal-content">
                      <div class="modal-header">
                        <h5 class="modal-title" id="exampleModalLabel">Are You Sure?</h5>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                          <span aria-hidden="true">&times;</span>
                        </button>
                      </div>
                      <div class="modal-body">
                       Are you sure you want to delete this Event? This cannot be undone.
                      </div>
                      <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Never Mind</button>
                        <button type="button" class="btn btn-danger" data-dismiss="modal" onclick="window.location.href='{% url 'deny_event' p.id %}'">Confirm Delete</button>

                      </div>
                    </div>
                  </div>
                </div>
                
                {% endfor %}
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
