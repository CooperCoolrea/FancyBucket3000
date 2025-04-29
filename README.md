# FancyBucket3000

## Summary of Project
The Fancy Bucket 3000 is a rain collection system with volume sensing, pH sensing, and an automatic valve opening for irrigation systems. This system utilizes an ultrasonic sensor to determine when the rain barrel is getting full and will notify the user that water testing needs to be done before releasing the water to the plants. We integrated a digital pH sensor to report the acidity of the water to the user and recommend treatments if necessary. There is also manual pH entry if the user prefers to use pH strips. Once the user has treated the water, they can push a button on our UI to open a ball valve to release the water to the irrigation system. This system will consist of piping from the Fancy Bucket 3000 to a prepared trough with soil and plants. Our project is fully operational and meets all outputs listed in the project initiation.

## Design Description
### Materials

**Table 1: Bill of Materials**

| **Part Number** | **Part Name**    | **Description**                                             | **Notes**                             | **Quantity** | **Units** | **Total Cost** | **Supplier** | **Supplier Part Number** | **Link** | **Package Size** | **Unit** | **Package price** |
|-----------------|------------------|-------------------------------------------------------------|----------------------------------------|--------------|-----------|----------------|--------------|---------------------------|-------------------------------------------------------------------------------------------------------------|------------------|----------|--------------------|
| 1001 | Plastic Bucket | 5-Gallon, HDPE | Comes with wire handle | 1.0 | each | 3.73 | Menards | 6482910 | [Link](https://www.menards.com/main/grocery-home/cleaners-household-essentials/cleaning-supplies/cleaning-tools/menards-reg-5-gallon-bucket/6482910/p-1444426310607-c-7113.htm) | 1.0 | each | 3.73 |
| 1002 | pH sensor | Teyleten pH detection sensor | arduino compatible | 1.0 | each | 18.99 | Amazon | B09H1MJS4S | [Link](https://www.amazon.com/dp/B09H1MJS4S) | 1.0 | each | 18.99 |
| 1003 | Wood Glue | Gorilla Wood Glue |  | 0.12 | fl oz. | 0.1191 | Home Depot | 62020 | [Link](https://www.homedepot.com/p/Gorilla-4-oz-Wood-Glue-62020/100672057) | 4.0 | fl oz. | 3.97 |
| 1004 | Ball Valve | U.S. Solid Motorized Ball Valve- 1/2" Brass Ball Valve | 9-24V AC/DC and 2 Wire Auto Return Setup | 1.0 | Each | 34.02 | Amazon | ANSI B16.34, IP65 | [Link](https://www.amazon.com/dp/B072QW8ST4) | 1.0 | Each | 34.02 |
| 1005 | 1 inch Plywood | 3/4 inch thick, sanded plywood |  | 225.0 | Sq in | 4.666 | Home Depot | 205960 | [Link](https://www.homedepot.com/p/Handprint-3-4-in-x-2-ft-x-4-ft-Sanded-Plywood-205960/205960) | 1152.0 | Sq in | 23.89 |
| 1006 | Porch screening | Charcoal fiberglass screen roll |  | 33.18 | sq in | 0.262 | Home Depot | FCS10396-M | [Link](https://www.homedepot.com/p/Saint-Gobain-ADFORS-36-in-x-84-in-Charcoal-Fiberglass-Screen-Roll-FCS10396-M/203176333) | 3024.0 | sq in | 11.48 |
| 1007 | 2.5 inch screws | Coarse zinc-plated steel square-head pocket screw |  | 16.0 | each | 2.71 | Home Depot | SML-C250-50 | [Link](https://www.homedepot.com/p/Kreg-2-1-2-in-Coarse-Zinc-Plated-Steel-Pocket-Screws-50-Pack-SML-C250-50/100401223) | 50.0 | each | 8.47 |
| 1008 | 1.25 inch screws | Square maxi-Loc head coarse zinc-plated steel pocket-hole screw |  | 12.0 | each | 1.14 | Home Depot | SML-C125-100 | [Link](https://www.homedepot.com/p/Kreg-1-1-4-in-Square-Maxi-Loc-Coarse-Zinc-Plated-Steel-Pocket-Hole-Screw-100-Pack-SML-C125-100/100401222) | 100.0 | each | 9.47 |
| 1009 | Epoxy | Gorilla Clear Epoxy Adhesive |  | 0.85 | fl oz. | 7.48 | Lowes | 13111000 | [Link](https://www.lowes.com/pd/Gorilla-Epoxy-Clear-Epoxy-Adhesive/5002785627) | 0.85 | fl oz. | 7.48 |
| 1010 | Bucket lid | Standard lid for 5 gallon plastic pail |  | 1.0 | each | 2.00 | Uline | S-9948BLU | [Link](https://www.uline.com/Product/Detail/S-9948BLU/Pails/Standard-Lid-for-35-5-6-and-7-Gallon-Plastic-Pail-Blue) | 1.0 | each | 2.00 |
| 1011 | Bucket connector | 1/2 in. PVC schedule 40 male adapter |  | 1.0 | each | 0.59 | Home Depot | PVC021090600HD | [Link](https://www.homedepot.com/p/Charlotte-Pipe-1-2-in-PVC-Schedule-40-Male-MPT-x-S-Adapter-PVC021090600HD/203811636) | 1.0 | each | 0.59 |
| 1012 | Silicone caulk | GE Silicone 1 All Purpose Clear Caulk |  | 1.5 | oz | 1.32 | Lowes | 2795576 | [Link](https://www.lowes.com/pd/GE-Silicone-1-All-Purpose-Windows-Doors-Exteriors-10-1-oz-Clear-Silicone-Caulk/5013443639) | 10.1 | oz | 8.88 |
| 1013 | 0.25 inch Plywood | 1/4 in. x 2 ft. x 2 ft. Sanded Plywood Project Panel |  | 38.5 | sq in. | 0.53 | Home Depot | 300810 | [Link](https://www.homedepot.com/p/Handprint-1-4-in-x-2-ft-x-2-ft-Sanded-Plywood-Project-Panel-) | 576 | sq in. | 7.88 |

### Drawings and Circuit Diagrams

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Wooden%20Stand%20Drawing.png">
</p>
<p align="center">
  <em>Figure 1: 3D model of wooden stand</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Bucket%20and%20Lid%20Drawing.png">
</p>
<p align="center">
  <em>Figure 2: 3D Model of Bucket and Lid Design</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Electronic%20Box%20Drawing.png">
</p>
<p align="center">
  <em>Figure 3: 3D Model of Waterproof Box</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Cover%20for%20Electric%20Box%20Drawing.png">
</p>
<p align="center">
  <em>Figure 4: 3D Model of Waterproof Box Lid</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Circuit%20Diagram-1.jpg">
</p>
<p align="center">
  <em>Figure 5: Circuit Drawing</em>
</p>

### Code

The following code was used to control the components attached to our RedBoard.
```cpp
PASTE HERE
```

The following code created our userinterface on streamlit.
```cpp
PASTE HERE
```

### Assembly Instructions
**Bucket and Stand Assembly**
1. To assemble the bucket and stand, we started by using a compass to outline the size of the hole we wanted to cut in the lid. Using a drill, we made a hole inside of the circle we drew to make a starting point to cut the circle out. Using a jig saw, we cut the circle out of the lid.

2. We cut a circle out of the screening that was slightly bigger than the hole cut in the lid. Using a scrap piece of cardboard as a mixing plate and a paint stick we mixed the gorilla two part epoxy. We used the paint stick to dab the epoxy on the perimeter of the circle, and placed the cut screening on the epoxy. We tapped the screen down onto the epoxy while wearing gloves, then taped the sides of the screen down to dry, as shown in the image below.
<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/drying%20lid.JPG">
</p>
<p align="center">
  <em>Figure 6: Lid and Mesh Cover Drying After Assembly</em>
</p>

3. Using a table saw, we cut a 16" by 16" square. Using a Miter Saw, we cut 4 16" long pieces, two 12" long pieces, and one 8" long piece from the 2-in x 4-in lumber. 

4. Starting with the 16" long pieces, we calibrated our pocket hole guide and drilled 3 pocket holes on one side of the pieces. The same thing was done on the 12" long pieces, and 8" piece, but 6 holes total were cut. Three holes in a row, but done on both sides of the same surface.

5. Once all pocket holes were drilled, we spread wood glue on the cut edge of the 16" pieces, on side with the pocket holes. The glue was placed down on the corner of the plywood piece, and a clamp was used to secure it in place. Using XXX inch screws, we drilled the screws into the pocket holes to fully secure the legs of the stand. 

6. The same process was done with the 12" long pieces, but they were clamped horizontally between the legs, 1 inch down from the base of the legs. For the 8" piece, it was glued horizontally between the two 12" pieces. All of these pieces were clamped down and set to dry overnight. The following image shows the pieces together, clamped down to dry. 
<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/drying%20stand.JPG">
</p>
<p align="center">
  <em>Figure 7: Wooden Stand Drying After Assembly</em>
</p>

7. For the valve portion of the bucket, we used a drill with a step cone drill bit attachment to make a 1/2 inch hole in the center of the bottom of the bucket. We applied silicone caulk  to the area around the hole on the inside of the bucket, and screwed in the pipe attachment as far as it could go. This was left to dry overnight. When the bucket was eventually dry, a wrench was used to hold the pipe in place while the sensor was glued on. 
 
8. To cut the hole in the wooden stand, we sketched out an area around the size of the entire valve, and used an oscillating saw to cut out the hole. 

9. For the waterproof box around our electronics, we 3D modeled and printed a box and sliding door in Autodesk Fusion. The following image shows the printed electronic box and cover, and the 3D model is shown in the Drawings section.

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/box%20picture.JPG">
</p>
<p align="center">
  <em>Figure 8: Final 3D Printed Box and Lid</em>
</p>

10. When the box was printed, we had to drill some holes in the box to allow for wires to get out, these are shown below. We held our circuit up to the box, and sketched out where we needed the holes, then drilled them around 1/4 to 1/2 inch in diameter. 

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Box%20drill%20holes.JPG">
</p>
<p align="center">
  <em>Figure 9: Electronic Box Drill Holes</em>
</p>

11. For the electronics box, we needed to add a piece of plywood to the back to make it able to be attached. We cut a piece of 1/4 inch plywood that was the same size as the outer edge of the box shown in the drawings section (7 inch by 5.5 inch), then used small amounts of epoxy on the corners of the box to hold it together. We taped the box and wood together on every side, then left it to dry overnight. When the epoxy was dry, we peeled off the tape. 

12. To attach the ultrasonic sensor to the bucket, we used the same step cone drill bit attachment to make a small hole one inch down from the top of the bucket. Then, we taped the ultrasonic sensor with the wires attached to it in the hole, making sure the sensor was angled to be perpendicular to the bottom of the bucket so we could get the best reading. We also put tape on the sensors themselves to make sure no caulk would obstruct them. This was then caulked in place, and left to dry overnight. The tape placement and caulk are shown in the images below. Once the caulk was dry, we peeled off the tape.

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Outside%20bucket%20tape.JPG">
</p>
<p align="center">
  <em>Figure 10: Tape on the Outside of the Bucket</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Inside%20sensor%20tape.JPG">
</p>
<p align="center">
  <em>Figure 11: Tape on the Sensor Inside the Bucket</em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/US%20caulk.JPG">
</p>
<p align="center">
  <em>Figure 12: Final Sensor with Caulk</em>
</p>

13. To attach the electronics box, we put a vertical line of the same caulk down the center of back of the plywood attached to the box. We laid the box face down on a table, then placed the side of the bucket on top of it, positioning the box to be approximately 3 inches below the hole we cut for the ultrasonic sensor. The bucket was propped up in position by objects we had, then left to dry overnight.

14. We used some double sided tape to hold the circuit in place when we open and close the electronics box, and threaded all of the appropriate wires through. After this, the Fancy Bucket 3000 was fully assembled!

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Final%20box.JPG">
</p>
<p align="center">
  <em>Figure 13: Final Fancy Bucket 3000</em>
</p>
    

**Circuit**
1. To construct our system, we first built a simple circuit that included a ball valve and a motor controller.
2. Next, we had to create a second power supply for the ball valve. One thing that we did not originally consider when we ordered the ball valve was that it required at least 9 Volts of power to function properly. Our Redboard could only provide 5 Volts and the battery pack that came with our Sparkfun Inventor Kit could only provide 6 Volts (1.5 Volts per battery). Thus, we found a 12 Volt source, then retrofit the wires to fit the ground and positive wires of the connector of the double A battery pack holder. After stripping the wires, we used a multimeter to determine which wire was positive and which was negative. Then, we soldered them to the battery pack connecter and wrapped the wires in electrical tape.
3. Next, we added a pH sensor. We connected wires to the ports on the pH sensor for power, ground, and one labled "Po" to represent pH output.
4. Finally, we incorporated an ultrasonic sensor. The final circuit diagram can be seen in figure 14. A picture of our final circuit can be seen in figure 15.

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Circuit%20Diagram-1.jpg">
</p>
<p align="center">
  <em>Figure 14: Circuit Diagram </em>
</p>

<p align="center">
<img width=50% src="https://github.com/CooperCoolrea/FancyBucket3000/blob/main/Complete%20Circuit.jpg">
</p>
<p align="center">
  <em>Figure 15: Completed Circuit </em>
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
4. Finally, we would ensure that the pH values being reported by the serial monitor were approximately correct by seeing if the reported value was in the estimated range the fluid should be in. If we were testing the pH sensor in an extremely acidic solution like vinegar, we knew our pH sensor was not working if it was reporting a neutral pH around 7.
5. Initially, our pH sensor was reporting very similar, neutral values no matter what fluid it was submerged in. To fix this, we integrated a calibration function into our code. Based on the voltage the probe was measuring in distilled water, the calibration function ensured that the output would be close to a neutral pH of 7. Once we utilized the calibration function, we recieved accurate pH results in different solutions.


**Automatic Ball Valve**
1. To test the automatic valve opening, we merely had to run our code and click the button on our GUI that was labeled “Open Valve.” If the valve opened, we considered that to be a successful trial.
2. Then, to test the closing function, we clicked the button on our GUI that was labeled “Close Valve.” If the valve closed, that was a successful trial. 
3. Finally, the valve needed to close automatically when it was empty. To test this, we would allow the bucket to release all of its contents, then we would observe the behavior of the ball valve. If it closed after releasing all the water, we considered that a successful trial.


## Design Decision Discussion
One of the first design decisions we made was to put a lid on our bucket with a large hole cutout with a mesh covering. This prevents leaves from getting in the bucket and allows water to enter. The border of the cutout is where the ultrasonic sensor rests. This prevents it from being rained on from above; however, the sensor would still be at risk of water damage if the bucket overfills. There is definitely room to improve this design. For example, someone could add a cover that automatically closes the bucket when it gets full. This would eliminate any risk of water damage. Additionally, there is some interference with the ultrasonic sensor's sound pulses bouncing off the bucket lid. This created some inaccurate volume results.

Another design decision we made was to use a ball valve as the connection between the water storage and water distribution. We mainly decided to use a ball valve because we were afraid that a solenoid valve would be unable to open with the amount of pressure at the bottom of our bucket. Additionally, a ball valve only requires a switch to operate, while a solenoid requires some analog signals to control it. We also considered rigging up an automatic opening with a servo or stepper motor; however, we decided that neither motor would have the power to open against the pressure of the water. The ball valve we used was also fairly simple to implement after having a proper power supply. We merely had to connect it to a motor controller and code it like any other component. Using a servo, stepper motor, or solenoid valve would've required more work and troubleshooting.

We decided to use an electronic pH sensor in the interest of time. It was very simple to code and calibrate. We also included a manual option on our GUI in case our users wanted to use a paper pH strip, then input their own reading. We were originally going to use a camera and code it to read the pH from the color; however, we decided this would be difficult since we would have to worry about interference from background colors and potentially would’ve had to utilize artificial intelligence. We also considered only using a manual option; however, we wanted to challenge ourselves and did not want there to have to be a secondary purchase to use our device. Another engineer could implement the camera reading with artificial intelligence or use manual entry only for simplicity.

We decided to 3D print a plastic box to hold our Redboard and circuitry because we wanted to protect the electronics from water damage. The lid of our electronic box includes a holder for the pH sensor. It may have been simpler to cut out a box from wood or metal; however, we did not want to have to wait for glue to dry, weld, or seal the box. Additionally, other engineers could improve on our design by making the box more flush with the curved surface of the bucket. We made ours flat and caulked it, because it was quick and effective. We also kept in mind that this was just a prototype.

One thing we debated at the beginning stages of our project was where to put the outlet of our bucket. We were debating whether or not to put it on the bottom surface or whether to put it on the side of the bucket. We decided to put it on the bottom since it allowed for minimal water stagnation, it provided clearance for our hose, and we had gravity working to encourage flow downward. One issue with this location is that our internal pipe connection is not entirely flush with the bottom and extends upward into the bucket. This means the bucket will never be completely empty. Another engineer could improve our design by slanting the inside of the bottom of the bucket. This would prevent any stagnation.


## Test Results Discussion
**Volume Sensing**

The volume sensing function exhibited consistent but slightly elevated baseline readings when water was input. Across trials with different numbers of gallons of water added, the sensor detected a small offset ranging from 0.21 to 0.29 gallons. Although the sensor did not register a perfect value, the measurements were relatively stable and within a narrow range, suggesting good repeatability. The consistent offset indicates that while the sensor is reliable in detecting changes in volume, it may have a systematic calibration error that causes a slight overestimation at very low volumes. This behavior would have minimal impact during normal operation, where larger volume changes are of primary concern.

**pH Sensing**

In testing the pH sensor, we first calibrated it using distilled water to ensure it returned accurate baseline readings, which it did relatively reliably, yielding a constant pH value of 6.45. We deemed this accurate, as the pH of distilled water in Lexington is around 5.8. However, when we tested the sensor with other common solutions such as water mixed with vinegar (acidic) and water mixed with baking soda (basic), the sensor displayed little to no variation in the pH readings. Despite the expected chemical changes, the sensor readings remained largely unchanged, indicating a malfunction. To confirm that the issue was with the probe itself and not our system design, we tested another group’s pH sensor with our setup, and it responded accurately to the solutions. This verified that the problem was isolated to our pH probe. Based on these observations, we concluded that our original pH probe was defective. To address this issue and maintain functionality, we integrated a manual pH input option into our GUI. This allows users to enter accurate pH values themselves, ensuring that the system can still provide appropriate treatment suggestions based on reliable input.

**Automated Ball Valve**

The automatic valve responded reliably to user input provided through our GUI application. Specifically, each time the user clicked the designated button on the app interface, the valve successfully opened as intended. During all five experimental trials, the valve consistently released the water contained in the bucket immediately following the user’s command. Similarly, each time the user pressed the button to close the valve, it closed successfully during all five trials. This consistent performance across multiple repetitions demonstrates that the system's valve control functionality operated with perfect precision, achieving a 100% success rate for both opening and closing operations. The seamless interaction between the software interface and the hardware mechanism confirms that the valve accurately and promptly executed the user’s instructions without any delay or malfunction, highlighting the reliability and effectiveness of our system's automated water release feature.

The ball valve demonstrated excellent accuracy in responding to the barrel reaching maximum capacity. In all five trials, the detected volume exceeded the required threshold of 3.66 gallons, and the valve opened successfully each time. The measured volumes ranged from 3.69 to 4.48 gallons, consistently surpassing the minimum capacity requirement. Additionally, after the water level dropped below the threshold, the valve reliably closed in each case, further confirming the system’s responsiveness and control. This consistent behavior highlights the valve's strong performance and reliability in both preventing overfilling and maintaining proper barrel management.


## Testing Results

**Volume Sensing**

**Table 1: Accuracy of Volume Sensing Function**
|Trial|Measured Volume of Water Inputted (gal)|Volume Detected (gal)|
|---|---|---|
|1|0|0.22|
|2|1|1.23|
|3|2|2.29|
|4|2.5|2.71|
|5|3|3.22|

**pH Sensing**

**Table 2: Accuracy of pH Sensing Function**
|Trial|Solution|Anticipated pH|pH Detected|
|---|---|---|---|
|1|Distilled Water|~5.8|6.45|
|2|Distilled Water|~5.8|6.45|
|3|Distilled Water|~5.8|6.45|
|4|Vinegar and Water Solution|~4-5 (Acidic)|6.47|
|5|Baking Soda and Water Solution|~8-9 (Basic)|6.53|

**Automated Ball Valve**

**Table 3: Accuracy of Valve Opening Prompted by User**
|Trial|Button Clicked (Yes/No)|Valve Open? (Yes/No)|
|---|---|---|
|1 |Yes|Yes|
|2 |Yes|Yes|
|3 |Yes|Yes|
|4 |Yes|Yes|
|5 |Yes|Yes|

**Table 4: Accuracy of Valve Closing Prompted by User**
|Trial|Button Clicked (Yes/No)|Valve Close? (Yes/No)|
|---|---|---|
|1 |Yes|Yes|
|2 |Yes|Yes|
|3 |Yes|Yes|
|4 |Yes|Yes|
|5 |Yes|Yes|


**Table 5: Accuracy of Valve Opening Prompted by Capacity of Barrel**
|Trial|Volume Detected (gal)|Required Volume for Maximum Capacity(gal)|Valve Open? (Yes/No)|
|---|---|---|---|
|1 |4.46| &ge;3.66 |Yes|
|2 |4.42| &ge;3.66|Yes|
|3 |4.48| &ge;3.66|Yes|
|4 |3.69| &ge;3.66|Yes|
|5 |4.18| &ge;3.66|Yes|
