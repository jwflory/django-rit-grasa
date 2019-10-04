{% include "header.php" %}
<div class="container event-container">
    <div class="row">
        
        <div class="col-sm-8">
            <h1>{{ event.title }}</h1>
            <h4 class="text-muted">{{ event.user_id.org_name }}</h4>
            <div class="activity-badges">
                <span class="badge badge-info card-title">Play</span>
                <span class="badge badge-info card-title">Sports and Recreation</span>
            </div>
            <p>{{ event.content }}</p>
            <p><b>Grades: </b> 3rd-5th, 6th-8th</p>
            <p><b>Timing: </b> After School, Summer</p>
            <p><b>Gender: </b> Non-Specific</p>
            <p><b>Transportation: </b> Not Provided</p>


        </div>
        <div class="col-sm-4">
            <div class="card event-page-card">
              <img src="https://via.placeholder.com/150" class="card-img-top" alt="Provider Logo">
              <ul class="list-group list-group-flush">
                <li class="list-group-item"><i class="fa fa-money" aria-hidden="true"></i> $20.00</li>
                <li class="list-group-item"><i class="fa fa-map-marker" aria-hidden="true"></i> 1 Lomb Memorial Dr, Rochester NY</li>
              </ul>
              <div class="card-body">
                <a href="#" class="card-link"><i class="fa fa-globe" aria-hidden="true"></i> "Event's Website"</a>
              </div>
            </div>
        </div>
        
    </div>
</div>

{% include "footer.php" %}