# FancyBucket3000

## Summary of Project
The Fancy Bucket 3000 is a rain collection system with volume sensing, pH sensing, and an automatic valve opening for irrigation systems. This system utilizes an ultrasonic sensor to determine when the rain barrel is getting full and will notify the user that water testing needs to be done before releasing the water to the plants. We integrated a digital pH sensor to report the acidity of the water to the user and recommend treatments if necessary. Once the user tells the system the water is treated by pushing a button on our UI, our system opens a ball valve to release the water to the irrigation system. This system will consist of piping from the Fancy Bucket 3000 to a prepared trough with soil and plants. Our project is fully operational and meets all outputs listed in the project initiation.

## Design Description
### Materials


**Part 2: Prompt 2**


|Part Number|Part Name| Description| Notes|Quantity|Units|Total Cost| Supplier| Supplier Part Number|Link|Package Size|Unit|Package price|
|--------------:|:-----------------|:----------------------------------------------------------------------|:-----------------------------------------|-----------:|:--------|-------------:|:-----------|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------:|:-------|----------------:|
|          1001 | Plastic Bucket   | 5-Gallon, HDPE                                                        | Comes with wire handle                   |     1      | each    |     3.73     | Menards    | 6482910                | [Bucket](https://www.menards.com/main/grocery-home/cleaners-household-essentials/cleaning-supplies/cleaning-tools/menards-reg-5-gallon-bucket/6482910/grocery-home/cleaners-household-essentials/cleaning-supplies/cleaning-tools/menards-reg-5-gallon-bucket/6482910/p-1444426310607-c-7113.htm)                                                                                                                                                                                                                                                                                                                                                               |           1    | each   |            3.73 |
|          1002 | pH sensor        | Teyleten pH detection sensor                                          | arduino compatible                       |     1      | each    |    18.99     | Amazon     | B09H1MJS4S             | [pH sensor](https://www.amazon.com/Teyleten-Robot-Acquisition-Alkalinity-Monitoring/dp/B09H1MJS4S/ref=sr_1_2?dib=eyJ2IjoiMSJ9.1CFYrYmmcpKNrIxjOmnX0jffglTHVM5b1Sw7TQZ0C8iBDQva5o6iGQsHBYegwtwWgUMbXYczJIpeFFFHm46cGa-RjiEleI7itIyUbvrrwtDTOh1kT09xJL-V_WJEAcmFho-56USq_9MMl0m6zUOtqJMfBNnrkEgah9K8reQq5lwVzyUeltDdtuLla0ei-x8I0g7hMQ4JqAEq83LOtwd_cKHGH0HOZzL0g93mE49XjE0.VaExV-hyRNdhqRwpgumMF3KMSi-lM_ih4i1tUKGTp14&dib_tag=se&hvadid=570508181467&hvdev=c&hvlocphy=9014313&hvnetw=g&hvqmt=e&hvrand=16108112357600221948&hvtargid=kwd-35578094204&hydadcr=19107_13375052&keywords=arduino+ph+sensor&mcid=e6ad8d63010f3e7a934b59b68e11023c&qid=1743538671&sr=8-2) |           1    | each   |           18.99 |
|          1003 | wood glue        | Gorilla Wood Glue                                                     | nan                                      |     0.12   | fl oz.  |     0.1191   | Home Depot | 62020                  | [Wood Glue](https://www.homedepot.com/b/Paint-Paint-Supplies-Adhesives-Wood-Adhesive/N-5yc1vZ2fkoqdc?NCNI-5&searchRedirect=Wood%20glue&semanticToken=j10r10r10f22040000000e_202504012025459300622023459_us-central1-vmpc%20j10r10r10f22040000000e%20%3E%20st%3A%7BWood%20glue%7D%3Ast%20ml%3A%7B24%7D%3Aml%20ct%3A%7Bwood%20glue%7D%3Act%20nr%3A%7Bwood%20glue%7D%3Anr%20nf%3A%7Bn%2Fa%7D%3Anf%20qu%3A%7Bwood%20glue%7D%3Aqu%20ie%3A%7B0%7D%3Aie%20qr%3A%7Bwood%20glue%7D%3Aqr)                                                                                                                                                                                    |           4    | fl oz. |            3.97 |
|          1004 | Ball Valve       | U.S. Solid Motorized Ball Valve- 1/2" Brass Ball Valve with Full Port | 9-24V AC/DC and 2 Wire Auto Return Setup |     1      | Each    |    34.02     | Amazon     | ANSI B16.34, IP65      | [Valve](https://www.amazon.com/Motorized-Valve-Return-U-S-Solid/dp/B06X9LWXMW/ref=sr_1_1_sspa?crid=3L8BVQ91X8O9S&dib=eyJ2IjoiMSJ9.BjAevbtx9WhAr5N7n-k1mwckuNmWSGIyKhG3s10rct1P6Ua2RoU-5Wzr_G6QTNoPG_VLtTVrl5tz7qs2B-ujtpNnakj-xdV5qHcQFEG04WNfDBqzjLInA0K4Mlb2Y54GzroJuos1ZT_olGD4B6inmqPmFr0xT56jaY4zMibyADr0yXDzVe-8o3j87ELtRUlNNpsK1EsX_SYsGfCwphbQCSi0iPjccTF5_X6JDMRWvqc.A3CoWLrXv5Rym1J3seuVb_8dcP3LDdDIo741wdYpZiE&dib_tag=se&keywords=us%2Bsolid%2Bmotorized%2Bball%2Bvalve&qid=1744654932&sprefix=us%2Bsolid%2Bmotorized%2Bball%2Bvalve%2Caps%2C75&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1)                                                  |           1    | Each   |           34.02 |
|          1005 | Hose             | 1/2" Hose Assembly                                                    | with male NPT X male NPT 5220 PSI (24")  |     1      | each    |    25.58     | Amazon     | 850057403343           | [Hose](https://www.amazon.com/Assembly-Hose-male-NPT-24/dp/B0CYQH7GM3/ref=asc_df_B0CYQH7GM3?mcid=f362d4a1c51b37ccad5cae2c5e60a6a3&hvocijid=1449949630395530453-B0CYQH7GM3-&hvexpln=73&tag=hyprod-20&linkCode=df0&hvadid=721245378154&hvpos=&hvnetw=g&hvrand=1449949630395530453&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9014318&hvtargid=pla-2281435178138&th=1)                                                                                                                                                                                                                                                                          |           1    | Each   |           25.58 |
|          1006 | Plywood          | 3/4 inch thick, sanded plywood                                        | nan                                      |   225      | Sq in   |     4.66602  | Home Depot | 205960                 | [Plywood](https://www.homedepot.com/p/Handprint-3-4-in-x-2-ft-x-4-ft-Pressure-Treated-Plywood-Project-Panel-205960/205603712)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |        1152    | Sq in  |           23.89 |
|          1007 | Porch screening  | Charcoal fiberglass screen roll                                       | nan                                      |    33.1831 | sq in   |     0.262151 | Home Depot | FCS10396-M             | [Mesh Screen](https://www.homedepot.com/pep/Saint-Gobain-ADFORS-36-in-x-84-in-Charcoal-Fiberglass-Clear-Advantage-Screen-Roll-for-Windows-and-Door-FCS10396-M/203176333?source=shoppingads&locale=en-US&pla&mtc=SHOPPING-BF-CDP-GGL-D30-030_023_GLASS_SCREEN-NA-NA-NA-PMAX-NA-NA-NA-NA-NBR-NA-NA-NEW-NA&cm_mmc=SHOPPING-BF-CDP-GGL-D30-030_023_GLASS_SCREEN-NA-NA-NA-PMAX-NA-NA-NA-NA-NBR-NA-NA-NEW-NA-20845711144--&gad_source=1&gclid=Cj0KCQjwqv2_BhC0ARIsAFb5Ac_nj4lNMFeHQmmr9335HjKUddwvHyaFdMRQF9wpi6CyyLSWIIyagLEaAiWKEALw_wcB&gclsrc=aw.ds)                                                                                                                   |        3024    | sq in  |           11.48 |
|          1008 | 2.5 inch screws  | Coarse zinc-plated steel square-head pocket screw                     | nan                                      |    16      | each    |     2.7104   | Home depot | SML-C250-50            | [2.5 inch screw](https://www.homedepot.com/p/Kreg-2-1-2-in-Coarse-Zinc-Plated-Steel-Square-Head-Pocket-Screw-50-Pack-SML-C250-50/205377485)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |          50    | each   |            8.47 |
|          1009 | 1.25 inch screws | Square maxi-Loc head coarse zinc-plated steel pocket-hole screw       | nan                                      |    12      | each    |     1.1364   | Home depot | SML-C125-100           | [1.25 inch screw](https://www.homedepot.com/p/Kreg-8-1-1-4-in-Square-Maxi-Loc-Head-Coarse-Zinc-Plated-Steel-Pocket-Hole-Screw-100-Pack-SML-C125-100/100572559?MERCH=REC-_-fbt_test-_-205377485-_-3-_-n/a-_-n/a-_-n/a-_-n/a-_-n/a)                                                                                                                                                                                                                                                                                                                                                                                                                                        |         100    | each   |            9.47 |
|          1010 | Epoxy            | Gorilla Clear Epoxy Adhesive                                          | nan                                      |     0.85   | fl oz.  |     7.48     | Lowes      | 13111000               | [Epoxy](https://www.lowes.com/pd/Gorilla-Epoxy-Clear-Epoxy-Adhesive/5002785627?store=607&cm_mmc=shp-_-c-_-prd-_-pnt-_-ggl-_-PMAX_PNT_000_Priority_Item-_-5002785627-_-local-_-0-_-0&gad_source=1&gclid=Cj0KCQjwqv2_BhC0ARIsAFb5Ac_pwwRUqPJZTI_g4-Brf3jD691PNHaQcOlJzuZ9Hb11_ngmyS-yJZAaArdiEALw_wcB&gclsrc=aw.ds)                                                                                                                                                                                                                                                                                                                                              |           0.85 | fl oz. |            7.48 |
|          1011 | Bucket lid       | Standard lid for 5 gallon plastic pail                                | nan                                      |     1      | each    |     2        | Uline      | S-9948BLU              | [Bucket Lid](https://www.uline.com/Product/Detail/S-9948BLU/Pails/Standard-Lid-for-35-5-6-and-7-Gallon-Plastic-Pail-Blue)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |           1    | each   |            2    |

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

7.XXXXXXXXXXXXXXXXXXXXX

**Circuit**
1. To construct our system, we first built a simple circuit with a ball valve and a motor controller. The circuit diagram can be seen in figure ___. One thing that we did not originally consider when we ordered the ball valve was that it required at least 9 Volts of power to function properly. Our Redboard could only provide 5 Volts and the battery pack that came with our Sparkfun Inventor Kit could only provide 6 Volts (1.5 Volts per battery). Thus, we had to ________________. After stripping the wires, we soldered them to _____, then added electrical tape _____.
2. Next, we added a pH sensor. The circuit diagram with the pH sensor included can be seen in figure ___.
3. Finally, we incorporated an ultrasonic sensor. The circuit diagram for the ultrasonic sensor can be seen in figure _____. A picture of our final build can be seen in figure ________.

**Software and GUI**
1. 



## Testing Description
### Test Equipment
* Cups of water from different sources

### Testing Procedures
Could another test engineer replicate your tests?
All test equipment specified (model numbers) and procedures fully described

**Volume Sensing**
1. To test if the ultrasonic sensor was working correctly and that our GUI was showing the correct volume, we would first fill our bucket to any depth.
2. Then, we would measure the depth and multiply that depth by the cross sectional area of the bucket. 
3. Finally, we would run our code and see if the volume value it was reporting was approximately the same as the calculated value. We allowed it to be incorrect by _____.


**pH Sensing**
1. To test the pH sensor, we filled cups with fluids that had different pH values. 
2. Then we would remove the pH sensor from its cover and insert it into the different fluids.
3. Finally, we would ensure that the pH values being reported by the serial monitor were approximately correct. We merely ensured that anything that was in its estimated range. If we were testing the pH sensor in an extremely acidic solution, we knew our pH sensor was not working if it was reporting an almost neutral solution.
4. Initially, our pH sensor was reporting very similar, neutral values no matter what fluid it was submerged in. To fix this, we changed the calibration in our code ______________.


**Automatic Ball Valve**
1. To test the automatic valve opening, we merely had to run our code and click the button on our GUI that was labeled “___________.” If the valve opened, we considered that to be a successful trial.
2. Then, to test the closing function, we clicked the button on our GUI that was labeled “______.” If the valve closed, that was a successful trial. 
3. Finally, the valve needed to close automatically when it was empty. To test this, we would allow the bucket to release all of its contents, then we would observe the behavior of the ball valve. If it closed after releasing all the water, we considered that a successful trial.


## Design Decision Discussion
Could competent engineer build on top of your design with modifications to provide different capabilities?
Design decisions are described completely. This is an excellent reference design for this type of system

One of the first design decisions we made was to put a lid on our bucket with a large hole cutout with a mesh covering. This prevents leaves from getting in the bucket and allows water to enter. The border of the cutout is where the ultrasonic sensor rests. This prevents it from being rained on from above; however, the sensor would still be at risk of water damage if the bucket overfills. There is definitely room to improve this design. For example, someone could add a cover that automatically closes the bucket when it gets full. This would eliminate any risk of water damage. We would have probably included this in our design if we were not limited on time.

Another design decision we made was to use a ball valve as the connection between the water storage and water distribution. We mainly decided to use a ball valve because we were afraid that a solenoid valve would be unable to open with the amount of pressure at the bottom of our bucket. We also considered rigging up an automatic opening with a servo or stepper motor; however, we decided that neither motor would have the power to open against the pressure of the water. The ball valve we used was also fairly simple to implement __________.

We decided to use an electronic pH sensor in the interest of time. It was very simple to code and calibrate. We also included a manual option on our GUI in case our users wanted to use a paper pH strip, then input their own reading. We were originally going to use a camera and code it to read the pH from the color; however, we decided this would be difficult since we would have to worry about interference from background colors and potentially would’ve had to utilize artificial intelligence. We also considered only using a manual option; however, we wanted to challenge ourselves and did not want there to have to be a secondary purchase to use our device. Another engineer could implement the camera reading or ____.

We decided to 3D print a plastic box to hold our Redboard and circuitry because we wanted to protect the electronics from water damage. The lid of our electronic box includes a holder for the pH sensor. It may have been simpler to cut out a box from wood or metal; however, we did not want to have to wait for glue to dry, weld, or seal the box. Additionally, other engineers could improve on our design by making the box more flush with the curved surface of the bucket. We made ours flat and caulked it, because it was quick and effective. We also kept in mind that this was just a prototype.

One thing we debated at the beginning stages of our project was where to put the outlet of our bucket. We were debating whether or not to put it on the bottom surface or whether to put it on the side of the bucket. We decided to put it on the bottom since _________. One issue with this location is that our pipe connection is not flush with the bottom and extends upward into the bucket. This means the bucket will never be entirely empty. Another engineer could improve our design by slanting the inside of the bottom of the bucket. This would prevent any stagnation.

## Testing Results Discussion
Are the capabilities of the system described? Where would this design work? How well does it work? What are its limitations? What can it not do?
It is clear what the system can do, cannot do, and where it works best

## Testing Results
Were the test results described correctly? Were the proper tests performed to measure system capabilities?
Proper tests were conducted and results clearly documented
