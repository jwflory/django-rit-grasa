<!doctype html>
<html lang="en">
<head>
    <!--Bootstrap Style-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    
    <!--Our Custom Style-->
    <link rel="stylesheet" type="text/css" href="styles/style.css">
    
    <!--Font Awesome 4-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    
    
    <!--Bootstrap JS Code-->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    
    <!--Custom 3rd Party Bootstrap Code-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/js/bootstrap-multiselect.min.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/css/bootstrap-multiselect.css">
    
    
    
    
    <title>GRASA Web Application</title>
</head>
<script>
    //Initalize data client side only for testing only
            //Categories
        var groupList = ["Activity", "Transportation", "Grades Served", "Gender","Distance", "Fees", "Timing"]
        
        //Activity
        var activityList = ["Academic Support", "Arts and Culture", "Career or College Readiness", "Civic Engagement", "Community Service/ Service Learning", "Entrepreneurship/ Leadership", "Financial Literacy", "Health & Wellness", "Media Technology",  "Mentoring", "Nature & the Environment", "Play", "Public Speaking", "Social and Emotional Learning (SEL)", "Sports and Recreation", "STEM", "Tutoring", "Other"]

        //Transportation
        var transportationList = ["Provided", "Not Provided"]
        
        //Grades Served
        var gradesList = ["K-3rd", "K-5th", "3rd-5th", "6th-8th", "9th-12th"]
        
        //Gender
        var genderList = ["Male Only", "Female Only", "Non-Specific"]
        
        //Distance
        var distanceList = ["0-5 miles", "6-10 miles", "11-15 miles", "16-20 miles", "20+ miles"]
        
        //Fees
        var feesList = ["Free", "$1-$25", "$26-$50", "$51-$75", "$75+"]
        
        //Timing
        var timingList = ["Before School", "After School", "Evenings", "Weekends", "Summer", "Other"]
        

</script>
<body class="d-flex flex-column h-100" cz-shortcut-listen="true">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
          <a class="navbar-brand" aria-label="GRASA-Logo" href="index.php">
          <img id="header-logo" src="media/grasalogo.png" alt="Logo">
        </a>

          <div class="collapse navbar-collapse" id="navbarsExample02">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <a class="nav-link" href="index.php">Home<span class="sr-only sr-only-focusable">(current)</span></a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="provider.php">Provider</a>
              </li>
                <li class="nav-item">
                <a class="nav-link" href="admin.php">Admin</a>
              </li>
            </ul>
          </div>
        <span class="form-inline mt-2 mt-md-0">
            <button onclick="window.location.href='/login.php'" class="btn btn-outline-light my-2 my-sm-0" >Login</button>
        </span>
    </nav>