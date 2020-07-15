bl_info = {
    "name": "Hair test addon1",
    "description": "testing",
    "author": "Mod",
    "version": (0),
    "blender": (2, 80, 0),
    #"support": "COMMUNITY",
}

import bpy
import HairAddonBody
import Buttons
import math

def AddHairPreset(h) :
    return h.append( [ ["vertex",0], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ], 1,1.,0.01,1 ] );
def DelHairPreset(h, id) :
    if id < len(h):
        del h[id];
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
    ReSetControlNoise(self);

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
def genGeomerti(self, context, maps, Hairs, aDe, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types,matrialType,Smooth,noiseYes,mod) :
    if types == "vertex":
        me = bpy.data.meshes.new(maps.name+" Hair")
    else :
        me = bpy.data.curves.new("HairCurve", "CURVE")
        me.dimensions = '3D'
        me.resolution_u = 1;
        me.bevel_depth = 0.01;
        me.bevel_resolution = 0;
        if not matrialType == -1 :
            me.materials.append(bpy.data.materials[ matrialType ] )
        else :
            for ide in self.uslesMaterial :
                me.materials.append(bpy.data.materials[ ide ])
    
    vert = bpy.data.objects.new(maps.name+" Hair", me) 
    vert.location = maps.location
    context.collection.objects.link(vert)
    
    
    if types == "vertex":
        vertexMap = HairAddonBody.GenerateHairVertexMap(vert, maps, aDe, [count, ditale], DinamickDitale, [LenghtMin, LenghtMax, LenghtPow ], SizeUv, RangeUv, mod)
        
        HairAddonBody.VertexSetPose(        maps, vert, aDe, vertexMap, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth, [self.NoiseButtonNumber-1,noiseYes, self], mod, "" );
        
    else :
        vertexMap = HairAddonBody.GenerateHairCurveMap(vert, maps, aDe, [count, ditale], DinamickDitale, [LenghtMin, LenghtMax, LenghtPow ], SizeUv, RangeUv, mod)
        c = [];
        for a in vertexMap :
            
            c = HairAddonBody.VertexSetPose(maps, vert, aDe, a, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth, [self.NoiseButtonNumber-1,noiseYes, self], mod, "curve" );
            #c =    HairAddonBody.CurvePose(maps, vert, aDe, a, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth,mod );
            HairAddonBody.makeSpline(vert.data, "BEZIER", c , size)
    return vert;

