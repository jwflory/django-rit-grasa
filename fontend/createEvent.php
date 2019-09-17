<?php include 'header.php';?>
<div class="container event-container">
    <div class="row">
        <div class="col-12">
            <button type="button" class="btn btn-danger float-right" id="cancelBtn"><i class="fa fa-times" aria-hidden="true"></i> Cancel</button>
        </div>
    </div>
    <div class="row">
        <div class="col-sm-4">
                    <div class="form-group">
                        <label>Age Group</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="e.g., 7-10">
                    </div>  
                
                    <div class="form-group">
                        <label>Category</label>
                        <select class="form-control">
                            <option>Select Category...</option>
                            <option>Theatre</option>
                            <option>Sports</option>
                            <option>Arts</option>
                            <option>Cooking</option>
                            <option>Robotics</option>
                            <option>Other</option>
                        </select>
                    </div>    
                
                    <div class="form-group">
                        <label>Location</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Street Address...">
                    </div>    
               
                    <div class="form-group">
                        <label>Website (optional)</label>
                        <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="http://">
                    </div>  
        </div>
        <div class="col-sm-8">
            <div class="form-group">
                <label>Program Name</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" placeholder="Name...">
            </div>
            <div class="form-group">
                <label>Description</label>
                <textarea class="form-control" id="exampleFormControlTextarea1" rows="10" placeholder="Tell us about your program..."></textarea>
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
    var cancelBtn = document.getElementById('cancelBtn');
    cancelBtn.onclick = function(){
        window.location = 'provider.php'
    }

</script>
<?php include 'footer.php';?>