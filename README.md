# Hair-conductor-for-corridor-geometry
This is a script for Blender 3d 2.8 to create a geometry of hair in shape
____
I don’t know if I will do anything else (there is no way to make support for the particles of hair yet). 
The plans: 
-The generation of a new object for the hair mesh. 
-Selection, mesh generation of an object or vector. 
-The ability to generate bones according to the plan of the hair frame. 
-Auto link vertex weights to the new skeleton. 
-Add a bezier curve to position hair points. 
-Adding a menu to create a full add-on.




# Addon for Blender 2.8 Hair Explorer.
The main function - makes hair styling according to your corridor geometry.

# Using:
*1 Call the Generate Hair by object function (from a space search or the Object fold) (An object for building hair should be selected).
*2 In the operator (a new menu on the screen), select (using the left-right buttons) the vertex group with which you marked the base of the hair.
*3 Press the button to build a hair plan (this may take some time. For safety, you will be shown a console with a report.) (Buildings are needed to interpret your geometry into a simple view that can be used for laying hair).
*4 Management of hair through settings in real time (due to the way the menu is created, it is necessary to manually update the parameters additionally, after introduction).

# Hair geometry requirements:
*Strictly 4x carbon tube.
*The ends are filled.
*No holes or tears.
*The whole number of rings.
*Only a polygon has a group of vertices - the base.
*The material for this pipe is assigned to the landfill.
*The aspect ratios of the base and scale affect the layout and amount of hair.
*Separate pipes must not be connected.
*Modifiers are not taken into account.
*The object should not be rotated, scaled, have a parent.

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/731649425130127420/1.png "One hair element cutaway")


# Supported features:
*View of the object (the object is initially visible / render material, the object is a grid, the overlay is off.)
**One or more types of hair at the same time.
**Hair type may be:
***Object Type (Geometry / Curve)
****Division Method (Do not divide objects by different materials / divide all / select only 1)
****For a curve, the width of the root.
****The amount of hair in the type (the scale of the hair bases is taken into account).
****Subdivision.
****Smoothing (Without / Bezier 1)
****Switched off.
****The noise of the hair position.
****Hair Size (Width)
****The randomizer is long:
****The maximum length of hair.
****Minimum hair length.
****Scatter (1 - no, 0 or 2 - closer to something)
# Not supported:
*Shelves of deformers (noise) - not supported yet.
*Skeleton generation (and harness) - not yet started.

# Testing:
[![Тут текст](https://cdn.discordapp.com/attachments/340195875399663617/731656260935614525/unknown.png)](https://cdn.discordapp.com/attachments/474472368706945024/731236109610385549/2020-07-10_22-46-10_convert-video-online.com.mp4)
[![Тут текст](https://cdn.discordapp.com/attachments/340195875399663617/731656260935614525/unknown.png)](https://cdn.discordapp.com/attachments/324814768152248323/731557262295957534/2020-07-11_20-03-58.mp4)
[![Тут текст](https://cdn.discordapp.com/attachments/340195875399663617/731656260935614525/unknown.png)](https://cdn.discordapp.com/attachments/324814768152248323/731642313515991110/2020-07-12_01-44-22.mp4)

# I want it:
*Get the folder.
*Open blender
*User settings
*Addons
*Open
*Folder
*HairAddonTest.py
*Activate.
____
 *The addon is still at an early stage of development. I'm not a mater of Python. The code has 2 clockless cycles, object-oriented programming is ignored, all the features of the language and bpy are not used, there is a lot of garbage text, there is no translation.