def gen(self, context, scene, maps, mod) : 
    for Hairs in range(len(self.Presets)) :
        sel = [];
        noiseYes = 0;
        if Hairs == self.MainButtonNumber-1 :
            types = self.MainCollectionTypeHair
            #self.MainCollectionSeparate
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
            Separate = self.MainCollectionSeparate
            DinamickDitale = self.DinamickDitale
            noiseYes = 1;
            
            if self.MainButtonSeparateRight == 1 :
                if len(self.uslesMaterial) > self.MainCollectionSeparate : 
                    Separate += 1;
                    self.MainCollectionSeparate += 1;
            if self.MainButtonSeparateLeft == 1 :
                if not self.MainCollectionSeparate == -1 :
                    Separate -= 1;
                self.MainCollectionSeparate -= 1;
            
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
        #print(Separate)
        sel = [];
        
        if self.UsFinishPreset :
            count *= self.CountFinish
            ditale *= self.DitaleFinish
            self.UsFinishPreset = 0;
        
        if use :
            if Separate == -1 :
                a = self.lines
                sel = [genGeomerti(self, context, maps, Hairs, a, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types, -1, Smooth, noiseYes, mod)]
            else : 
                LinesByMatreial = HairAddonBody.SeparateLineToMaterial(self.lines, self.uslesMaterial);
            if Separate == 0 :
                for a in range(len(LinesByMatreial)) :
                    sel.append( genGeomerti(self, context, maps, Hairs, LinesByMatreial[a], count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types, self.uslesMaterial[a], Smooth, noiseYes, mod) )
            if Separate > 0 :
                a = LinesByMatreial[Separate-1]
                sel = [genGeomerti(self, context, maps, Hairs, a, count,ditale, DinamickDitale,size,SizeUv,RangeUv,LenghtMin,LenghtMax,LenghtPow,types, self.uslesMaterial[Separate-1], Smooth, noiseYes, mod)]
        
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
    UsFinishPreset: bpy.props.BoolProperty(name="", description="Us finish preset, use all hair")
    
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
    NoiseCollectionType: bpy.props.EnumProperty( name="Type", description ="Type of deform", items=( ('noiseUV', "UV Noise", 'Gradient noise deform by hair data', 'MOD_NOISE', 0), ('noiseXYZ', "XYZ Noise", 'Gradient noise deform by hair cord', 'MOD_NOISE', 1), ('voron','Voronoise','1','IPO_ELASTIC', 2), ('round','Round','1','CURVE_NCIRCLE', 3), ('size','Resize','resize ','SORTSIZE', 5), ('rotate','Rotate','rotate ','MOD_SCREW', 6) ) )
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
    
    DomenButtonViews: bpy.props.BoolProperty(name="")
    DomenButtonBuild: bpy.props.BoolProperty(name="")
    DomenButtonBuildLeft: bpy.props.BoolProperty(name="")
    DomenButtonBuildRight: bpy.props.BoolProperty(name="")
    DomenButtonBuildNumber: bpy.props.IntProperty(name="Fractal", default=0, min=0, max=1000)
    
    
    string = bpy.props.StringProperty(name="curve")
    
    
    MainCollectionTypeHair: bpy.props.EnumProperty( name="Type", items=( ('vertex', "Object", '1', 'OUTLINER_DATA_HAIR', 0), ('curves','Curves','1','OUTLINER_OB_HAIR', 1) ) )
    #MainCollectionSeparate: bpy.props.EnumProperty( name="Separation", items=( ('not', "Do not separation", '1', '', 0), ('all','All materials','1','', 1), ('one','By ID','2','', 2) ) )
    
    MainCollectionSeparate: bpy.props.IntProperty(name="Fractal", default=0, min=-1, max=100)
    MainButtonSeparateLeft: bpy.props.BoolProperty(name="")
    MainButtonSeparateRight: bpy.props.BoolProperty(name="")
    
    
    
    Presets = [ [ ["vertex",0], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ],1, 1.,0.01,1 ] ];
    
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
                self.linesOld = HairAddonBody.HairLines(maps, self.DomenButtonBuildNumber, mod);
            if (not self.UsFinishPreset)*(not self.CountHairPreviev == 0) * ( self.CountHairPreviev < len(self.linesOld) ) :
                self.lines = self.linesOld[0:self.CountHairPreviev]
            else :
                self.lines = self.linesOld;
            self.uslesMaterial = HairAddonBody.noCopiList(self.lines)
            
            gen(self, context, scene, maps, mod)
            
            #print(self.selectObject)
            for sec in range(len(self.selectObject)) :
                for sel in self.selectObject[sec] :
                    if sec == self.MainButtonNumber-1 :
                        sel.select_set(True)
                    else :
                        sel.select_set(False)
            
            if not self.DomenButtonViews :
                maps.display_type = 'WIRE'
                #bpy.context.space_data.shading.type = 'MATERIAL'
                #bpy.context.space_data.overlay.show_overlays = False
            else :
                #bpy.context.space_data.overlay.show_overlays = True
                #bpy.context.space_data.shading.type = 'SOLID'
                maps.display_type = 'TEXTURED'
            
        
        return {'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        row = layout.row()
        
        maps = context.active_object
        mod = bpy.context.mode;
        
        if len(self.lines) == 0 :
            le = len(maps.vertex_groups)
            row = (layout.box()).row()
            row = row.split(factor=0.1, align=True)
            if Buttons.DomenButtonBuildLeft(row, self) :
                    self.DomenButtonBuildNumber -= 1;
            row = row.split(factor=0.1, align=True)
            if Buttons.DomenButtonBuildRight(row, self) :
                if le-1 > self.DomenButtonBuildNumber :
                    self.DomenButtonBuildNumber += 1;
            row = row.split(factor=0.8, align=True)
            row.label(text="Hair base group "+maps.vertex_groups[self.DomenButtonBuildNumber].name)
            row = row.split(factor=1, align=True)
            Buttons.DomenButtonBuild(row,self)
            
        else :
            
            row.prop(self, "DomenButtonViews",text="View domain ");
            #row.label(text="View domain ")
            
            row = layout.row()
            
            row.label(text="Hair collection: ", icon="HAIR_DATA")
            row = (layout.box()).row()
            
            row = row.split(factor=0.1, align=True)
            if Buttons.MainButtonAdd(row, self) :
                self.MainButtonCount += 1;
                self.MainButtonNumber += 1;
                AddHairPreset(self.Presets);
                ReSetControlPresets(self);
            
            row = row.split(factor=0.1, align=True)
            if Buttons.MainButtonDel(row, self) :
                if self.MainButtonCount > 1 :
                    DelHairPreset(self.Presets, self.MainButtonNumber-1);
                    self.MainButtonCount -= 1;
                    self.MainButtonNumber -= 1;
                    ReSetControlPresets(self);
            
            row.label(text = "Delet thes or add new (count "+str(self.MainButtonCount)+")" )
        
            if self.MainButtonCount > 1:
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if Buttons.MainButtonLeft(row, self) :
                    self.MainButtonNumber -= 1;
                    ReSetControlPresets(self);
                
                row = row.split(factor=0.1, align=True)
                if Buttons.MainButtonRight(row, self) :
                    if self.MainButtonNumber < self.MainButtonCount :
                        self.MainButtonNumber += 1;
                        ReSetControlPresets(self);
                
                row.label(text = "Hair preset number "+str(self.MainButtonNumber)+".")
                row = layout.row()
            #print(self.MainButtonNumber - 1,self.NoiseButtonNumber - 1);
            row = layout.row()
            row.label(text="This collection hair main setings: ", icon="OUTLINER_OB_GROUP_INSTANCE")
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
            Buttons.MainButtonSeparateLeft(row, self)
            row = row.split(factor=0.1, align=True)
            Buttons.MainButtonSeparateRight(row, self)
            self.Presets[self.MainButtonNumber-1][0][1] = self.MainCollectionSeparate;
            if self.MainCollectionSeparate == -1 :
                row.label(text = "No Separate Object")
            if self.MainCollectionSeparate == 0 :
                row.label(text = "Separate All Material")
            if self.MainCollectionSeparate > 0 :
                if len(e) > self.MainCollectionSeparate-1 : 
                    row.label(text = "Only "+self.uslesMaterial[self.MainCollectionSeparate-1])
            #self.execute(self, context)
            row = layout.row()
            #row = (layout.box()).row()
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
            self.Presets[self.DinamickDitale-1][8] = self.DinamickDitale;
            
            row = layout.row()
            row.prop(self, "MainActive", text="Use")
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
            
            row.separator(factor=2.0)
            row = layout.row()
            row.label(text="Hair deform collection: ", icon = "MODIFIER") # , icon = ""
            row = (layout.box()).row()
            
            row = row.split(factor=0.1, align=True)
            if Buttons.NoiseButtonAdd(row, self) :
                AddDeformPreset(self.Presets[self.MainButtonNumber-1]);
                self.NoiseButtonCount += 1;
                self.NoiseButtonNumber = self.NoiseButtonCount;
                ReSetControlNoise(self);
            
            row = row.split(factor=0.1, align=True)
            if Buttons.NoiseButtonDel(row, self) :
                if self.NoiseButtonCount > 0 :
                    if self.NoiseButtonNumber > 1 :
                        self.NoiseButtonNumber -= 1;
                        ReSetControlNoise(self);
                        DelDeformPreset(self.Presets[self.MainButtonNumber-1], self.NoiseButtonNumber-1);
                    else :
                        DelDeformPreset(self.Presets[self.MainButtonNumber-1], self.NoiseButtonNumber-1);
                        ReSetControlNoise(self);
        
            row.label(text = "Delet thes or add new (count "+str(self.NoiseButtonCount)+") ")
        
            if (self.NoiseButtonCount > 1):
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                
                if Buttons.NoiseButtonTop(row, self) :
                    if self.NoiseButtonNumber > 1 :
                        self.NoiseButtonNumber -= 1;
                        ReSetControlNoise(self);
                row = row.split(factor=0.1, align=True)
                if Buttons.NoiseButtonDown(row, self) :
                    if self.NoiseButtonNumber < self.NoiseButtonCount :
                        self.NoiseButtonNumber += 1;
                        ReSetControlNoise(self);
                row = row.split(factor=0.6, align=True)
                row.label(text = "Number "+str(self.NoiseButtonNumber))
                
                row = row.split(factor=0.3, align=True)
                if Buttons.NoiseButtonSetTop(row, self) :
                    self.Presets[self.MainButtonNumber-1][4] = resetIdNoise(self.Presets[self.MainButtonNumber-1][4], self.NoiseButtonNumber-1, -1)
                    ReSetControlNoise(self)
                row = row.split(factor=0.4, align=True)
                if Buttons.NoiseButtonSetDown(row, self) :
                    self.Presets[self.MainButtonNumber-1][4] = resetIdNoise(self.Presets[self.MainButtonNumber-1][4], self.NoiseButtonNumber-1, 1)
                    ReSetControlNoise(self)
                
            if (self.NoiseButtonCount > 0) :
                for i in range(self.NoiseButtonNumber-1) :
                    row = (layout.box()).row()
                    row.label(text = "Number "+str(i+1)+", Type "+ self.Presets[self.MainButtonNumber-1][4][i][0]+", Size "+str(math.floor( self.Presets[self.MainButtonNumber-1][4][i][1]*10)/10 ))
                
                row = layout.row()
                row.label(text = "Number "+str(self.NoiseButtonNumber))
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
                    row.label(text = "Number "+str(i+self.NoiseButtonNumber+1)+", Type "+ self.Presets[self.MainButtonNumber-1][4][i+self.NoiseButtonNumber][0]+", Size "+str(math.floor( self.Presets[self.MainButtonNumber-1][4][i+self.NoiseButtonNumber][1]*10)/10))
            row = layout.row()
            row.separator(factor=2.0)
            row = layout.row()
            row.label(text = "Prewiev setingt", icon="OPTIONS")
            row = (layout.box()).row()
            if self.CountHairPreviev == 0 :
                row = row.split(factor=0.5, align=True)
                row.label(text = "View full object")
            row.prop(self, "CountHairPreviev")
            row = layout.row()
            row = (layout.box()).row()
            row = row.split(factor=0.4, align=True)
            row.prop(self, "CountFinish")
            row = row.split(factor=4/6, align=True)
            row.prop(self, "DitaleFinish")
            row.prop(self, "UsFinishPreset",icon="VIS_SEL_11")
            row = layout.row()
            row.prop(self, "ReSetPreset",icon="FILE_REFRESH")
            
            
            
            
        
    def ttt(self) :
        print("test")
    def invoke(self, context, event):
        self.DomenButtonBuild = 0;
        if self.ReSetPreset :
            self.DomenButtonViews = 1;
            self.Presets = [ [ ["vertex",0], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ],1,1.,0.01,1  ] ];
            self.MainButtonCount = 0;
            self.MainButtonNumber = 0;
            self.NoiseButtonCount = 0;
            self.NoiseButtonNumber = 0;
            ReSetControlPresets(self);
            self.lines = [];
            self.vertexMap = [];
            self.DitaleFinish = 1;
            self.CountFinish = 1;
            #self.UsFinishPreset = 1;
            self.CountHairPreviev = 0;
        return {'FINISHED'}

classe = [HairMainOperator];

#testProp: bpy.props.StringProperty(name="testProp")
#bpy.types.Scene.testprop = bpy.props.FloatProperty(name="testProp")

testTranslate = {"ru_RU":  {('operator', "Hair uv size") : "ПЕРЕВОД"} }

def menu_func(self, context):
    self.layout.operator(HairMainOperator.bl_idname)

def register():
    for c in classe :
        bpy.utils.register_class(c)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    #print(translations_dict)
    bpy.app.translations.register(__name__, testTranslate)
    
def unregister():
    for c in classe :
        bpy.utils.unregister_class(c)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    bpy.app.translations.unregister(__name__)