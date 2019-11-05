{% include "header.php" %}
<div class="container event-container">
    <div class="row">

        <div class="col-sm-8">
            <h1>{{ event.title }}</h1>
            <h4 class="text-muted">{{ event.user_id.org_name }}</h4>
            <div class="activity-badges">
            {% for f in topic_list %}
                <span class="badge badge-info card-title">{{ f }}</span>
            {% endfor %}
            </div>
            <p class="text-break">{{ event.content }}</p>
            <p><b>Grades: </b> {{ grades_list_pub }} </p>
            <p><b>Timing: </b> {{ timing_list_pub }}</p>
            <p><b>Gender: </b> {{ gender_list_pub }}</p>
            <p><b>Transportation: </b> {{ transportation_list_pub}}</p>
            <p><b>Contact Information: </b> <br><i class="fa fa-user fa-fw" aria-hidden="true"></i> {{ event.contact_name }} <br><i class="fa fa-envelope fa-fw" aria-hidden="true"></i> {{ event.contact_email }} <br><i class="fa fa-phone fa-fw" aria-hidden="true"></i> {{ event.contact_phone }}</p>


        </div>
        <div class="col-sm-4">
            <div class="card event-page-card">
              <img src="https://via.placeholder.com/150" class="card-img-top" alt="Provider Logo">
              <ul class="list-group list-group-flush">
                {% if event.fees %}
                <li class="list-group-item"><i class="fa fa-money fa-fw" aria-hidden="true"></i> ${{ fees }}</li>
                {% else %}
                <li class="list-group-item"><i class="fa fa-money fa-fw" aria-hidden="true"></i> Not Provided </li>
                {% endif %}
                {% if event.address %}
                <a target="_blank" href="https://maps.google.com/?q={{ event.address }}"><li class="list-group-item"><i class="fa fa-map-marker fa-fw" aria-hidden="true"></i>{{ event.address }}</li></a>
                {% else %}
                <a><li class="list-group-item"><i class="fa fa-map-marker fa-fw" aria-hidden="true"></i>Not Provided</li></a>
                {% endif %}
              </ul>
              <div class="card-body">
              {% if event.website %}
                 <a target="_blank" href="{{ event.website }}" class="card-link"><i class="fa fa-globe fa-fw" aria-hidden="true"></i> {{ event.website }}</a>
              {% else %}
                <div class="card-link"><i class="fa fa-globe fa-fw" aria-hidden="true"></i> Not Provided
              {% endif %}
              </div>
            </div>
        </div>

    </div>
</div>
</div>

{% include "footer.php" %}
