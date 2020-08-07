# Addon for Blender 2.8 Hair Conductor.

**The main function**: 
makes hair styling according to your corridor geometry.

**Using**: 
 - 1 Call the Generate Hair by object function (from a space search or the Object fold) (An object for building hair should be selected).
 - 2 In the operator (a new menu on the screen), select (using the left-right buttons) the vertex group with which you marked the base of the hair.
 - 3 Press the button to build a hair plan (this may take some time. For safety, you will be shown a console with a report.) (Buildings are needed to interpret your geometry into a  simple view that can be used for laying hair).
 - 4 Management of hair through settings in real time (due to the way the menu is created, it is necessary to manually update the parameters additionally, after introduction).

**Usage example**: 
 - Hair geometry requirements:
 - Strictly 4x carbon tube.
 - The ends are filled.
 - No holes or tears.
 - The whole number of rings.
 - Only a polygon has a group of vertices - the base.
 - The material for this pipe is assigned to the base.
 - The aspect ratios of the base and scale affect the layout and amount of hair.
 - Separate pipes must not be connected.
 - Modifiers are not taken into account.
 - The object should not be rotated, scaled, have a parent.
 - The object must have at least 1 material
![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/731649425130127420/1.png "One hair element cutaway")

**Supported features**: 
 - View of the object (the object is initially visible / render material, the object is a grid, the overlay is off.)
 - One or more types of hair at the same time.
 - Hair type may be:
 - Object Type (Geometry / Curve)
 - Division Method (Do not divide objects by different materials / divide all / select only 1)
 - For a curve, the width of the root.
 - The amount of hair in the type (the scale of the hair bases is taken into account).
 - Subdivision.
 - Smoothing (Without / Bezier 1)
 - Switched off.
 - The noise of the hair position.
 - Hair Size (Width)
 - The randomizer is long:
 - The maximum length of hair.
 - Minimum hair length.
 - Scatter (1 - no, 0 or 2 - closer to something)
 - Shelves of deformers (noise).
 - Not supported:
 - Skeleton generation (and harness) - not yet started.

**Demonstration of the finished result**: 
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/029/099/810/large/mod-____-man-1-1-2.jpg?1596463522 "One hair element cutaway")
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/029/099/814/large/mod-____-man-1-1-3.jpg?1596463531 "One hair element cutaway")
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/029/102/674/large/mod-____-girl-1-1-2.jpg?1596469609 "One hair element cutaway")
![Alt-текст](https://cdnb.artstation.com/p/assets/images/images/029/102/671/large/mod-____-girl-1-1-3.jpg?1596469594 "One hair element cutaway")
![Alt-текст](https://cdnb.artstation.com/p/assets/images/images/028/696/445/large/mod-____-render-test-1-1-1.jpg?1595249808 "One hair element cutaway")
![Alt-текст](https://cdnb.artstation.com/p/assets/images/images/028/696/463/large/mod-____-render-test-1-2-1.jpg?1595249822 "One hair element cutaway")
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/028/791/780/large/mod-____-srgvzsaerv-1-1-1.jpg?1595518164 "One hair element cutaway")
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/028/791/788/large/mod-____-srgvzsaerv-1-2-1.jpg?1595518172 "One hair element cutaway")
![Alt-текст](https://cdnb.artstation.com/p/assets/images/images/028/791/795/large/mod-____-srgvzsaerv-1-3-1.jpg?1595518179 "One hair element cutaway")
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/028/791/804/large/mod-____-srgvzsaerv-1-4-1.jpg?1595518187 "One hair element cutaway")
![Alt-текст](https://cdnb.artstation.com/p/assets/images/images/028/791/823/large/mod-____-srgvzsaerv-1-6-1.jpg?1595518201 "One hair element cutaway")
![Alt-текст](https://cdna.artstation.com/p/assets/images/images/028/791/832/large/mod-____-srgvzsaerv-1-7-1.jpg?1595518208 "One hair element cutaway")
![Alt-текст](https://cdnb.artstation.com/p/assets/images/images/028/791/839/large/mod-____-srgvzsaerv-1-8-1.jpg?1595518216 "One hair element cutaway")

**Addon Discussion Location**:
- https://blenderartists.org/t/addon-hair-conductor-blender-2-8/1242182

**I want it**: 
 - Get the ZIP/
 - Open blender/
 - User settings/
 - Addons/
 - Open/
 - This add-on/
 - Activate/
 - View3D/
 - Object/
 -Generate Hair by object.
____
# The addon is still at an early stage of development. I'm not a mater of Python. Object-oriented programming is ignored, all the features of the language and bpy are not used, there is a lot of garbage text, there is no translation.
