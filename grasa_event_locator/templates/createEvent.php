<?php include 'header.php';?>
<div class="container event-container">
    <h2>Create Event</h2>
    <div class="row">
        <div class="col-12">
            <button type="button" class="btn btn-danger float-right" data-toggle="modal" data-target="#cancelModal">Cancel</button>
        </div>
        <!--Cancel Modal-->
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
                <button type="button" class="btn btn-secondary" data-dismiss="modal"> Nevermind</button>
                <button type="button" class="btn btn-primary" id="cancelBtn">Confirm Cancel</button>
                
              </div>
            </div>
          </div>
        </div>
        
        <!--Submit Modal-->
        <div class="modal fade" id="submitModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">Submitted</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
               Your event has been submitted to the administrators for approval. Until it is approved, your event will not appear in search results.
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-success" id="submitOkBtn">OK</button>
                
              </div>
            </div>
          </div>
        </div>
        
    </div>
    
    <form class="needs-validation" novalidate>
      <div class="form-row">
            <div class="col-sm-8">
                <div class="form-group">
                    <label>Program Name</label>
                    <input type="text" class="form-control" placeholder="Name..." required>
                    <div class="invalid-feedback">
                        Please provide a name for your program.
                    </div>
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="8" placeholder="Tell us about your program..." required></textarea>
                    <div class="invalid-feedback">
                        Please provide a description for your program.
                    </div>
                </div>
                <div class="form-group">
                    <label>Location</label>
                    <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Street Address..." required>
                    <div class="invalid-feedback">
                        Please provide your program's street address.
                    </div>
                </div>    
                <div class="form-group">
                    <label>Website (optional)</label>
                    <input type="url" class="form-control" id="exampleFormControlInput1" placeholder="http://">
                </div>  
            </div>
            <div class="col-sm-4">
                <div class="form-group text-left multiBox">
                    <label>Activity</label><br>
                    <select class="form-control custom-select w-100 activitySelect" id="basic" multiple="multiple" required>
                    </select>
                    <div class="invalid-feedback">
                        Please select at least one activity.
                    </div>
                </div> 
                <div class="form-group">
                    <label>Transportation</label>
                    <select class="form-control" required>
                        <option>Not Provided</option>
                        <option>Provided</option>
                    </select>
                </div> 
                <div class="form-group text-left multiBox">
                    <label>Grades Served</label><br>
                    <select class="custom-select w-100 gradesSelect" id="basic" multiple="multiple" required>
                    </select>
                    <div class="invalid-feedback">
                        Please select at least one grade group.
                    </div>
                </div> 
                <div class="form-group">
                    <label>Gender</label>
                    <select class="form-control" required>
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
                      <input type="number" class="form-control" aria-label="Amount (to the nearest dollar)" placeholder="0.00" required>
                        <div class="invalid-feedback">
                            Please enter total amount of fees. If the program is free enter 0.00
                        </div>
                    </div>
                    
                </div>
                <div class="form-group text-left multiBox">
                    <label>Timing</label><br>
                    <select class="custom-select w-100 timingSelect" id="basic" multiple="multiple" required>
                    </select>
                     <div class="invalid-feedback">
                        Please select at least one time.
                    </div>
                </div> 


            </div>
        </div>
        
      <button class="btn btn-success float-right" type="submit"><i class="fa fa-check" aria-hidden="true"></i> Submit for Approval</button>
    </form>
    
    
</div>
<script>
    
    //Cancel Button and Ok Button returns to provider page
    var cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.onclick = function(){
        window.location = 'provider.php'
    }
    var cancelBtn = document.getElementById('submitOkBtn');
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
            }else{
                var name = list[i]
            }
            $( "."+location).append( "<option value="+name+">"+list[i]+"</option>" );
        }
    }
    
    //Validation
    (function() {
      'use strict';
      window.addEventListener('load', function() {
        // Fetch all the forms we want to apply custom Bootstrap validation styles to
        var forms = document.getElementsByClassName('needs-validation');
        // Loop over them and prevent submission
        var validation = Array.prototype.filter.call(forms, function(form) {
          form.addEventListener('submit', function(event) {
            if (form.checkValidity() === false) {
              event.preventDefault();
              event.stopPropagation();
            }else{
                //IF CLIENT SIDE VALIDATION WORKS YOU END UP HERE
                event.preventDefault();     //this stops the form from submitting, DELETE later
                $('#submitModal').modal('show');
            }
            form.classList.add('was-validated');
              
            //validation style fix for multiselect
            var multiList = document.getElementsByClassName("multiBox");
            for(var i=0; i<multiList.length;i++){
                var message = $(multiList[i]).find(".invalid-feedback")[0]
                var button = $(multiList[i]).find(".btn-group").find(".multiselect")[0]
                if($(message).css('display') == 'block'){
                    $(button).css('border', 'solid 1px #dc3545')
                }else{
                    $(button).css('border', 'solid 1px #28a745')
                    $(button).find("i").remove();
                    $(button).append('<i class="fa fa-check" aria-hidden="true" style="color:#28a745;padding-top:5px;padding-right:5px;"></i>')
                }
                var liList = $(multiList[i]).find("li")
                for(var x=0; x<liList.length;x++){
                    var checkbox = $(liList[x]).find("input")[0]
                    $(checkbox).change(function() {
                        var parentBtn = $(this).parentsUntil(".multiBox")[4].firstChild
                        var label = parentBtn.firstChild
                        var txt = $(label).text()
                        if(txt == "None selected"){
                            //error make red and 
                            $(parentBtn).css('border', 'solid 1px #dc3545')
                            $(parentBtn).find("i").remove();
                            $(parentBtn).append('<i class="fa fa-times" aria-hidden="true" style="color:#dc3545;padding-top:5px;padding-right:5px;"></i>')
                        }else{
                            //for more than one checkbox remove all then add one
                            $(parentBtn).find("i").remove();
                            $(parentBtn).css('border', 'solid 1px #28a745')
                            $(parentBtn).append('<i class="fa fa-check" aria-hidden="true" style="color:#28a745;padding-top:5px;padding-right:5px;"></i>')
                        }
                    });
                }
            }
            });
          }, false); 
        }, false);
    })();
    
    //multi select validation issues continue

    

</script>
<?php include 'footer.php';?>