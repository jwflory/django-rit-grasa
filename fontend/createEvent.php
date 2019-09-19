<?php include 'header.php';?>
<div class="container event-container">
    <div class="row">
        <div class="col-12">
            <button type="button" class="btn btn-danger float-right" data-toggle="modal" data-target="#cancelModal">Cancel</button>
        </div>
        <div class="modal fade" id="cancelModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Confirmation</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                Are you sure you want to cancel? The information for your new event will not be saved.
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Nevermind</button>
                <button type="button" class="btn btn-primary" id="cancelBtn">Confirm Cancel</button>
              </div>
            </div>
          </div>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-8">
            <div class="form-group">
                <label>Program Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Name...">
            </div>
            <div class="form-group">
                <label>Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="8" placeholder="Tell us about your program..."></textarea>
            </div>
            <div class="form-group">
                <label>Location</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Street Address...">
            </div>    

            <div class="form-group">
                <label>Website (optional)</label>
                <input type="url" class="form-control" id="exampleFormControlInput1" placeholder="http://">
            </div>  
        </div>
        <div class="col-sm-4">
            <div class="form-group text-left multiBox">
                <label>Activity</label><br>
                <select class="custom-select w-100 activitySelect" id="basic" multiple="multiple">
                </select>
            </div> 
            <div class="form-group">
                <label>Transportation</label>
                <select class="form-control">
                    <option>Not Provided</option>
                    <option>Provided</option>
                </select>
            </div> 
            <div class="form-group text-left multiBox">
                <label>Grades Served</label><br>
                <select class="custom-select w-100 gradesSelect" id="basic" multiple="multiple">
                </select>
            </div> 
            <div class="form-group">
                <label>Gender</label>
                <select class="form-control">
                    <option>Not Specific</option>
                    <option>Female</option>
                    <option>Male</option>
                </select>
            </div>
            <div class="form-group">
                <label>Fees</label>
                <div class="input-group mb-3">
                  <div class="input-group-prepend">
                    <span class="input-group-text">$</span>
                  </div>
                  <input type="number" class="form-control" aria-label="Amount (to the nearest dollar)" placeholder="0.00">
                </div>
            </div>
            <div class="form-group text-left multiBox">
                <label>Timing</label><br>
                <select class="custom-select w-100 timingSelect" id="basic" multiple="multiple">
                </select>
            </div> 
            
                
        </div>
    </div>
    <div class="row float-right">
        <div class="col-12">
            <button type="button" class="btn btn-success"><i class="fa fa-check" aria-hidden="true"></i> Submit for Approval</button>
        </div>
    </div>
</div>
<script>
    
    //Cancel Button returns to provider page
    var cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.onclick = function(){
        window.location = 'provider.php'
    }
    
    //fill checkbox selects
    fillCheckboxSelects(activityList,"activitySelect");
    fillCheckboxSelects(gradesList,"gradesSelect");
    fillCheckboxSelects(timingList,"timingSelect");
    
    //Use 3rd party code to make checkbox select
    $('.custom-select').multiselect({
        templates: {
            li: '<li><a href="javascript:void(0);"><label class="pl-2"></label></a></li>'
        }
    });
    $(".multiselect-container").addClass('w-100');
    $(".multiBox .btn-group").addClass('w-100');
    
    
    //fill helper function
    function fillCheckboxSelects(list, location){
        for(var i=0; i<list.length; i++){
            //check for name with spaces
            var words = list[i].split(" ")
            if(words.length > 1){
                //value names cannot have a slash in it or it won't show up
               var name = words[0].replace(/^\/|\/$/g, '')
               console.log(name);
            }else{
                var name = list[i]
            }
            $( "."+location).append( "<option value="+name+">"+list[i]+"</option>" );
        }
    }

</script>
<?php include 'footer.php';?>