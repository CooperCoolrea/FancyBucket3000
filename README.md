# FancyBucket3000

## Summary of Project
The Fancy Bucket 3000 is a rain collection system with volume sensing, pH sensing, and an automatic valve opening for irrigation systems. This system utilizes an ultrasonic sensor to determine when the rain barrel is getting full and will notify the user that water testing needs to be done before releasing the water to the plants. We integrated a digital pH sensor to report the acidity of the water to the user and recommend treatments if necessary. Once the user tells the system the water is treated by pushing a button on our UI, our system opens a ball valve to release the water to the irrigation system. This system will consist of piping from the Fancy Bucket 3000 to a prepared trough with soil and plants. Our project is fully operational and meets all outputs listed in the project initiation.

## Design Description
### Materials


**Table 1: Bill of Materials**

| **Part Number** | **Part Name**    | **Description**                                             | **Notes**                             | **Quantity** | **Units** | **Total Cost** | **Supplier** | **Supplier Part Number** | **Link** | **Package Size** | **Unit** | **Package price** |
|-----------------|------------------|-------------------------------------------------------------|----------------------------------------|--------------|-----------|----------------|--------------|---------------------------|-------------------------------------------------------------------------------------------------------------|------------------|----------|--------------------|
| 1001 | Plastic Bucket | 5-Gallon, HDPE | Comes with wire handle | 1.0 | each | 3.73 | Menards | 6482910 | [Link](https://www.menards.com/main/grocery-home/cleaners-household-essentials/cleaning-supplies/cleaning-tools/menards-reg-5-gallon-bucket/6482910/p-1444426310607-c-7113.htm) | 1.0 | each | 3.73 |
| 1002 | pH sensor | Teyleten pH detection sensor | arduino compatible | 1.0 | each | 18.99 | Amazon | B09H1MJS4S | [Link](https://www.amazon.com/dp/B09H1MJS4S) | 1.0 | each | 18.99 |
| 1003 | wood glue | Gorilla Wood Glue |  | 0.12 | fl oz. | 0.1191 | Home Depot | 62020 | [Link](https://www.homedepot.com/p/Gorilla-4-oz-Wood-Glue-62020/100672057) | 4.0 | fl oz. | 3.97 |
| 1004 | Ball Valve | U.S. Solid Motorized Ball Valve- 1/2" Brass Ball Valve | 9-24V AC/DC and 2 Wire Auto Return Setup | 1.0 | Each | 34.02 | Amazon | ANSI B16.34, IP65 | [Link](https://www.amazon.com/dp/B072QW8ST4) | 1.0 | Each | 34.02 |
| 1005 | Plywood | 3/4 inch thick, sanded plywood |  | 225.0 | Sq in | 4.666 | Home Depot | 205960 | [Link](https://www.homedepot.com/p/Handprint-3-4-in-x-2-ft-x-4-ft-Sanded-Plywood-205960/205960) | 1152.0 | Sq in | 23.89 |
| 1006 | Porch screening | Charcoal fiberglass screen roll |  | 33.18 | sq in | 0.262 | Home Depot | FCS10396-M | [Link](https://www.homedepot.com/p/Saint-Gobain-ADFORS-36-in-x-84-in-Charcoal-Fiberglass-Screen-Roll-FCS10396-M/203176333) | 3024.0 | sq in | 11.48 |
| 1007 | 2.5 inch screws | Coarse zinc-plated steel square-head pocket screw |  | 16.0 | each | 2.71 | Home Depot | SML-C250-50 | [Link](https://www.homedepot.com/p/Kreg-2-1-2-in-Coarse-Zinc-Plated-Steel-Pocket-Screws-50-Pack-SML-C250-50/100401223) | 50.0 | each | 8.47 |
| 1008 | 1.25 inch screws | Square maxi-Loc head coarse zinc-plated steel pocket-hole screw |  | 12.0 | each | 1.14 | Home Depot | SML-C125-100 | [Link](https://www.homedepot.com/p/Kreg-1-1-4-in-Square-Maxi-Loc-Coarse-Zinc-Plated-Steel-Pocket-Hole-Screw-100-Pack-SML-C125-100/100401222) | 100.0 | each | 9.47 |
| 1009 | Epoxy | Gorilla Clear Epoxy Adhesive |  | 0.85 | fl oz. | 7.48 | Lowes | 13111000 | [Link](https://www.lowes.com/pd/Gorilla-Epoxy-Clear-Epoxy-Adhesive/5002785627) | 0.85 | fl oz. | 7.48 |
| 1010 | Bucket lid | Standard lid for 5 gallon plastic pail |  | 1.0 | each | 2.00 | Uline | S-9948BLU | [Link](https://www.uline.com/Product/Detail/S-9948BLU/Pails/Standard-Lid-for-35-5-6-and-7-Gallon-Plastic-Pail-Blue) | 1.0 | each | 2.00 |
| 1011 | Bucket connector | 1/2 in. PVC schedule 40 male adapter |  | 1.0 | each | 0.59 | Home Depot | PVC021090600HD | [Link](https://www.homedepot.com/p/Charlotte-Pipe-1-2-in-PVC-Schedule-40-Male-MPT-x-S-Adapter-PVC021090600HD/203811636) | 1.0 | each | 0.59 |
| 1012 | Silicone caulk | GE Silicone 1 All Purpose Clear Caulk |  | 1.5 | oz | 1.32 | Lowes | 2795576 | [Link](https://www.lowes.com/pd/GE-Silicone-1-All-Purpose-Windows-Doors-Exteriors-10-1-oz-Clear-Silicone-Caulk/5013443639) | 10.1 | oz | 8.88 |
| 1013 | Hot glue | AdTech Crystal Clear Hot Glue Sticks | 4" length, .44 in diameter | 3.0 | sticks | 1.04 | Walmart | - | [Link](https://www.walmart.com/ip/AdTech-Crystal-Clear-Hot-Glue-Gun-Full-Size-4-x-44-10-Sticks/22217933) | 10.0 | sticks | 3.48 |


### Drawings and Circuit Diagrams
### Code
### Assembly Instructions
**Bucket and Stand Assembly**
1. To assemble the bucket and stand, we started by using a compass to outline the size of the hole we wanted to cut in the lid. Using a drill, we made a hole inside of the circle we drew to make a starting point to cut the circle out. Using a jig saw, we cut the circle out of the lid.

2. We cut a circle out of the screening that was slightly bigger than the hole cut in the lid. Using a scrap piece of cardboard as a mixing plate and a paint stick we mixed the gorilla two part epoxy. We used the paint stick to dab the epoxy on the perimeter of the circle, and placed the cut screening on the epoxy. We tapped the screen down onto the epoxy while wearing gloves, then taped the sides of the screen down to dry, as shown in the image below.
<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/drying%20lid.JPG">
</p>
<p align="center">
  <em>Figure x: Lid and mesh cover drying after assembly</em>
</p>

3. Using a table saw, we cut a 16" by 16" square. Using a Miter Saw, we cut 4 16" long pieces, two 12" long pieces, and one 8" long piece from the 2-in x 4-in lumber. 

4. Starting with the 16" long pieces, we calibrated our pocket hole guide and drilled 3 pocket holes on one side of the pieces. The same thing was done on the 12" long pieces, and 8" piece, but 6 holes total were cut. Three holes in a row, but done on both sides of the same surface.

5. Once all pocket holes were drilled, we spread wood glue on the cut edge of the 16" pieces, on side with the pocket holes. The glue was placed down on the corner of the plywood piece, and a clamp was used to secure it in place. Using XXX inch screws, we drilled the screws into the pocket holes to fully secure the legs of the stand. 

6. The same process was done with the 12" long pieces, but they were clamped horizontally between the legs, 1 inch down from the base of the legs. For the 8" piece, it was glued horizontally between the two 12" pieces. All of these pieces were clamped down and set to dry overnight. The following image shows the pieces together, clamped down to dry. 
<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/drying%20stand.JPG">
</p>
<p align="center">
  <em>Figure X: Wooden stand drying after assembly</em>
</p>

7. For the valve portion of the bucket, we used a drill with a step cone drill bit attachment to make a 1/2 inch hole in the center of the bottom of the bucket. We applied silicone caulk  to the area around the hole on the inside of the bucket, and screwed in the pipe attachment as far as it could go. This was left to dry overnight. When the bucket was eventually dry, a wrench was used to hold the pipe in place while the sensor was glued on. 
 
8. To cut the hole in the wooden stand, we sketched out an area around the size of the entire valve, and used an oscillating saw to cut out the hole. 

9. For the waterproof box around our electronics, we 3D modeled and printed a box and sliding door in Autodesk Fusion. The following images show the design and box, and the 3D model is in the repository. 

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/3D%20box.png">
</p>
<p align="center">
  <em>Figure X: 3D model of waterproof box</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/3D%20lid.png">
</p>
<p align="center">
  <em>Figure X: 3D model of waterproof box lid</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/box%20picture.JPG">
</p>
<p align="center">
  <em>Figure X: Final 3D printed box and lid</em>
</p>

10. When the box was printed, we had to drill some holes in the box to allow for wires to get out, these are shown below. 

INSERT PIC

11. To attach the box to the bucket, first we hot glued the arduino where we wanted it to sit. Then …………………………..


**Circuit**
1. To construct our system, we first built a simple circuit that included a ball valve and a motor controller.
2. Next, we had to create a second power supply for the ball valve. One thing that we did not originally consider when we ordered the ball valve was that it required at least 9 Volts of power to function properly. Our Redboard could only provide 5 Volts and the battery pack that came with our Sparkfun Inventor Kit could only provide 6 Volts (1.5 Volts per battery). Thus, we found a 12 Volt source, then retrofit the wires to fit the ground and positive wires of the connector of the double A battery pack holder. After stripping the wires, we used a multimeter to determine which wire was positive and which was negative. Then, we soldered them to the battery pack connecter and wrapped the wires in electrical tape.
3. Next, we added a pH sensor. We connected wires to the ports on the pH sensor for power, ground, and one labled "Po" to represent pH output.
4. Finally, we incorporated an ultrasonic sensor. The final circuit diagram can be seen in figure _____. A picture of our final circuit can be seen in figure ________.

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Circuit%20Diagram-1.jpg">
</p>
<p align="center">
  <em>Figure X: Complete Circuit Diagram </em>
</p>

**Software and GUI**
1. To create the code for our project, we prompted ChatGPT to create a script for Arduino IDE that controls an electronic ball valve, a pH sensor, and an ultrasonic sensor. To control the electronic ball valve, the program needed to open the valve with the click of a button and automatically close the valve after water has been released. The pH sensor needed to read the pH accurately, report it to the user, and provide a treatment recommendation. The ultrasonic sensor needed to report the volume to the user and notify the user when it is too full.
2. After ChatGPT provided the code, we tested it with our circuit design. If it did not work appropriately, we would identify the issue, then prompt ChatGPT to fix it. We continued this process until our code worked successfully.
3. Once we had a working code, we had ChatGPT rewrite it in Python to be used in Visual Studio with a user interface (UI).


## Testing Description
### Test Equipment
* Cups of water from different sources

### Testing Procedures
Could another test engineer replicate your tests?
All test equipment specified (model numbers) and procedures fully described

**Volume Sensing**
1. To test if the ultrasonic sensor was working correctly and that our GUI was showing the correct volume, we would first fill our bucket to any depth.
2. Then, we would measure the depth and multiply that depth by the cross sectional area of the bucket. 
3. Finally, we would run our code and see if the volume value it was reporting was approximately the same as the calculated value. If it was not, we would recallibrate our code and rerun the test.


**pH Sensing**
1. To test the pH sensor, we filled cups with fluids that had different pH values. 
2. Then we would remove the pH sensor from its cover and insert it into the different fluids.
3. Between each different solution, we made sure to insert the probe into distilled water as a calibration technique.
4. Finally, we would ensure that the pH values being reported by the serial monitor were approximately correct. We merely ensured that anything that was in its estimated range. If we were testing the pH sensor in an extremely acidic solution, we knew our pH sensor was not working if it was reporting an almost neutral solution.
5. Initially, our pH sensor was reporting very similar, neutral values no matter what fluid it was submerged in. To fix this, we integrated a calibration function into our code. Based on the voltage the probe was measuring in distilled water, the calibration function ensured that the output would be close to a neutral pH of 7. Once we utilized the calibration function, we recieved accurate pH results in different solutions.


**Automatic Ball Valve**
1. To test the automatic valve opening, we merely had to run our code and click the button on our GUI that was labeled “Open Valve.” If the valve opened, we considered that to be a successful trial.
2. Then, to test the closing function, we clicked the button on our GUI that was labeled “Close Valve.” If the valve closed, that was a successful trial. 
3. Finally, the valve needed to close automatically when it was empty. To test this, we would allow the bucket to release all of its contents, then we would observe the behavior of the ball valve. If it closed after releasing all the water, we considered that a successful trial.


## Design Decision Discussion
One of the first design decisions we made was to put a lid on our bucket with a large hole cutout with a mesh covering. This prevents leaves from getting in the bucket and allows water to enter. The border of the cutout is where the ultrasonic sensor rests. This prevents it from being rained on from above; however, the sensor would still be at risk of water damage if the bucket overfills. There is definitely room to improve this design. For example, someone could add a cover that automatically closes the bucket when it gets full. This would eliminate any risk of water damage. We would have probably included this in our design if we were not limited on time.

Another design decision we made was to use a ball valve as the connection between the water storage and water distribution. We mainly decided to use a ball valve because we were afraid that a solenoid valve would be unable to open with the amount of pressure at the bottom of our bucket. We also considered rigging up an automatic opening with a servo or stepper motor; however, we decided that neither motor would have the power to open against the pressure of the water. The ball valve we used was also fairly simple to implement after having a proper power supply. We merely had to connect it to a motor controller and code it like any other component. Using a servo, stepper motor, or solenoid valve would've required more work and troubleshooting.

We decided to use an electronic pH sensor in the interest of time. It was very simple to code and calibrate. We also included a manual option on our GUI in case our users wanted to use a paper pH strip, then input their own reading. We were originally going to use a camera and code it to read the pH from the color; however, we decided this would be difficult since we would have to worry about interference from background colors and potentially would’ve had to utilize artificial intelligence. We also considered only using a manual option; however, we wanted to challenge ourselves and did not want there to have to be a secondary purchase to use our device. Another engineer could implement the camera reading with artificial intelligence or use manual entry only for simplicity.

We decided to 3D print a plastic box to hold our Redboard and circuitry because we wanted to protect the electronics from water damage. The lid of our electronic box includes a holder for the pH sensor. It may have been simpler to cut out a box from wood or metal; however, we did not want to have to wait for glue to dry, weld, or seal the box. Additionally, other engineers could improve on our design by making the box more flush with the curved surface of the bucket. We made ours flat and caulked it, because it was quick and effective. We also kept in mind that this was just a prototype.

One thing we debated at the beginning stages of our project was where to put the outlet of our bucket. We were debating whether or not to put it on the bottom surface or whether to put it on the side of the bucket. We decided to put it on the bottom since it allowed for minimal water stagnation, it provided clearance for our hose, and we had gravity working to encourage flow downward. One issue with this location is that our internal pipe connection is not entirely flush with the bottom and extends upward into the bucket. This means the bucket will never be completely empty. Another engineer could improve our design by slanting the inside of the bottom of the bucket. This would prevent any stagnation.

## Testing Results Discussion
Are the capabilities of the system described? Where would this design work? How well does it work? What are its limitations? What can it not do?
It is clear what the system can do, cannot do, and where it works best

**Volume Sensing**

**Table 1: Accuracy of Volume Sensing Function**
|Trial|Measured Volume of Water Inputted (L)|Volume Detected (L)|
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

**pH Sensing**

**Table 2: Accuracy of pH Sensing Function**
|Trial|Solution|Anticipated pH|pH Detected|
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

**Automated Ball Valve**

**Table 3: Accuracy of Valve Opening Prompted by User**
|Trial|Button Clicked (Yes/No)|Valve Open? (Yes/No)|
|---|---|---|
| | | |
| | | |
| | | |
| | | |
| | | |

**Table 4: Accuracy of Valve Opening Prompted by Capacity of Barrel**
|Trial|Solution|Anticipated pH|pH Detected|
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |

## Testing Results
Were the test results described correctly? Were the proper tests performed to measure system capabilities?
Proper tests were conducted and results clearly documented

**Volume Sensing**

**pH Sensing**

**Automated Ball Valve**

The automatic valve responded reliably to user input provided through our Streamlit application. Specifically, each time the user clicked the designated button on the app interface, the valve successfully opened as intended. During all five experimental trials, the valve consistently released the water contained in the bucket immediately following the user’s command. This consistent performance across multiple repetitions demonstrates that the system's valve control functionality operated with perfect precision, achieving a 100% success rate. The seamless interaction between the software interface and the hardware mechanism confirms that the valve accurately and promptly executed the user’s instructions without any delay or malfunction, highlighting the reliability and effectiveness of our system's automated water release feature.

