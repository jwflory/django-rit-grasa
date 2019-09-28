{ % include header.php % }

	<div class="container about-container">
		
		<div class="about-row">

			<h2 id="about">About Us</h2>
			<span class="subhead">OUR STORY</span>
			
			<p class="main-content">
			Lorem Ipsum er ganske enkelt fyldtekst fra print- og typografiindustrien. Lorem Ipsum har været standard 
			fyldtekst siden 1500-tallet, hvor en ukendt trykker sammensatte en tilfældig spalte for at trykke en bog 
			til sammenligning af forskellige skrifttyper. Lorem Ipsum har ikke alene overlevet fem århundreder, 
			men har også vundet indpas i elektronisk typografi uden væsentlige ændringer. Sætningen blev gjordt kendt 
			i 1960'erne med lanceringen af Letraset-ark, som indeholdt afsnit med Lorem Ipsum, og senere med 
			layoutprogrammer som Aldus PageMaker, som også indeholdt en udgave af Lorem Ipsum.
			<br>			
			
			I modsætning til hvad mange tror, er Lorem Ipsum ikke bare tilfældig tekst. Det stammer fra et stykke 
			litteratur på latin fra år 45 f.kr., hvilket gør teksten over 2000 år gammel. Richard McClintock, 
			professor i latin fra Hampden-Sydney universitet i Virginia, undersøgte et af de mindst kendte ord 
			"consectetur" fra en del af Lorem Ipsum, og fandt frem til dets oprindelse ved at studere brugen gennem 
			klassisk litteratur. Lorem Ipsum stammer fra afsnittene 1.10.32 og 1.10.33 fra "de Finibus Bonorum et 
			Malorum" (Det gode og ondes ekstremer), som er skrevet af Cicero i år 45 f.kr. Bogen, som var meget 
			populær i renæssancen, er en afhandling om etik. Den første linie af Lorem Ipsum "Lorem ipsum dolor sit 
			amet..." kommer fra en linje i afsnit 1.10.32.
			Standardafsnittet af Lorem Ipsum, som er brugt siden 1500-tallet, er gengivet nedenfor for de, der er interesserede. 
			Afsnittene 1.10.32 og 1.10.33 fra "de Finibus Bonorum et Malorum" af Cicero er også gengivet i deres nøjagtige 
			udgave i selskab med den engelske udgave fra oversættelsen af H. Rackham fra 1914.
	
			
			</p>		

		</div>
	
	</div>

  </section>
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
									<input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
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
								<button type="submit" class="btn btn-primary">Submit</button>
							
							
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
							<a href="https://www.monroecounty.gov/" target="_blank"><i class="fa fa-globe"></i></i>
							www.moroecounty.gov </a>							
						</p>
						<h5>Office Hours</h5>
						<p>
							Mon - Fri : 9a.m - 5p.m <br>
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
										
		</section>
		
	</div>
		
	
<?php include 'footer.php';?>
