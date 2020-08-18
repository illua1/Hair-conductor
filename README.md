# Addon for Blender 2.8 Hair Conductor.

**The main function**: 
Makes hair styling according to your corridor geometry.

**Using**: 
 - 1 Call the Generate Hair by object function (from a space search or the Object fold) (An object for building hair should be selected).
 - 2 In the operator (a new menu on the screen), select (using the left-right buttons) the vertex group with which you marked the base of the hair.
 - 3 Press the button to build a hair plan (this may take some time. For safety, you will be shown a console with a report.) (Buildings are needed to interpret your geometry into a  simple view that can be used for laying hair).
 - 4 Management of hair through settings in real time (due to the way the menu is created, it is necessary to manually update the parameters additionally, after introduction).

<details>
  <summary>Hair geometry requirements:</summary>

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

</details>

<details>
  <summary>Supported features: </summary>

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
 - Skeleton generation (and harness).
 - Saving and loading addon session.
 - Tool for edit-mode tool - Hair Selecter Floor.
 - Tool for edit-mode tool - Hair Loop Cut Floors.

</details>

<details>
  <summary>Demonstration of the finished result: </summary>

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

</details>

**Addon Discussion Location**:
- https://blenderartists.org/t/addon-hair-conductor-blender-2-8/1242182

<details>
  <summary>#I want it: </summary>

 - Get the ZIP/
 - Open blender/
 - User settings/
 - Addons/
 - Open/
 - This add-on/
 - Activate/
 
 </details>
 
<details>
  <summary>Start use: </summary>

- What do you want

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745364795779317861/first_1-8-1.png "What do you want")

- Materials required

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745364797687595028/first_1-8-2.png "Materials required")

- Select a root group

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745364798899749034/first_1-8-3.png "Select a root group")

- Cause Mapping

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745364801114603640/first_1-8-4.png "Cause Mapping")

- Create your first hair

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745364803349905560/first_1-8-5.png "Create your first hair")

- To add your hair to the save list, click this

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745364806525124718/first_1-8-6.png "To add your hair to the save list, click this")

</details>

<details>
  <summary>Hair preset: </summary>

  <details>
    <summary>    See the geometry of the map</summary>

 - Don't see the geometry of the map 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368401761009694/first_1-9-1.png "See the geometry of the map")

 - See the geometry of the map

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368402712854609/first_1-9-2.png "Don't see the geometry of the map")

</details>

<details>
  <summary>    Switch hair type</summary>

 - Switch hair type: curve 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368404952743936/first_1-9-3.png "Switch hair type: mesh")

 - Switch hair type: mesh

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368407473651762/first_1-9-4.png "Switch hair type: curve")

</details>

<details>
  <summary>    Split by materials</summary>

 - Do not split by materials

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368411495727107/first_1-9-5.png "Do not split by materials")

 - Split all materials

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368414708826122/first_1-9-6.png "Split all materials")

 - Select 1 material

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368414708564028/first_1-9-7.png "Select 1 material")

 - Select 1 material

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745368416633749556/first_1-9-8.png "Select 1 material")

</details>

<details>
  <summary>    Length range</summary>

 - Scatter location 1.

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374827312840854/first_1-10-1.png "Scatter location 1.")

 - Scatter location 2.

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374829099745280/first_1-10-2.png "Scatter location 2.")

 - Scatter location 0.

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374830538522714/first_1-10-3.png "Scatter location 0.")

 - High minimum

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374832530555010/first_1-10-4.png "High minimum")

</details>

<details>
  <summary>    Hair width</summary>

 - Large width

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374835076497498/first_1-11-1.png "Large width")

 - Small width

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374837001945501/first_1-11-2.png "Small width")

</details>

<details>
  <summary>    Hair scatter</summary>

 - The spread is high

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374838830399548/first_1-11-3.png "The spread is high")

 - Low spread

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745374840629887097/first_1-11-4.png "Low spread")

</details>

<details>
  <summary>    Dynamic number of vertices</summary>

 - Dynamic number of vertices taking into account length

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377207798595694/first_1-11-5.png "Dynamic number of vertices taking into account length")

 - Constant length

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377208331403304/first_1-11-6.png "Constant length")

</details>

<details>
  <summary>    Count of preset</summary>

 - 2 different presets created

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377211145650178/first_1-12-1.png "2 different presets created")

 - All presets disabled

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377212433301615/first_1-12-2.png "All presets disabled")

 - Preset 1 only

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377214316544011/first_1-12-3.png "Preset 1 only")

 - Preset 2 only

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377216124158012/first_1-12-4.png "Preset 2 only")

 - Record of the number of different presets

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745377218384887848/first_1-12-5.png "Record of the number of different presets")
</details>
</details>

<details>
  <summary>Use Of Deformers: </summary>

No deformers 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006060909232219/first_1-1-1.png "No deformers")

<details>
  <summary>    UVZ noise</summary>

**Type**: Noise in hair space : 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006064189046874/first_1-2-1.png "Noise in hair space")

 - The size

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006067578175590/first_1-2-2.png "The size")

 - Drop

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006070820372540/first_1-2-3.png "Drop")

</details>

<details>
  <summary>    XYZ noise</summary>

**Type**: Coordinate noise : 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006074742177912/first_1-3-1.png "Coordinate noise")

 - Power

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006076528951387/first_1-3-2.png "Power")

 - The size

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006103720362126/first_1-3-3.png "The size")

 - Drop

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006106580877343/first_1-3-4.png "Drop")

</details>

<details>
  <summary>    Voronoise</summary>

**Type**: Voronoise (clusters) : 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006111022907482/first_1-4-1a.png "Voronoise clusters")

 - Power

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006113216397352/first_1-4-2a.png "Power")

 - The size

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006116206936134/first_1-4-3a.png "The size")

 - Drop

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006120275410994/first_1-4-4a.png "Drop")

</details>

<details>
  <summary>    Resize</summary>

**Type**: Size (in width) : 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006143977553971/first_1-5-1.png "Size (in width)")

 - Size vector

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006146372501544/first_1-5-2.png "Size vector")

 - The size

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006150096912384/first_1-5-3.png "The size")

 - Drop

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006154400399580/first_1-5-4.png "Drop")

</details>

<details>
  <summary>    Rotate</summary>

**Type**: Rotation (To lenght) : 

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006158015889480/first_1-6-1.png "Rotation (To lenght)")

 - Power

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006161157423184/first_1-6-2.png "Power")

 - The size

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006180665131238/first_1-6-3.png "The size")

 - Drop

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006181684215938/first_1-6-4.png "Drop")

</details>

Combination example

![Alt-текст](https://cdn.discordapp.com/attachments/340195875399663617/745006184716566579/first_1-7-1.png "Combination example")

</details>

 **Warning**:
 - Extreme parameters, such as the amount of hair or their fragmentation, can not only make you wait a long time for the result, but also destroy your memory! both graphics card and RAM, if you're not careful, you can lose your blender session.
 - If you are using this hair for rendering, then you are using curves, but it is not hair! and if you render them in cycles you could lose your computer to gpu! Don't risk it! Use eevee!
____
# The addon is still at an early stage of development. I'm not a mater of Python. Object-oriented programming is ignored, all the features of the language and bpy are not used, there is a lot of garbage text, there is no translation.
