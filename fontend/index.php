<?php include 'header.php';?>
<!-- Homepage, wireframe #5 -->
<div class="container home-container">
    <div class="row">
    <!-- most outer row-->
        <div class="col-3">
        <!--left sidebar-->
            <div class="row">
            <!-- Search by Program Row -->
                <label><b>Search Program</b></label>
                <div class="input-group mb-3">
                  <input type="text" class="form-control" placeholder="Search..." aria-label="Search for a Program by name" aria-describedby="button-addon2">
                  <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" id="button-addon2"><i class="fa fa-search" aria-hidden="true"></i></button>
                  </div>
                </div>
            </div>
            <div class="row">
            <!-- Search by City, State and Zip Row -->
                <label><b>City & State or Zip Code</b></label>
                <div class="input-group mb-3">
                  <input type="text" class="form-control" placeholder="Search..." aria-label="Search for a Program by Zip code" aria-describedby="button-addon2">
                  <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" id="button-addon2"><i class="fa fa-search" aria-hidden="true"></i></button>
                  </div>
                </div>
            </div>
            <div class="row">
            <!-- Category Row -->
                <div class="card" style="width:100%">
                    <header class="card-header">Filter Programs</header>
                        <div class="list-group list-group-flush">
                          <label class="form-check list-group-item">
                              <input type="checkbox" value="">
                              <span class="form-check-label">
                                Sports
                              </span>
                            </label> <!-- form-check.// -->
                           <label class="form-check list-group-item">
                              <input type="checkbox" value="">
                              <span class="form-check-label">
                                Theatre
                              </span>
                            </label> <!-- form-check.// -->
                           <label class="form-check list-group-item">
                              <input type="checkbox" value="">
                              <span class="form-check-label">
                                Art
                              </span>
                            </label> <!-- form-check.// -->
                           <label class="form-check list-group-item">
                              <input type="checkbox" value="">
                              <span class="form-check-label">
                               Robotics
                              </span>
                            </label> <!-- form-check.// -->
                        </div>  <!-- list-group .// -->
                </div>
            </div>
        </div>
        <div class="col-9">
        <!--Right Content-->
            <div class="card program-list-card">
              <div class="card-header">
                Programs
              </div>
              <div class="card-body">
                <!--Example Event-->
                  <div class="card event-card">
                      <div class="card-body">
                        <h5 class="card-title">Soccer Program</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Rochester Middle School</h6>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel risus tortor. Maecenas posuere bibendum aliquet. Nulla eget maximus velit. Praesent sed laoreet nisl. Fusce fringilla eros quis risus ornare, a posuere velit dictum. Nunc ac luctus orci, vitae mollis massa.  </p>
                        <a href="#" class="card-link">www.rocmiddleschool.com</a>
                        <a href="#" class="card-link">Another link</a>
                        <i class="event-icon fa fa-futbol-o" aria-hidden="true"></i>
                      </div>
                    </div>
                <!--Example Event-->
                  <div class="card event-card">
                      <div class="card-body">
                        <h5 class="card-title">Art Program</h5>
                        <h6 class="card-subtitle mb-2 text-muted">Henrietta High School</h6>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vel risus tortor. Maecenas posuere bibendum aliquet. Nulla eget maximus velit. Praesent sed laoreet nisl. Fusce fringilla eros quis risus ornare, a posuere velit dictum. Nunc ac luctus orci, vitae mollis massa.  </p>
                        <a href="#" class="card-link">www.henhighschool.com</a>
                        <a href="#" class="card-link">Another link</a>
                        <i class="event-icon fa fa-paint-brush
" aria-hidden="true"></i>
                      </div>
                    </div>
                  
                  
                  
              </div>
            </div>
        </div>
    </div>
    <div class="row">
    <!-- map row-->
            <iframe id="gmap_canvas" src="https://maps.google.com/maps?q=Rochester%20Institute%20of%20Technology%20&t=&z=9&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>
    </div>
</div>

<?php include 'footer.php';?>
