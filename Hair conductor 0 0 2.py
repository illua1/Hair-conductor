


#Code editing license.
#-You can change the code for personal use.
#-You can transfer modified code when mentioning the fact of editing, the user of the editor and the author of the add-on.
#-You cannot sell a modified addon.
#-You cannot use parts of the addon code for commercial purposes.



bl_info = {
    "name": "Hair conductor",
    "description": "testing v0.0.2",
    "author": "Mod",
    "version": (0, 0, 2),
    "blender": (2, 80, 0),
    "location": "View3D > Object > Generate Hair by object",
}

import bpy
import math
import HairConductorSets.HairAddonBody 
import HairConductorSets.Buttons
from HairConductorSets.Hairtextblock import OperatorText
from HairConductorSets.Hairtextblock import DeformNames

def AddHairPreset(h) :
    return h.append( [ ["vertex",-1], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ], 1,1.,0.01,1,0, 0 ] );
def DelHairPreset(h, id) :
    if id < len(h):
        del h[id];
    return h;

def AddBonePreset(h) :
    return h.append( [ -1, 0, 5 ] );
def DelBonePreset(h, id, have) :
    if id < len(h):
        del h[id];
    
    for h in have :
      #  print(h[9])
        if not h[9] == 0 :
            if h[9]-1 > id :
                h[9] -= 1;
            else :
                if h[9]-1 == id :
                    print(h[9]-1 , id)
    return h;

def AddDeformPreset(h) :
    return h[4].append(  ["noiseUV",0.7,0.1,0.1,1, [1.,1.,1.], 1.]   );
def DelDeformPreset(h, id) :
    if id < len(h[4]):
        del h[4][id];
    return h;
def resetIdNoise(r,id,d) :
    if d >= 0 :
        if id+d < len(r) :
            r[id], r[d+id] = r[d+id], r[id]
    else :
        if id+d > -1 :
            r[id], r[d+id] = r[d+id], r[id]
    return r;

def ReSetControlPresets(self) :
    n = self.MainButtonNumber-1
    b = self.BoneButtonNumber-1
    
    self.MainCollectionTypeHair = self.Presets[n][0][0];
    self.MainCollectionSeparate = self.Presets[n][0][1];
    self.Count =                  self.Presets[n][1][0];
    self.Ditale =                 self.Presets[n][1][1];
    self.NoiseUv =                self.Presets[n][2][0];
    self.SizeUv =                 self.Presets[n][2][1];
    self.LenghtMax =              self.Presets[n][3][0];
    self.LenghtMin =              self.Presets[n][3][1];
    self.LenghtPow =              self.Presets[n][3][2];
    self.MainActive =             self.Presets[n][5];
    self.Smooth =                 self.Presets[n][6];
    self.HairRadius=              self.Presets[n][7];
    self.DinamickDitale =         self.Presets[n][8];
    self.MainButtonBoneNumber =   self.Presets[n][9];
    self.CountHairPreviev =       self.Presets[n][10];
    ReSetControlNoise(self);
    
    
    self.BoneButtonCount = len(self.BonePreset)
    if self.BoneButtonCount > 0 :
        self.BoneButtonUseDinamick =  self.BonePreset[b][1]
        self.BoneButtonDitale =       self.BonePreset[b][2]
        self.BoneButtonSepaateMaterials =self.BonePreset[b][0]
    else :
        self.BoneButtonUseDinamick =  0
        self.BoneButtonDitale =  0
        self.BoneButtonSepaateMaterials =0
        
    

def ReSetControlNoise(self) :
    
    n = self.MainButtonNumber - 1;
    
    self.NoiseButtonCount =       len(self.Presets[n][4])
    if self.NoiseButtonCount > self.NoiseButtonNumber :
        g = self.NoiseButtonNumber;
    else :
        g = self.NoiseButtonCount;
    
    self.NoiseButtonNumber = g;
    
    b = self.NoiseButtonNumber - 1;
    
    if len(self.Presets[n][4]) > 0 :
        self.NoiseHight =             self.Presets[n][4][b][1]
        self.NoisePower =             self.Presets[n][4][b][2]
        self.NoiseSize =              self.Presets[n][4][b][3]
        self.NoiseCollectionType =    self.Presets[n][4][b][0]
        self.NoiseActive =            self.Presets[n][4][b][4]
        
        self.NoiseGrowth =         self.Presets[n][4][b][6]
        for i in [0,1,2] :
            self.NoiseSpace[i] =   self.Presets[n][4][b][5][i]
    
