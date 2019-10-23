{% load static %}

<!doctype html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!--Bootstrap Style-->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <!--Our Custom Style-->
    <link rel="stylesheet" type="text/css" href="{% static "css/custom.css" %}">

    <!--Font Awesome 4-->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">


    <!--Bootstrap JS Code-->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

    <!--Custom 3rd Party Bootstrap Code-->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/js/bootstrap-multiselect.min.js" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-multiselect/0.9.13/css/bootstrap-multiselect.css">

    <!--Leaflet Code-->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.5.1/dist/leaflet.css"
   integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
   crossorigin=""/>




    <title>GRASA Web Application</title>
</head>
<script>
    //Initalize data client side only for testing only
            //Categories
        var groupList = ["Activity", "Transportation", "Grades Served", "Gender","Distance", "Fees", "Timing"]

        //Activity
        var activityList = ["Academic Support", "Arts and Culture", "Career or College Readiness", "Civic Engagement", "Community Service / Service Learning", "Entrepreneurship / Leadership", "Financial Literacy", "Health & Wellness", "Media Technology",  "Mentoring", "Nature & the Environment", "Play", "Public Speaking", "Social and Emotional Learning (SEL)", "Sports and Recreation", "STEM", "Tutoring", "Other"]

        //Transportation
        //Refactored to match header and forms as well as fix duplicate search bug
        var transportationList = ["Provided", "Not-Provided"]

        //Grades Served
        var gradesList = ["K-3rd", "K-5th", "3rd-5th", "6th-8th", "9th-12th"]

        //Gender
        //Refactored to match header and forms as well as fix duplicate search bug
        var genderList = ["Male-Only", "Female-Only", "Non-Specific"]

        //Distance
        var distanceList = ["0-5 miles", "6-10 miles", "11-15 miles", "16-20 miles", "20+ miles"]

        //Fees
        var feesList = ["Free", "$1-$25", "$26-$50", "$51-$75", "$75+"]

        //Timing
        //Refactored to "Other Time", "Before-School", and "After-School" to avoid conflicts with activities "Other" as well as fix duplicate search bug
        var timingList = ["Before-School", "After-School", "Evenings", "Weekends", "Summer", "Other-Time"]

</script>
<body class="d-flex flex-column h-100" cz-shortcut-listen="true">
    <nav class="navbar navbar-expand navbar-dark bg-dark">
          <a class="navbar-brand" aria-label="GRASA-Logo" href="/index.php">
          <img id="header-logo" src="{% static "img/grasalogo.png" %}" alt="Logo">
        </a>

          <div class="collapse navbar-collapse" id="navbarsExample02">
            <ul class="navbar-nav mr-auto">
              <li class="nav-item active">
                <a class="nav-link" href="/index.php">Browse Events<span class="sr-only sr-only-focusable">(current)</span></a>
              </li>
              {% if not user.userinfo.isAdmin %}
              <li class="nav-item">
                <a class="nav-link" href="/provider.php">Provider</a>
              </li>
              {% endif %}
              {% if user.userinfo.isAdmin or not user.is_authenticated %}
                <li class="nav-item">
                <a class="nav-link" href="/admin.php">Admin</a>
              </li>
              {% endif %}
              {% if not user.is_authenticated %}
              <li class="nav-item">
                <a class="nav-link" href="admin_user">Create Administrator Account</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="admin_activate">Reactivate Administrator Account</a>
              </li>
              {% endif %}
            </ul>
          </div>
        <span class="form-inline mt-2 mt-md-0">
        {% if user.is_authenticated %}
            {% if not user.userinfo.isAdmin and user.is_authenticated %}
                <a class="nav-link" style="color:white;">{{ user.userinfo.org_name }}</a>
            {% endif %}
            <button onclick="window.location.href='/logout'" class="btn btn-outline-light my-2 my-sm-0" >Logout</button>
        {% else %}
            <button onclick="window.location.href='/login.php'" class="btn btn-outline-light my-2 my-sm-0" >Login</button>
        {% endif %}
        </span>
    </nav>
