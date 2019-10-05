{% include "header.php" %}
<!-- Homepage -->
<div class="container home-container">
    <div class="row">
    <!-- most outer row-->
        <div class="col-sm-3 filter-col">
        <!-- Filter column-->
            <div class="accordion" id="accordionExample">
                <!--data filled with JS-->
            </div>
            <div class="row filter-btn-row">
            <!-- button row-->
                <div class="col-12">
                    <div class="filter-alert alert alert-danger alert-dismissible fade show" role="alert">
                      Filters Cleared
                    </div>
                </div>
                <div class="btn-group col-12" role="group" aria-label="Basic example">
                  <button type="button" class="btn btn-secondary btn-outline-success">Apply Filters</button>
                  <button type="button" class="btn btn-secondary btn-outline-danger" id="clearFilters">Clear Filters</button>
                </div>

            </div>
        </div>
        <div class="col-sm-9">
        <!-- search results column-->
            <div class="row">
            <!-- search bar row-->
                <div class="input-group mb-3 search-bar">
                  <input type="text" class="form-control" placeholder="Search..." aria-label="Search for a Program by name" aria-describedby="button-addon2">
                  <div class="input-group-append">
                    <button class="btn btn-outline-secondary" type="button" id="button-addon2" aria-label="Search"><i class="fa fa-search" aria-hidden="true"></i></button>
                  </div>
                </div>
            </div>
            <div class="row">
            <!-- Search Results Row-->
                <div id="results-box">
            {% for event in allEventList %}
                    <a href="{% url 'event_page' event.id %}"> <div class="card w-100 event-box">
                      <div class="card-body row">
                        <div class="col-sm-6">
                            <h5 class="card-title">{{ event.title }}</h5>
                            <h6 class="card-subtitle mb-2 text-muted">{{ event.user_id.org_name }}</h6>
                        </div>
                        <div class="col-sm-6 right-info">
                                {% for t in event.categories.all %}
                                <span class="badge badge-info card-title">
                                {{ t }}
                                </span>
                                {% endfor %}
                            <h6 class="card-subtitle mb-2 text-muted"><i class="fa fa-map-marker" aria-hidden="true"></i> {{ event.address }}</h6>
                        </div>
                      </div>
                    </div>
                    <a>
                    {% endfor %}
                </div>
            </div>
        </div>
    </div>
    <div class="row">
    <!-- map row-->
        <div id="mapid"></div>


    </div>
</div>
<!--Leaflet JS-->
<script src="https://unpkg.com/leaflet@1.5.1/dist/leaflet.js"
   integrity="sha512-GffPMF3RvMeYyc1LWMHtK8EbPv0iNZ8/oTtHPx9/cc2ILxQ+u905qIwdpULaqDkyBKgOaB57QTMg7ztg8Jm2Og=="
   crossorigin=""></script>

<!--Custom page JS-->
<script>
    //Clicking on an event opens the event page
    $('.event-box').hover(
       function(){ $(this).addClass('border-info') },
       function(){ $(this).removeClass('border-info') }
    ).click(function() {
      window.location = "index.php"
    });

    //Filter Buttons
    var clearBtn = document.getElementById('clearFilters');
    clearBtn.onclick= function(){
        var items = $(".accordion [type='checkbox']")
        for (var i = 0; i < items.length; i++) {
            if (items[i].type == 'checkbox')
                items[i].checked = false;
        }
        //show and hide alert for clear filters
        $(".filter-alert").show()
        setTimeout(function() {
            $(".filter-alert").hide();
        }, 2000);

    }

    $( document ).ready(function() {
        //Categories
        for(var i=0; i<groupList.length; i++){

            //check for group name with spaces
            var words = groupList[i].split(" ")
            if(words.length > 1){
               var name = words[0]
            }else{
                var name = groupList[i]
            }

            //uncollapse first filter box
            if(i==0){
                $(".accordion").append("<div class='card'><div class='card-header' id='heading"+name+"'><h2 class='mb-0'><button class='btn btn-link' type='button' data-toggle='collapse' data-target='#collapse"+name+"' aria-expanded='true' aria controls='collapse"+name+"'>"+groupList[i]+"</button></h2></div><div id='collapse"+name+"' class='collapse show' data-parent='#accordionExample'><div class='card-body'></div></div></div>")

            //add distance
            }else if(name=="Distance"){
                $(".accordion").append("<div class='card'><div class='card-header' id='heading"+name+"'><h2 class='mb-0'><button class='btn btn-link collapsed' type='button' data-toggle='collapse' data-target='#collapse"+name+"' aria-expanded='true' aria controls='collapse"+name+"'>"+groupList[i]+"</button></h2></div><div id='collapse"+name+"' class='collapse' data-parent='#accordionExample'><div class='card-body'><input class='form-control form-control-sm distance-input' type='text' placeholder='From Address...'></div></div></div>")
            }else{
                $(".accordion").append("<div class='card'><div class='card-header' id='heading"+name+"'><h2 class='mb-0'><button class='btn btn-link collapsed' type='button' data-toggle='collapse' data-target='#collapse"+name+"' aria-expanded='true' aria controls='collapse"+name+"'>"+groupList[i]+"</button></h2></div><div id='collapse"+name+"' class='collapse' data-parent='#accordionExample'><div class='card-body'></div></div></div>")
            }

        }

        //Activity
        fillCheckBoxes(activityList, "collapseActivity");

        //Transportation
        fillCheckBoxes(transportationList, "collapseTransportation");

        //Grades Served
        fillCheckBoxes(gradesList, "collapseGrades");

        //Gender
        fillCheckBoxes(genderList, "collapseGender");

        //Distance
        fillCheckBoxes(distanceList, "collapseDistance");

        //Fees
        fillCheckBoxes(feesList, "collapseFees");

        //Timing
        fillCheckBoxes(timingList, "collapseTiming");


    });

    function fillCheckBoxes(list, location){
        for(var i=0; i<list.length; i++){
            var words = list[i].split(" ")
            if(words.length > 1){
               var name = words[0]
            }else{
                var name = list[i]
            }
            $( "#"+location+" .card-body" ).append( "<div class='form-check'><input class='form-check-input' type='checkbox' value='' id='defaultCheck"+name+i+"'><label class='form-check-label' for='defaultCheck"+name+i+"'>"+list[i]+"</label></div>" );
        }
    }

    //Leaflet Code
    //init
    var mymap = L.map('mapid').setView([43.0846, -77.6743], 13);
    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: 'sk.eyJ1IjoibGRpZG9uYXRvIiwiYSI6ImNrMTdzdmN4YTFqODgzbnBrOHB4ZzJ1dzQifQ.T7D-X5eab-y3J-KIu_WTBw'
    }).addTo(mymap);

    //markers
    //testing colors https://github.com/pointhi/leaflet-color-markers
    var greenIcon = new L.Icon({
      iconUrl: 'https://cdn.rawgit.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      shadowSize: [41, 41]
    });

    var marker = L.marker([43.0846, -77.6743]).addTo(mymap);
    marker.bindPopup("<div class='leafeventPopup'><b>Soccer Program</b><br>Rochester Middle School<br><a href='event.php'>Details</a></div>").openPopup();


    var marker2 = L.marker([43.0966, -77.6973], {icon: greenIcon}).addTo(mymap);
    marker2.bindPopup("<b>Cooking for Kids</b><br>Henrietta Elementary School<br><a href='event.php'>Details</a></div>");


</script>
{% include "footer.php" %}