#HairAddonBody.inf(bpy.data.materials)
def genGeomerti(mainColect, self, context, maps, Hairs, aDe, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types,matrialType,Smooth,noiseYes,bonesList,BoneId,mod) :
    if types == "vertex":
        me = bpy.data.meshes.new(maps.name+" Hair")
    else :
        me = bpy.data.curves.new("HairCurve", "CURVE")
        me.dimensions = '3D'
        me.resolution_u = 1;
        me.bevel_depth = 0.01;
        HairConductorSets.HairAddonBody.inf(me)
        me.bevel_resolution = 0;
        if not matrialType == -1 :
            me.materials.append(bpy.data.materials[ matrialType ] )
        else :
            for ide in self.uslesMaterial :
                me.materials.append(bpy.data.materials[ ide ])
    
    vert = bpy.data.objects.new(maps.name+" Hair", me)
    vert.location = maps.location
    
    if self.UsFinishPreset :
        if not self.DomenButtonReSize :
            if types == "curve":
                me.bevel_depth = 0;
        higt = bpy.data.collections.new(maps.name+" Hair")
        
        mainColect[0].children.link(higt)
        higt.hide_viewport = True
    else :
        higt = mainColect[0];
    
    higt.objects.link(vert)
    
    aperentBone = [];
    if types == "vertex": 
        if not BoneId == 0 :
            a = vert.modifiers.new(type = 'ARMATURE', name = 'test')
            apende = bpy.data.objects.find( bonesList[BoneId-1][0] )
            a.object = bpy.data.objects[apende]
            for lineBone in bonesList[BoneId-1][1] :
                LisEniBone = [];
                for EvryBone in lineBone[2] :
                    vert.vertex_groups.new(name = EvryBone)
                    LisEniBone.append(EvryBone)
                aperentBone.append( [ LisEniBone, lineBone[3] ] )
    VeteLenMap = [];
    if self.UsFinishPreset:
        print("Generate vertex")
    if types == "vertex":
        vertexMap = HairConductorSets.HairAddonBody.GenerateHairVertexMap(vert, maps, aDe, [count, ditale], DinamickDitale, [LenghtMin, LenghtMax, LenghtPow ], SizeUv, RangeUv, mod, self.UsFinishPreset )
        
        VeteLenMap = HairConductorSets.HairAddonBody.VertexSetPose(        maps, vert, aDe, vertexMap, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth, [self.NoiseButtonNumber-1,noiseYes, self], mod, "", self.UsFinishPreset);
        
        HairConductorSets.HairAddonBody.VertexGroupSet(vert, vertexMap, aperentBone, VeteLenMap, self.UsFinishPreset)
        
    else :
        vertexMap = HairConductorSets.HairAddonBody.GenerateHairCurveMap(vert, maps, aDe, [count, ditale], DinamickDitale, [LenghtMin, LenghtMax, LenghtPow ], SizeUv, RangeUv, mod, self.UsFinishPreset)
        c = [];
        for a in vertexMap :
            
            c = HairConductorSets.HairAddonBody.VertexSetPose(maps, vert, aDe, a, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth, [self.NoiseButtonNumber-1,noiseYes, self], mod, "curve", self.UsFinishPreset);
            HairConductorSets.HairAddonBody.makeSpline(vert, "BEZIER", c , size, vertexMap, aperentBone, VeteLenMap, self.UsFinishPreset)
            
    return vert;
