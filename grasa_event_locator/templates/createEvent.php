{% include "header.php" %}
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
                <h5 class="modal-title" id="exampleModalLabel">Submit</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
               Looks Good! Your event will be submitted to the administrators for approval. Until it is approved, your event will not appear in search results.
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-danger" data-dismiss="modal"><i class="fa fa-times" aria-hidden="true"></i> Cancel</button>
                <button type="button" class="btn btn-success" id="submitOkBtn"><i class="fa fa-check" aria-hidden="true"></i> Submit for Approval</button>
                
              </div>
            </div>
          </div>
        </div>
        
    </div>
    
    <form class="needs-validation" method="post" novalidate>
    {% csrf_token %}
      <div class="form-row">
            <div class="col-sm-8">
                <div class="form-group">
                    <label>Program Name</label>
                    <input type="text" class="form-control" placeholder="Program Name..." name="title" required>
                    <div class="invalid-feedback">
                        Please provide a name for your program.
                    </div>
                </div>
                <div class="form-group">
                    <label>Description</label>
                    <textarea class="form-control" id="exampleFormControlTextarea1" rows="4" placeholder="Tell us about your program..." name="content" required></textarea>
                    <div class="invalid-feedback">
                        Please provide a description for your program.
                    </div>
                </div>
                <div class="form-group">
                    <label>Location</label>
                    <input type="text" class="form-control" id="addressInput" placeholder="Street Address..." name="address" required>
                    <input type="text" id="lat" name="lat" value="0" readonly>
                    <input type="text" id="lng" name="lng" value="0" readonly>
                    <div class="invalid-feedback">
                        Please provide your program's street address.
                    </div>
                </div>
                <div class="form-group">
                    <label>Website (optional)</label>
                    <input type="url" class="form-control" id="exampleFormControlInput1" placeholder="http://" name="website">
                </div>
                <fieldset class="pocFieldset">
                    <legend>Point of Contact</legend>
                   <div class="form-row">
                        <div class="form-group col-md-4">
                          <label for="contactname">Name</label>
                          <input type="text" class="form-control" id="contactname" placeholder="Name..." name="contact_name" required>
                            <div class="invalid-feedback">
                                Please provide your program's contact name.
                            </div>
                        </div>
                        <div class="form-group col-md-4">
                          <label for="email">Email</label>
                          <input type="email" class="form-control" id="email" placeholder="Email..." name="contact_email" required>
                            <div class="invalid-feedback">
                                Please provide your program's contact email.
                            </div>
                        </div>
                        <div class="form-group col-md-4">
                          <label for="phone">Phone</label>
                          <input type="tel" class="form-control" id="phone" placeholder="Phone..." name="contact_phone" required>
                            <div class="invalid-feedback">
                                Please provide your program's contact phone number.
                            </div>
                        </div>
                      </div>
                 </fieldset>
            </div>
            <div class="col-sm-4">
                <div class="form-group text-left multiBox">
                    <label>Activity</label><br>
                    <select class="form-control custom-select w-100 activitySelect" id="basic" multiple="multiple" name="activity" required>
                    </select>
                    <div class="invalid-feedback">
                        Please select at least one activity.
                    </div>
                </div>
                <div class="form-group">
                    <label>Transportation</label>
                    <select class="form-control" name="transportation" required>
                        <option name="Transportation Not Provided">Not Provided</option>
                        <option name="Transportation Provided">Provided</option>
                    </select>
                </div>
                <div class="form-group text-left multiBox">
                    <label>Grades Served</label><br>
                    <select class="custom-select w-100 gradesSelect" id="basic" multiple="multiple" name="grades" required>
                    </select>
                    <div class="invalid-feedback">
                        Please select at least one grade group.
                    </div>
                </div>
                <div class="form-group">
                    <label>Gender</label>
                    <select class="form-control" name="gender" required>
                        <option name="Not Specified">Not Specific</option>
                        <option name="Female">Female</option>
                        <option name="Male">Male</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="fees">Fees</label>
                    <div class="input-group mb-3">
                      <div class="input-group-prepend">
                        <span class="input-group-text">$</span>
                      </div>
                      <input type="number" class="form-control" aria-label="Amount (to the nearest dollar)" placeholder="0.00" name="fees" required>
                        <div class="invalid-feedback">
                            Please enter total amount of fees. If the program is free enter 0.00
                        </div>
                    </div>

                </div>
                <div class="form-group text-left multiBox">
                    <label>Timing</label><br>
                    <select class="custom-select w-100 timingSelect" id="basic" multiple="multiple" name="timing" required>
                    </select>
                     <div class="invalid-feedback">
                        Please select at least one time.
                    </div>
                </div>


            </div>
        </div>

      <button class="btn btn-success float-right" type="submit">Validate Event</button>
    </form>


</div>
<script>

    //Cancel Button and Ok Button returns to provider page
    var cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.onclick = function(){
        window.location = 'provider.php'
    }
    var okBtn = document.getElementById('submitOkBtn');
    okBtn.onclick = function(){
        //SUBMITS the form
        $('form').submit()
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
            $( "."+location).append( "<option value=\""+list[i]+"\">"+list[i]+"</option>" );
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
            if(form.checkValidity() === false) {
              event.preventDefault();
              event.stopPropagation();
            }else{
                event.preventDefault();
                event.stopPropagation();
                //IF CLIENT SIDE VALIDATION WORKS YOU END UP HERE
                doGeocoding().then(function(results){
                    //sends an alert if something is wrong with the geocoding.
                    console.log("geocoding should be done")
                    if(geoCheck() === false){
                        alert('There was a problem finding your event location.')
                    }else{
                        $('#submitModal').modal('show');
                    }
                });
                
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
    
    //function that geocodes the street address
    function doGeocoding(){
        var streetString = $('#addressInput').val();
        var api_url = 'http://www.mapquestapi.com/geocoding/v1/address?key=nEoQhpyWJ6K3nx0wsur3eVa4oYAfhvhY&location='+streetString
        return fetch(api_url).then((resp) => resp.json()).then(function(data) {
            if(data.info.statuscode === 0){
                 $('#lat').val(data.results[0].locations[0].latLng.lat)
                 $('#lng').val(data.results[0].locations[0].latLng.lng)
                 return true;
            }else{
                 $('#lat').val('nil')
                 $('#lng').val('nil')
                return false;
            }
            console.log("geocoding is done")
          }).catch(function(error) {
            $('#lat').val('nil')
            $('#lng').val('nil')
            console.log(error);
            return false;
        });
    }
    
    //function to check if the geocoding worked
    function geoCheck(){
        if($('#lat').val() === 'nil' || $('#lng').val() === 'nil'){
            return false;
        }else{
            return true;
        }
    }
    
</script>
{% include "footer.php" %}