<?php include 'header.php';?>
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
                <div class="btn-group col-12" role="group" aria-label="Basic example">
                  <button type="button" class="btn btn-secondary btn-outline-success">Apply Filters</button>
                  <button type="button" class="btn btn-secondary btn-outline-danger">Clear Filters</button>
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
                    <button class="btn btn-outline-secondary" type="button" id="button-addon2"><i class="fa fa-search" aria-hidden="true"></i></button>
                  </div>
                </div>
            </div>
            <div class="row">
            <!-- Search Results Row-->
                <div id="results-box">
                    <div class="card w-100 event-box">
                      <div class="card-body row">
                        <div class="col-sm-6">
                            <h5 class="card-title">Soccer Program</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Rochester Middle School</h6>
                        </div>
                        <div class="col-sm-6 right-info">
                                <span class="badge badge-info card-title">Play</span>
                                <span class="badge badge-info card-title">Sports and Recreation</span>
                            <h6 class="card-subtitle mb-2 text-muted"><i class="fa fa-map-marker" aria-hidden="true"></i> 1 Lomb Memorial Dr, Rochester NY</h6>
                        </div>                      
                      </div>
                    </div>

                    <div class="card w-100 event-box">
                      <div class="card-body row">
                        <div class="col-sm-6">
                            <h5 class="card-title">Cooking for Kids</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Henrietta Elementary School</h6>
                        </div>
                        <div class="col-sm-6 right-info">
                                <span class="badge badge-info card-title">Health &amp; Wellness</span>
                                <span class="badge badge-info card-title">Arts and Culture</span>
                            <h6 class="card-subtitle mb-2 text-muted"><i class="fa fa-map-marker" aria-hidden="true"></i> 14 The Random Rd, Henrietta NY</h6>
                        </div>                      
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
<script>
    //Clicking on an event opens the event page
    $('.event-box').hover(
       function(){ $(this).addClass('border-info') },
       function(){ $(this).removeClass('border-info') }
    ).click(function() {
      window.location = "event.php"
    });
    
    
    $( document ).ready(function() {
        
        //Categories
        var groupList = ["Activity", "Transportation", "Grades Served", "Gender","Distance", "Fees", "Timing"]
        
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
                $(".accordion").append("<div class='card'><div class='card-header' id='heading"+name+"'><h2 class='mb-0'><button class='btn btn-link' type='button' data-toggle='collapse' data-target='#collapse"+name+"' aria-expanded='true' aria controls='collapse"+name+"'>"+groupList[i]+"</button></h2></div><div id='collapse"+name+"' class='collapse show' aria-labelledby='headingOne' data-parent='#accordionExample'><div class='card-body'></div></div></div>")
            
            //add distance
            }else if(name=="Distance"){
                $(".accordion").append("<div class='card'><div class='card-header' id='heading"+name+"'><h2 class='mb-0'><button class='btn btn-link collapsed' type='button' data-toggle='collapse' data-target='#collapse"+name+"' aria-expanded='true' aria controls='collapse"+name+"'>"+groupList[i]+"</button></h2></div><div id='collapse"+name+"' class='collapse' aria-labelledby='headingOne' data-parent='#accordionExample'><div class='card-body'><input class='form-control form-control-sm distance-input' type='text' placeholder='From Address...'></div></div></div>")
            }else{
                $(".accordion").append("<div class='card'><div class='card-header' id='heading"+name+"'><h2 class='mb-0'><button class='btn btn-link collapsed' type='button' data-toggle='collapse' data-target='#collapse"+name+"' aria-expanded='true' aria controls='collapse"+name+"'>"+groupList[i]+"</button></h2></div><div id='collapse"+name+"' class='collapse' aria-labelledby='headingOne' data-parent='#accordionExample'><div class='card-body'></div></div></div>")
            }
            
        }
        
        //Activity
        var activityList = ["Academic Support", "Arts and Culture", "Career or College Readiness", "Civic Engagement", "Community Service/ Service Learning", "Entrepreneurship/ Leadership", "Financial Literacy", "Health & Wellness", "Media Technology",  "Mentoring", "Nature & the Environment", "Play", "Public Speaking", "Social and Emotional Learning (SEL)", "Sports and Recreation", "STEM", "Tutoring", "Other"]
        fillCheckBoxes(activityList, "collapseActivity");
        
        //Transportation
        var transportationList = ["Provided", "Not Provided"]
        fillCheckBoxes(transportationList, "collapseTransportation");
        
        //Grades Served
        var gradesList = ["K-3rd", "K-5th", "3rd-5th", "6th-8th", "9th-12th"]
        fillCheckBoxes(gradesList, "collapseGrades");
        
        //Gender
        var genderList = ["Male Only", "Female Only", "Non-Specific"]
        fillCheckBoxes(genderList, "collapseGender");
        
        //Distance
        var distanceList = ["0-5 miles", "6-10 miles", "11-15 miles", "16-20 miles", "20+ miles"]
        fillCheckBoxes(distanceList, "collapseDistance");
        
        //Fees
        var feesList = ["Free", "$1-$25", "$26-$50", "$51-$75", "$75+"]
        fillCheckBoxes(feesList, "collapseFees");
        
        //Timing
        var timingList = ["Before School", "After School", "Evenings", "Weekends", "Summer", "Other"]
        fillCheckBoxes(timingList, "collapseTiming");
        
         
    });
    
    function fillCheckBoxes(list, location){
        for(var i=0; i<list.length; i++){
            $( "#"+location+" .card-body" ).append( "<div class='form-check'><input class='form-check-input' type='checkbox' value='' id='defaultCheckGender"+i+"'><label class='form-check-label' for='defaultCheckGender"+i+"'>"+list[i]+"</label></div>" );
        }
    }
   

    
</script>
<?php include 'footer.php';?>