def gen(self, context, scene, maps, mod) : 
    bonesList = []
    for Bones in range(len(self.BonePreset)) :
        if Bones == self.BoneButtonNumber-1 :
            dinamic = self.BoneButtonUseDinamick
            materisl = self.BoneButtonSepaateMaterials
            if self.BoneButtonSepaateLeft :
                if self.BoneButtonSepaateLeft > 0 :
                    materisl -= 1;
            if self.BoneButtonSepaateRight :
                if self.BoneButtonSepaateRight < len(self.uslesMaterial) :
                    materisl += 1;
            ditale = self.BoneButtonDitale
        else :
            dinamic = self.BonePreset[Bones][1]
            materisl = self.BonePreset[Bones][0]
            ditale = self.BonePreset[Bones][2]
        
        arm = bpy.data.armatures.new(maps.name+" Hair "+str(Bones+1))
        Armature = bpy.data.objects.new(maps.name+" Bone "+str(Bones+1), arm) 
        Armature.location = maps.location
        context.collection.objects.link(Armature)
        
        bonesList.append( HairConductorSets.HairAddonBody.GenerateBoneHairs(maps, Armature, ditale, dinamic, materisl, self.uslesMaterial, self.lines, mod) ) ;
        
    
    HairMainColection = bpy.data.collections.new("Hair collection")
    context.collection.children.link(HairMainColection)
    for Hairs in range(len(self.Presets)) :
        sel = [];
        noiseYes = 0;
        
        if Hairs == self.MainButtonNumber-1 :
            types = self.MainCollectionTypeHair
            Smooth = self.Smooth 
            count = self.Count
            ditale = self.Ditale
            RangeUv = self.NoiseUv
            SizeUv  = self.SizeUv
            LenghtMax = self.LenghtMax
            LenghtMin = self.LenghtMin
            LenghtPow = self.LenghtPow
            use = self.MainActive
            size = self.HairRadius
            DinamickDitale = self.DinamickDitale
            noiseYes = 1;
            
            BoneId = self.MainButtonBoneNumber
            Separate = self.MainCollectionSeparate
            
            SliseLines = self.CountHairPreviev;
            
            if self.MainButtonSeparateRight == 1 :
                if len(self.uslesMaterial) > self.MainCollectionSeparate : 
                    Separate += 1;
                    self.MainCollectionSeparate += 1;
            if self.MainButtonSeparateLeft == 1 :
                if not self.MainCollectionSeparate == -1 :
                    Separate -= 1;
                self.MainCollectionSeparate -= 1;
            if Separate > 0 and (self.MainButtonBoneRight or self.MainButtonBoneLeft) :
                boneUsles = self.BonePreset
            else :
                boneUsles = self.BonePreset
            
            if self.MainButtonBoneRight :
                if len(boneUsles) > self.MainButtonBoneNumber-1 : 
                    BoneId += 1;
                    self.MainButtonBoneNumber += 1;
            if self.MainButtonBoneLeft :
                if not self.MainButtonBoneNumber == 0 :
                    BoneId -= 1;
                    self.MainButtonBoneNumber -= 1;
        else :
            types =     self.Presets[Hairs][0][0]
            count =     self.Presets[Hairs][1][0]
            ditale =    self.Presets[Hairs][1][1]
            RangeUv =   self.Presets[Hairs][2][0]
            SizeUv  =   self.Presets[Hairs][2][1]
            LenghtMax = self.Presets[Hairs][3][0]
            LenghtMin = self.Presets[Hairs][3][1]
            LenghtPow = self.Presets[Hairs][3][2]
            use =       self.Presets[Hairs][5]
            size =      self.Presets[Hairs][7]
            Separate =  self.Presets[Hairs][0][1]
            Smooth =    self.Presets[Hairs][6]
            DinamickDitale = self.Presets[Hairs][8]
            BoneId =    self.Presets[Hairs][9]
            SliseLines =self.Presets[Hairs][10]
            
        sel = [];
        
        mainColect = [];
        if self.UsFinishPreset :
            count *= self.CountFinish
            ditale *= self.DitaleFinish
            
            print("Preset "+str(Hairs) )
            
            bpy.context.space_data.shading.type = 'WIREFRAME'
            
            mainColect.append( bpy.data.collections.new("Finish hair") )
            HairMainColection.children.link( mainColect[0] )
        else : 
            mainColect.append( HairMainColection )
        if use or self.UsFinishPreset :
            if Separate == -1 :
                if (not self.UsFinishPreset)*(not SliseLines == 0) * ( SliseLines < len(self.lines) ) :
                    a = self.lines[0:SliseLines]
                else :
                    a = self.lines
                if self.UsFinishPreset: 
                    print("All Element")
                sel = [genGeomerti(mainColect, self, context, maps, Hairs, a, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types, -1, Smooth, noiseYes, bonesList, BoneId, mod)]
            else : 
                LinesByMatreial = HairConductorSets.HairAddonBody.SeparateLineToMaterial(self.lines, self.uslesMaterial);
            if Separate == 0 :
                for a in range(len(LinesByMatreial)) :
                    if (not self.UsFinishPreset)*(not SliseLines == 0) * ( SliseLines < len(LinesByMatreial[a]) ) :
                        LinesByMatreialF = LinesByMatreial[a][0:SliseLines]
                    else :
                        LinesByMatreialF = LinesByMatreial[a];
                    if self.UsFinishPreset: 
                        print("Element "+str(a))
                    sel.append( genGeomerti(mainColect, self, context, maps, Hairs, LinesByMatreialF, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types, self.uslesMaterial[a], Smooth, noiseYes, bonesList, BoneId, mod) )
            if Separate > 0 :
                a = LinesByMatreial[Separate-1]
                if (not self.UsFinishPreset)*(not SliseLines == 0) * ( SliseLines < len(self.lines) ) :
                    a = a[0:SliseLines]
                if self.UsFinishPreset: 
                    print("Element "+str(Separate-1))
                sel = [genGeomerti(mainColect, self, context, maps, Hairs, a, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types, self.uslesMaterial[Separate-1], Smooth, noiseYes, bonesList, BoneId, mod)]
        
        self.selectObject.append(sel);
            


