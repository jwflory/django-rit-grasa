{% include "header.php" %}

	<div class="container about-container">
		
		<div class="about-row">
            <br>
			<h2 id="about">About Us</h2>
			<span class="subhead">OUR STORY</span>
			
			<p class="main-content">
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sed nunc ac neque interdum euismod id sit amet purus. Nam ut dapibus purus, non laoreet lectus. Mauris et sollicitudin velit, malesuada aliquam neque. Mauris a vehicula erat, sit amet rhoncus ante. Praesent nulla mi, tincidunt et porttitor ac, congue in tellus. Aliquam erat volutpat. Nulla pretium non dolor sit amet euismod. Donec a metus id elit cursus fermentum a sed lectus. Integer iaculis blandit mauris, quis pharetra ex varius sit amet. Morbi suscipit magna lectus, et interdum tellus porttitor a. Pellentesque volutpat luctus consequat. Phasellus nisi lorem, sodales ac malesuada at, molestie non metus. Sed finibus tincidunt elit ac bibendum. Donec non diam efficitur, pulvinar arcu iaculis, congue tortor. Curabitur enim metus, condimentum pellentesque iaculis ac, auctor eu odio.</p>

            <p>Phasellus volutpat lacus sit amet mi aliquam ultrices. Sed dui nisl, fermentum sit amet commodo ut, auctor et arcu. Proin non erat ut justo euismod viverra. Nunc tempus rhoncus tellus ac efficitur. Sed vel tincidunt eros, non venenatis nunc. Maecenas blandit erat varius leo dictum, a sagittis diam viverra. Integer et libero nec est placerat tincidunt. Pellentesque egestas, justo vitae molestie tincidunt, risus ipsum blandit erat, ac egestas lacus urna sed ligula. Proin id accumsan lorem, vel blandit justo. Aenean pellentesque at lorem non tincidunt. Aliquam efficitur vitae mi at rhoncus. Proin rutrum facilisis mi, a facilisis nunc commodo vel. Ut pulvinar in diam non consectetur. Proin et tincidunt eros.
	
			
			</p>		

		</div>
	
	</div>
	<div class="container contact-container">
		
				<h2 id="contact">Contact Us</h2>
				<hr><br>
				<div class="row">
					<div class="col-lg-7">
						<div class="form-contact">
						<form action="aboutContact.php">
							<div class="form-row">
								
								<div class="form-group col-md-6">
									<label for="exampleInputName">Full Name</label>
									<input type="text" class="form-control" placeholder="Enter full name *">
								</div>
								
								<div class="form-group col-md-6">
									<label for="exampleInputNumber">Phone Number</label>
									<input type="number" class="form-control" placeholder="Contact Number *">
								</div>
								
							</div>
							
							<div class="form-row">
								<div class="form-group col-md-12">
									<label for="exampleInputEmail1">Email address</label>
									<input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email *">
									<small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
								</div>
							</div>
							
							<div class="form-row">
								<div class="form-group col-md-12">
									<label for="exampleInputSubject">Subject</label>
									<input type="text" class="form-control" placeholder="Subject *">
								</div>
							</div>
							
							<div class="form-row">	
								<div class="form-group col-md-12">
									<label for="exampleInputMsg">Message</label>
									<textarea class="form-control" rows="6" placeholder="Type your message for us here *"></textarea>
								</div>
							</div>
								<button type="submit" class="btn btn-success">Submit</button>
							
							
						</form>
						</div>
					</div>
					
					
					<div class="col-lg-1">
					</div>
					<div class="col-lg-4 address">
						
						<h5>Call Us </h5>
						<p><a href="tel:+5951234567"><i class="fa fa-phone" aria-hidden="true"></i> (+1) 585-123-4567 </a><br>
						
						</p>
						<h5>Email</h5>
						<p>
							<a href="mailto:johndoe@gmail.com"><i class="fa fa-envelope"></i>
							johndoe@gmail.com</a>
						</p>						
						<h5>Website</h5>
						<p>
							<a href="https://www.monroecounty.gov/" target="_blank"><i class="fa fa-globe"></i>
							www.moroecounty.gov </a>							
						</p>
						<h5>Office Hours</h5>
						<p>
							Mon - Fri : 9am - 5pm <br>
							Sat - Sun : closed
						</p>
						
						<h5>Address</h5>
						<p>
							111 Monroe County <br>
							New York 14623
							
						</p>
					</div>
				</div>
			</div>
		
	
{% include "footer.php" %}