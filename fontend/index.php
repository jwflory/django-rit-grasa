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
            <iframe title="Map" id="gmap_canvas" src="https://maps.google.com/maps?q=Rochester%20Institute%20of%20Technology%20&t=&z=9&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" aria-hidden="true"></iframe>
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
    
    //Filter Buttons
    var clearBtn = document.getElementById('clearFilters');
    clearBtn.onclick= function(){
        var items = $(".accordion [type='checkbox']")
        for (var i = 0; i < items.length; i++) {
            if (items[i].type == 'checkbox')
                items[i].checked = false;
        }
        console.log("Filters Cleared")
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
   

    
</script>
<?php include 'footer.php';?>