class HairMainOperator(bpy.types.Operator): 
    bl_label = "Generate Hair by object"
    bl_idname = "object.hair"
    bl_options = {'REGISTER', 'UNDO'}
    
    Count: bpy.props.IntProperty(name="Count", default=4, min=1, max=1000)
    Ditale: bpy.props.IntProperty(name="Number of vertices", default=3, min=2, max=1000)
    MainActive: bpy.props.BoolProperty(name="")
    Smooth: bpy.props.FloatProperty(name="Smooth", default=0, min=0, max=1, unit ='NONE', subtype ='FACTOR')
    DinamickDitale: bpy.props.BoolProperty(name="Dynamic count of vertices")
    
    
    CountHairPreviev: bpy.props.IntProperty(name="Count Hair Previev", default=0, min=0)
    CountFinish: bpy.props.FloatProperty(name="Count Finish", default=1, min=0.001)
    DitaleFinish: bpy.props.FloatProperty(name="Ditale Finish", default=1, min=0.001)
    UsFinishPreset: bpy.props.BoolProperty(name="", description="Us finish preset, use all hair, all preset")
    
    ReSetPreset: bpy.props.BoolProperty(name="", default=1, description="If true, all setting on new operator is reset")
    
    HairRadius: bpy.props.FloatProperty(name="Hair size", default=0.01, min=0.0001, max=2)
    NoiseUv: bpy.props.FloatProperty(name="Noise", default=1, min=0, max=1, unit ='NONE', subtype ='FACTOR')
    SizeUv: bpy.props.FloatProperty(name="Hair uv size", default=1, min=0, max=2)
    LenghtMax: bpy.props.FloatProperty(name="Max lenght", default=1, min=0, max=1, unit ='NONE', subtype ='FACTOR')
    LenghtMin: bpy.props.FloatProperty(name="Min lenght", default=1, min=0, max=1, unit ='NONE', subtype ='FACTOR')
    LenghtPow: bpy.props.FloatProperty(name="Lenght range", default=1, min=0.001, max=2)
    
    NoiseHight: bpy.props.FloatProperty(name="Noise hight", default=0.5, min=0, max=1, unit ='NONE', subtype ='FACTOR')
    NoisePower: bpy.props.FloatProperty(name="Noise power", default=0.02)
    
    NoiseSize: bpy.props.FloatProperty(name="Noise size", default=0.02)
    NoiseGrowth: bpy.props.FloatProperty(name="Noise growth", default=1, min=0.001, max=6)
    
    NoiseSpace: bpy.props.FloatVectorProperty(name="Noise space size", description="", default=(0.0, 0.0, 0.0), subtype='XYZ' )
    NoiseCollectionType: bpy.props.EnumProperty( name="Type", description ="Type of deform", items=( ('noiseUV', DeformNames[0][0], DeformNames[0][1], 'MOD_NOISE', 0), ('noiseXYZ', DeformNames[1][0], DeformNames[1][1], 'MOD_NOISE', 1), ('voron',DeformNames[2][0],DeformNames[3][1],'IPO_ELASTIC', 2), ('round',DeformNames[3][0],DeformNames[3][1],'CURVE_NCIRCLE', 3), ('size',DeformNames[4][0],DeformNames[4][1],'SORTSIZE', 5), ('rotate',DeformNames[5][0],DeformNames[5][1],'MOD_SCREW', 6) ) )
    NoiseActive: bpy.props.BoolProperty(name="")
    
    MainButtonLeft: bpy.props.BoolProperty(name="")
    MainButtonRight: bpy.props.BoolProperty(name="")
    MainButtonCount: bpy.props.IntProperty(name="", default=1, min=1, max=1000)
    MainButtonNumber: bpy.props.IntProperty(name="", default=1, min=1, max=1000)
    MainButtonDel: bpy.props.BoolProperty(name="")
    MainButtonAdd: bpy.props.BoolProperty(name="")
    
    NoiseButtonTop: bpy.props.BoolProperty(name="")
    NoiseButtonDown: bpy.props.BoolProperty(name="")
    NoiseButtonCount: bpy.props.IntProperty(name="", default=0, min=0, max=1000)
    NoiseButtonNumber: bpy.props.IntProperty(name="", default=0, min=0, max=1000)
    NoiseButtonDel: bpy.props.BoolProperty(name="")
    NoiseButtonAdd: bpy.props.BoolProperty(name="")
    NoiseButtonSetTop: bpy.props.BoolProperty(name="")
    NoiseButtonSetDown: bpy.props.BoolProperty(name="")
    
    DomenButtonConsole: bpy.props.BoolProperty(name="", default=1, description="If trye, console opened and demonstrate progress")
    DomenButtonReSize: bpy.props.BoolProperty(name="", default=0, description="If trye, curve use geometry volume")
    DomenButtonViews: bpy.props.BoolProperty(name="")
    DomenButtonBuild: bpy.props.BoolProperty(name="")
    DomenButtonBuildLeft: bpy.props.BoolProperty(name="")
    DomenButtonBuildRight: bpy.props.BoolProperty(name="")
    DomenButtonBuildNumber: bpy.props.IntProperty(name="Fractal", default=0, min=0, max=1000)
    
    
    BoneButtonLeft: bpy.props.BoolProperty(name="")
    BoneButtonRight: bpy.props.BoolProperty(name="")
    BoneButtonAdd: bpy.props.BoolProperty(name="")
    BoneButtonDel: bpy.props.BoolProperty(name="")
    BoneButtonCount: bpy.props.IntProperty(name="", default=0, min=0, max=1000)
    BoneButtonNumber: bpy.props.IntProperty(name="", default=1, min=1, max=1000)
    BoneButtonSepaateLeft: bpy.props.BoolProperty(name="")
    BoneButtonSepaateRight: bpy.props.BoolProperty(name="")
    
    BoneButtonUseDinamick: bpy.props.BoolProperty(name="Use dinamick ditale")
    BoneButtonDitale: bpy.props.FloatProperty(name="", default=1, min=1)
    BoneButtonSepaateMaterials: bpy.props.IntProperty(name="", default=0, min=0, max=1000 )
    
    MainButtonBoneLeft: bpy.props.BoolProperty(name="")
    MainButtonBoneRight: bpy.props.BoolProperty(name="")
    MainButtonBoneNumber: bpy.props.IntProperty(name="", default=0, min=0, max=1000)
    
    
    
    
    
    string = bpy.props.StringProperty(name="curve")
    
    
    MainCollectionTypeHair: bpy.props.EnumProperty( name="Type", items=( ('vertex', "Object", '1', 'OUTLINER_DATA_HAIR', 0), ('curves','Curves','1','OUTLINER_OB_HAIR', 1) ) )
    #MainCollectionSeparate: bpy.props.EnumProperty( name="Separation", items=( ('not', "Do not separation", '1', '', 0), ('all','All materials','1','', 1), ('one','By ID','2','', 2) ) )
    
    MainCollectionSeparate: bpy.props.IntProperty(name="Fractal", default=0, min=-1, max=100)
    MainButtonSeparateLeft: bpy.props.BoolProperty(name="")
    MainButtonSeparateRight: bpy.props.BoolProperty(name="")
    
    
    
    Presets = [ [ ["vertex",-1], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ],1, 1.,0.01,1,0, 0 ] ];
    BonePreset = [ ];
    
    uslesMaterial = [];
    #MainCollectionSeparate = [];
    lines = [];
    vertexMap = [];
    selectObject = [];
    
    def execute(self, context):
        scene = context.scene
        maps = context.active_object
        mod = bpy.context.mode;
        self.selectObject = [];
          
        if self.DomenButtonBuild :
            if (len(self.lines) == 0) :
                self.lines = HairConductorSets.HairAddonBody.HairLines(maps, self.DomenButtonBuildNumber, mod);
                self.BonePreset = [];
                self.BoneButtonNumber = 0;
                self.BoneButtonCount = 0;
                
            self.uslesMaterial = HairConductorSets.HairAddonBody.noCopiList(self.lines)
            if self.UsFinishPreset and self.DomenButtonConsole :
                bpy.ops.wm.console_toggle()
            gen(self, context, scene, maps, mod)
            if self.UsFinishPreset and self.DomenButtonConsole : 
                bpy.ops.wm.console_toggle()
            #print(self.selectObject)
            for sec in range(len(self.selectObject)) :
                for sel in self.selectObject[sec] :
                    if not self.UsFinishPreset :
                        sel.select_set(True)
                        
                  #  else :
                #        sel.select_set(False)
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.object.mode_set(mode=mod)
            
            if not self.DomenButtonViews :
                maps.display_type = 'WIRE'
            else :
                maps.display_type = 'TEXTURED'
            self.UsFinishPreset = 0;
        
        return {'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        row = layout.row()
        
        maps = context.active_object
        mod = bpy.context.mode;
        
        if len(self.lines) == 0 :
            if len(maps.data.materials) > 0 :
                
                le = len(maps.vertex_groups)
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.DomenButtonBuildLeft(row, self) :
                    self.DomenButtonBuildNumber -= 1;
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.DomenButtonBuildRight(row, self) :
                    if le-1 > self.DomenButtonBuildNumber :
                        self.DomenButtonBuildNumber += 1;
                row = row.split(factor=0.8, align=True)
                if not len(maps.vertex_groups) == 0 :
                    row.label(text=OperatorText[0]+maps.vertex_groups[self.DomenButtonBuildNumber].name)
                else :
                    row.label(text=OperatorText[1])
                row = row.split(factor=1, align=True)
                HairConductorSets.Buttons.DomenButtonBuild(row,self)
            else :
                row.label(text=OperatorText[2], icon="SHADING_TEXTURE")
            
        else :
            
            row.prop(self, "DomenButtonViews",text="View domain ");
            #row.label(text="View domain ")
            
            row = layout.row()
            
            row.label(text=OperatorText[3], icon="HAIR_DATA")
            row = (layout.box()).row()
            
            row = row.split(factor=0.1, align=True)
            if HairConductorSets.Buttons.MainButtonAdd(row, self) :
                self.MainButtonCount += 1;
                self.MainButtonNumber = self.MainButtonCount;
                AddHairPreset(self.Presets);
                ReSetControlPresets(self);
            
            row = row.split(factor=0.1, align=True)
            if HairConductorSets.Buttons.MainButtonDel(row, self) :
                if self.MainButtonCount > 1 :
                    DelHairPreset(self.Presets, self.MainButtonNumber-1);
                    self.MainButtonCount -= 1;
                    self.MainButtonNumber -= 1;
                    ReSetControlPresets(self);
            
            row.label(text = OperatorText[4]+str(self.MainButtonCount)+")" )
        
            if self.MainButtonCount > 1:
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.MainButtonLeft(row, self) :
                    self.MainButtonNumber -= 1;
                    ReSetControlPresets(self);
                
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.MainButtonRight(row, self) :
                    if self.MainButtonNumber < self.MainButtonCount :
                        self.MainButtonNumber += 1;
                        ReSetControlPresets(self);
                
                row.label(text = OperatorText[5]+str(self.MainButtonNumber)+".")
                row = layout.row()
            #print(self.MainButtonNumber - 1,self.NoiseButtonNumber - 1);
            row = layout.row()
            row.label(text=OperatorText[6], icon="OUTLINER_OB_GROUP_INSTANCE")
            row = layout.row()
            row.prop(self, "MainCollectionTypeHair",icon="PARTICLEMODE");
            self.Presets[self.MainButtonNumber-1][0][0] = self.MainCollectionTypeHair;
            row = layout.row()
            if "curves" == self.MainCollectionTypeHair :
                row.prop(self, "HairRadius");
                self.Presets[self.MainButtonNumber-1][7] = self.HairRadius;
                row = layout.row()
            
            e = maps.material_slots
            row = (layout.box()).row()
            row = row.split(factor=0.1, align=True)
            HairConductorSets.Buttons.MainButtonSeparateLeft(row, self)
            row = row.split(factor=0.1, align=True)
            HairConductorSets.Buttons.MainButtonSeparateRight(row, self)
            self.Presets[self.MainButtonNumber-1][0][1] = self.MainCollectionSeparate;
            if self.MainCollectionSeparate == -1 :
                row.label(text = OperatorText[7])
            if self.MainCollectionSeparate == 0 :
                row.label(text = OperatorText[8])
            if self.MainCollectionSeparate > 0 :
                if len(e) > self.MainCollectionSeparate-1 : 
                    row.label(text = OperatorText[9]+self.uslesMaterial[self.MainCollectionSeparate-1])
            
            if self.MainCollectionTypeHair == "vertex" :
                row = layout.row()
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                HairConductorSets.Buttons.MainButtonBoneLeft(row, self)
                row = row.split(factor=0.1, align=True)
                HairConductorSets.Buttons.MainButtonBoneRight(row, self)
                if self.MainButtonBoneNumber == 0 :
                    row.label(text = OperatorText[10])
                else :
                    row.label(text = OperatorText[11]+str(self.MainButtonBoneNumber))
                    if self.BonePreset[ self.Presets[self.MainButtonNumber-1][9]-1 ][0] == 0 :
                        row.label(text = OperatorText[12])
                    else :
                        row.label(text = self.uslesMaterial[ self.BonePreset[ self.Presets[self.MainButtonNumber-1][9]-1 ][0]-1 ] )
                self.Presets[self.MainButtonNumber-1][9] = self.MainButtonBoneNumber;
            
            row = layout.row()
            
            row = row.split(factor=0.5, align=True)
            row.prop(self, "Count")
            self.Presets[self.MainButtonNumber-1][1][0] = self.Count;
            row.prop(self, "Ditale")
            self.Presets[self.MainButtonNumber-1][1][1] = self.Ditale;#DinamickDitale
            
            row = layout.row()
            row.prop(self, "Smooth")
            self.Presets[self.MainButtonNumber-1][6] = self.Smooth;
            row = layout.row()
            row.prop(self, "DinamickDitale")
            self.Presets[self.MainButtonNumber-1][8] = self.DinamickDitale;
            
            row = layout.row()
            row.prop(self, "MainActive", text=OperatorText[13])
            self.Presets[self.MainButtonNumber-1][5] = self.MainActive;
            
            row = layout.row()
            #row = (layout.box()).row()
            row = row.split(factor=0.5, align=True)
            row.prop(self, "NoiseUv")
            self.Presets[self.MainButtonNumber-1][2][0] = self.NoiseUv;
            row.prop(self, "SizeUv", translate=True)
            self.Presets[self.MainButtonNumber-1][2][1] = self.SizeUv;
            
            row = layout.row()
            #row = (layout.box()).row()
            row = row.split(factor=0.333, align=True)
            row.prop(self, "LenghtMax")
            self.Presets[self.MainButtonNumber-1][3][0] = self.LenghtMax;
            row.prop(self, "LenghtMin")
            self.Presets[self.MainButtonNumber-1][3][1] = self.LenghtMin;
            row.prop(self, "LenghtPow")
            self.Presets[self.MainButtonNumber-1][3][2] = self.LenghtPow;
            
            
            
            row = layout.row()
            row.label(text = OperatorText[14], icon="OPTIONS")
            row = (layout.box()).row()
            if self.CountHairPreviev == 0 :
                row = row.split(factor=0.5, align=True)
                row.label(text = OperatorText[15])
            row.prop(self, "CountHairPreviev")
            self.Presets[self.MainButtonNumber-1][10] = self.CountHairPreviev;
            
            
            
            row = layout.row()
            
            row.separator(factor=2.0)
            row = layout.row()
            row.label(text=OperatorText[16], icon = "MODIFIER") # , icon = ""
            row = (layout.box()).row()
            
            row = row.split(factor=0.1, align=True)
            if HairConductorSets.Buttons.NoiseButtonAdd(row, self) :
                AddDeformPreset(self.Presets[self.MainButtonNumber-1]);
                self.NoiseButtonCount += 1;
                self.NoiseButtonNumber = self.NoiseButtonCount;
                ReSetControlNoise(self);
            
            row = row.split(factor=0.1, align=True)
            if HairConductorSets.Buttons.NoiseButtonDel(row, self) :
                if self.NoiseButtonCount > 0 :
                    if self.NoiseButtonNumber > 1 :
                        self.NoiseButtonNumber -= 1;
                        ReSetControlNoise(self);
                        DelDeformPreset(self.Presets[self.MainButtonNumber-1], self.NoiseButtonNumber-1);
                    else :
                        DelDeformPreset(self.Presets[self.MainButtonNumber-1], self.NoiseButtonNumber-1);
                        ReSetControlNoise(self);
        
            row.label(text = OperatorText[17]+str(self.NoiseButtonCount)+") ")
        
            if (self.NoiseButtonCount > 1):
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                
                if HairConductorSets.Buttons.NoiseButtonTop(row, self) :
                    if self.NoiseButtonNumber > 1 :
                        self.NoiseButtonNumber -= 1;
                        ReSetControlNoise(self);
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.NoiseButtonDown(row, self) :
                    if self.NoiseButtonNumber < self.NoiseButtonCount :
                        self.NoiseButtonNumber += 1;
                        ReSetControlNoise(self);
                row = row.split(factor=0.6, align=True)
                row.label(text = OperatorText[16]+str(self.NoiseButtonNumber))
                
                row = row.split(factor=0.3, align=True)
                if HairConductorSets.Buttons.NoiseButtonSetTop(row, self) :
                    self.Presets[self.MainButtonNumber-1][4] = resetIdNoise(self.Presets[self.MainButtonNumber-1][4], self.NoiseButtonNumber-1, -1)
                    ReSetControlNoise(self)
                row = row.split(factor=0.4, align=True)
                if HairConductorSets.Buttons.NoiseButtonSetDown(row, self) :
                    self.Presets[self.MainButtonNumber-1][4] = resetIdNoise(self.Presets[self.MainButtonNumber-1][4], self.NoiseButtonNumber-1, 1)
                    ReSetControlNoise(self)
                
            if (self.NoiseButtonCount > 0) :
                for i in range(self.NoiseButtonNumber-1) :
                    row = (layout.box()).row()
                    row.label(text = OperatorText[18]+str(i+1)+", Type "+ self.Presets[self.MainButtonNumber-1][4][i][0]+", Size "+str(math.floor( self.Presets[self.MainButtonNumber-1][4][i][1]*10)/10 ))
                
                row = layout.row()
                row.label(text = OperatorText[18]+str(self.NoiseButtonNumber))
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "NoiseCollectionType", icon = "PRESET")
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "NoiseHight")
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "NoisePower")
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "NoiseSize")
                if self.NoiseCollectionType == "size" :
                    row = layout.row()
                    row = row.grid_flow(row_major = 1);
                    row.prop(self, "NoiseSpace")
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "NoiseGrowth")
                row = layout.row()
                row.prop(self, "NoiseActive", text="Use")
                
                
                self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][4] = self.NoiseActive;
                self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][1] = self.NoiseHight;
                self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][2] = self.NoisePower;
                self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][3] = self.NoiseSize;
                self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][0] = self.NoiseCollectionType;
                for i in [0,1,2] :
                    self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][5][i] = self.NoiseSpace[i];
                self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][6] = self.NoiseGrowth;
                
                for i in range( len( self.Presets[self.MainButtonNumber-1][4] ) -self.NoiseButtonNumber) :
                    row = (layout.box()).row()
                    row.label(text = OperatorText[18]+str(i+self.NoiseButtonNumber+1)+", Type "+ self.Presets[self.MainButtonNumber-1][4][i+self.NoiseButtonNumber][0]+", Size "+str(math.floor( self.Presets[self.MainButtonNumber-1][4][i+self.NoiseButtonNumber][1]*10)/10))
            row = layout.row()
            row.separator(factor=2.0)
            
            row = layout.row()
            row.label(text = OperatorText[20], icon="OPTIONS")#DomenButtonReSize
            row = layout.row()
            row = (layout.box()).row()
            row.prop(self, "DomenButtonReSize", icon="CONE")
            row.prop(self, "DomenButtonConsole", icon="WORDWRAP_ON")
            row = row.split(factor=0.4, align=True)
            row.prop(self, "CountFinish")
            row = row.split(factor=4/6, align=True)
            row.prop(self, "DitaleFinish")
            row.prop(self, "UsFinishPreset",icon="VIS_SEL_11")
            
            
            row = layout.row()
            row.separator(factor=2.0)
            row = layout.row()
            row.label(text = OperatorText[21], icon="ARMATURE_DATA")
            
            
            row = (layout.box()).row()
            row = row.split(factor=0.1, align=True)
            if HairConductorSets.Buttons.BoneButtonAdd(row, self) :
                self.BoneButtonCount += 1;
                self.BoneButtonNumber = self.BoneButtonCount
                AddBonePreset(self.BonePreset);
                ReSetControlPresets(self);
            
            row = row.split(factor=0.1, align=True)
            if HairConductorSets.Buttons.BoneButtonDel(row, self) :
                if self.BoneButtonNumber > 0 :
                    DelBonePreset(self.BonePreset, self.BoneButtonNumber-1, self.Presets);
                    self.BoneButtonCount -= 1;
                    self.BoneButtonNumber -= 1;
                    ReSetControlPresets(self);
            
            row.label(text = OperatorText[22]+str(self.BoneButtonCount)+")" )
        
            if self.BoneButtonCount > 1:
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.BoneButtonLeft(row, self) :
                    self.BoneButtonNumber -= 1;
                    ReSetControlPresets(self);
                
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.BoneButtonRight(row, self) :
                    if self.BoneButtonNumber < self.BoneButtonCount :
                        self.BoneButtonNumber += 1;
                        ReSetControlPresets(self);
                
                row.label(text = OperatorText[23]+str(self.BoneButtonNumber)+".")
                row = layout.row()
            if self.BoneButtonCount > 0:
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "BoneButtonUseDinamick")
                row = layout.row()
                row = row.split(factor=1, align=True)
                row.prop(self, "BoneButtonDitale")
                row = layout.row()
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.BoneButtonSepaateLeft(row, self) :
                    self.BoneButtonSepaateMaterials -= 1;
                row = row.split(factor=0.1, align=True)
                if HairConductorSets.Buttons.BoneButtonSepaateRight(row, self) :
                    if self.BoneButtonSepaateMaterials < len(self.uslesMaterial) :
                        self.BoneButtonSepaateMaterials += 1;
                if self.BoneButtonSepaateMaterials > 0 :
                    row.label(text = OperatorText[24]+self.uslesMaterial[self.BoneButtonSepaateMaterials-1])
                else :
                    row.label(text = OperatorText[25])
                row = layout.row()
                
                self.BonePreset[self.BoneButtonNumber-1][1] = self.BoneButtonUseDinamick;
                self.BonePreset[self.BoneButtonNumber-1][2] = self.BoneButtonDitale;
                self.BonePreset[self.BoneButtonNumber-1][0] = self.BoneButtonSepaateMaterials;
            
            
            row = layout.row()
            row.separator(factor=2.0)
            row = layout.row()
            row.prop(self, "ReSetPreset",icon="FILE_REFRESH")
            
        
    def ttt(self) :
        print("test")
    def invoke(self, context, event):
        self.DomenButtonBuild = 0;
        if self.ReSetPreset :
            self.DomenButtonViews = 1;
            self.Presets = [ [ ["vertex",-1], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ],1,1.,0.01,1,0, 0  ] ];
            self.lines = [];
            self.vertexMap = [];
            self.BonePreset = [];
            self.MainButtonCount = 0;
            self.MainButtonNumber = 0;
            self.NoiseButtonCount = 0;
            self.NoiseButtonNumber = 0;
            ReSetControlPresets(self);
            self.DitaleFinish = 1;
            self.CountFinish = 1;
            self.CountHairPreviev = 0;
            self.BoneButtonNumber = 0;
            self.BoneButtonCount = 0;
            
        return {'FINISHED'}

classe = [HairMainOperator];

def menu_func(self, context):
    self.layout.operator(HairMainOperator.bl_idname)

def register():
    for c in classe :
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    for c in classe :
        bpy.utils.unregister_class(c)
    bpy.types.VIEW3D_MT_object.remove(menu_func)

if __name__ == "__main__":
    register()