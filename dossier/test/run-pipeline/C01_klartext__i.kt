process: #SD.2

	name: 
		Software Development Planning

	purpose:
		The objective of the "Software Development Planning" Process is to plan the software development tasks, communicate procedures and goals to members of the development team.

		Systematic software development planning ensures that risks caused by software are reduced and quality characteristics for the medical device software are met.
	

	base-practices:

		base-practice: #SD2_BP1 part-of-process="development"

			title: 
				Establish a Software Development Plan
            
			Establish a plan for the software development. Design the plan appropriate to the scope, the magnitude and the software safety classification of the software system.

			achieves> SD2_OC1

			references> IEC62304:2006 section="5.1.1" class="A,B,C"
			references> ISO13485:2003 section="7.3.1"
			references> IEC60601-1:2005 section="14.4"


        base-practice: #SD2_BP2

            title: 
				Determine safety class

			Assign a software safety class to the software system according to the following classification:
            
			* Class A: No injury or damage to health is possible
            * Class B: Non-serious injury is possible
			* Class C: Death or serious injury is possible

			Document the software safety class.

			!!! note
				For each software system, until a software safety class is assigned, class C requirements shall apply.

			achieves> SD2_OC2
			
			references> IEC62304:2006 section="4.3" class="A,B,C"

process: #SD.2

	name: Software Development Planning

	purpose:
		The objective of the "Software Development Planning" Process is to plan the software development tasks, communicate procedures and goals to members of the development team.

		Systematic software development planning ensures that risks caused by software are reduced and quality characteristics for the medical device software are met.
