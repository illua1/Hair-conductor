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
    return h.append( [ ["vertex",0], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ], 1,0.,0.01 ] );
def DelHairPreset(h, id) :
    if id < len(h):
        del h[id];
    return h;

def AddDeformPreset(h) :
    return h[4].append(  ["default",0.7,0.1,0.1,"xyz",1]   );
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
        self.HoiseSize =              self.Presets[n][4][b][3]
        self.NoiseCollectionType =    self.Presets[n][4][b][0]
        self.NoiseCollectionCoord =   self.Presets[n][4][b][4]
        self.NoiseActive =            self.Presets[n][4][b][5]

class HairMainOperator(bpy.types.Operator): 
    bl_label = "Generate Hair by object"
    bl_idname = "object.hair"
    bl_options = {'REGISTER', 'UNDO'}
    
    Count: bpy.props.IntProperty(name="Count", default=4, min=1, max=1000)
    Ditale: bpy.props.IntProperty(name="Fractal", default=3, min=2, max=1000)
    MainActive: bpy.props.BoolProperty(name="")
    Smooth: bpy.props.FloatProperty(name="Smooth", default=0, min=0, max=1)
    
    HairRadius: bpy.props.FloatProperty(name="Hair size", default=0.01, min=0.0001, max=2)
    NoiseUv: bpy.props.FloatProperty(name="Noise", default=1, min=0, max=1)
    SizeUv: bpy.props.FloatProperty(name="Hair uv size", default=1, min=0, max=2)
    LenghtMax: bpy.props.FloatProperty(name="Max lenght", default=1, min=0, max=1)
    LenghtMin: bpy.props.FloatProperty(name="Min lenght", default=1, min=0, max=1)
    LenghtPow: bpy.props.FloatProperty(name="Lenght range", default=1, min=0.001, max=2)
    
    NoiseHight: bpy.props.FloatProperty(name="Noise hight", default=1, min=0.001, max=1)
    NoisePower: bpy.props.FloatProperty(name="Noise power", default=0.2, min=0.001, max=1)
    HoiseSize: bpy.props.FloatProperty(name="Hoise size", default=0.2, min=0.001, max=5)
    NoiseCollectionType: bpy.props.EnumProperty( name="Type", items=( ('default', "Gradient", '1', '', 0), ('voron','Voronoise','1','', 1) ) )
    NoiseCollectionCoord: bpy.props.EnumProperty( name="Coordinate", items=( ('xyz', "XYZ", '1', '', 0), ('id','CiHiVi','1','', 1) ) )
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
    
    string = bpy.props.StringProperty(name="curve")
    
    
    MainCollectionTypeHair: bpy.props.EnumProperty( name="Type", items=( ('vertex', "Object", '1', '', 0), ('curves','Curves','1','', 1) ) )
    #MainCollectionSeparate: bpy.props.EnumProperty( name="Separation", items=( ('not', "Do not separation", '1', '', 0), ('all','All materials','1','', 1), ('one','By ID','2','', 2) ) )
    
    MainCollectionSeparate: bpy.props.IntProperty(name="Fractal", default=0, min=-1, max=100)
    MainButtonSeparateLeft: bpy.props.BoolProperty(name="")
    MainButtonSeparateRight: bpy.props.BoolProperty(name="")
    
    
    
    
    Presets = [ [ ["vertex",0], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ],1, 0.,0.01 ] ];
    
    lines = [];
    vertexMap = [];
    
    def execute(self, context):
        scene = context.scene
        maps = context.active_object
        mod = bpy.context.mode;
        floor = "f";
        selectObject = [];
        
        if 1 :
            if len(self.lines) == 0 :
                self.lines = HairAddonBody.HairLines(maps, "f", mod);
            
            
            for Hairs in range(len(self.Presets)) :
                if Hairs == self.MainButtonNumber-1 :
                    types = self.MainCollectionTypeHair
                    #self.MainCollectionSeparate
                    #self.Smooth
                    count = self.Count
                    ditale = self.Ditale
                    RangeUv = self.NoiseUv
                    SizeUv  = self.SizeUv
                    LenghtMax = self.LenghtMax
                    LenghtMin = self.LenghtMin
                    LenghtPow = self.LenghtPow
                    use = self.MainActive
                    size = self.HairRadius
                else :
                    types = self.Presets[Hairs][0][0]
                    count = self.Presets[Hairs][1][0]
                    ditale = self.Presets[Hairs][1][1]
                    RangeUv = self.Presets[Hairs][2][0]
                    SizeUv  = self.Presets[Hairs][2][1]
                    LenghtMax = self.Presets[Hairs][3][0]
                    LenghtMin = self.Presets[Hairs][3][1]
                    LenghtPow = self.Presets[Hairs][3][2]
                    use = self.Presets[Hairs][5]
                    size = self.Presets[Hairs][7]
                    
                if use :
                    if types == "vertex":
                        me = bpy.data.meshes.new(maps.name+" Hair")
                    else :
                        me = bpy.data.curves.new("HairCurve", "CURVE")
                        me.dimensions = '3D'
                        me.resolution_u = 1;
                        me.bevel_depth = 0.01;
                        me.bevel_resolution = 0;

                        
                    vert = bpy.data.objects.new(maps.name+" Hair", me) 
                    vert.location = maps.location
                    context.collection.objects.link(vert)
                    
                    selectObject.append(vert)
                    
                    if types == "vertex":
                        self.vertexMap = HairAddonBody.GenerateHairVertexMap(vert, maps, self.lines, [count, ditale], mod)
                        
                        HairAddonBody.VertexSetPose(maps, vert, self.lines, self.vertexMap, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], mod );
                        
                    else :
                        self.vertexMap =  HairAddonBody.GenerateHairCurveMap(vert, maps, self.lines, [count, ditale], mod)
                        c = [];
                        for a in self.vertexMap :
                            c = HairAddonBody.CurvePose(maps, vert, self.lines, a, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], mod );
                            HairAddonBody.makeSpline(vert.data, "BEZIER", c , size)
                    
            for sel in range(len(selectObject)) :
                if sel == self.MainButtonNumber-1 :
                    selectObject[sel].select_set(True)
                else :
                    selectObject[sel].select_set(False)
                #HairAddonBody.CurveSetPose(maps, vert, self.lines, self.vertexMap, self.SizeUv, [self.LenghtMin, self.LenghtMax, self.LenghtPow ], self.NoiseUv, [self.NoiseHight, self.NoisePower,self.HoiseSize], mod );
        return {'FINISHED'}
    
    def draw(self, context):
        
        layout = self.layout
        row = layout.row()
        
        row.label(text="Hair collection: ")
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
        row.label(text="This collection hair main setings: ")
        
        row = layout.row()
        row.prop(self, "MainCollectionTypeHair");
        self.Presets[self.MainButtonNumber-1][0][0] = self.MainCollectionTypeHair;
        row = layout.row()
        if "curves" == self.MainCollectionTypeHair :
            row.prop(self, "HairRadius");
            self.Presets[self.MainButtonNumber-1][7] = self.HairRadius;
            row = layout.row()
        
        e = context.active_object.material_slots
        row = (layout.box()).row()
        row = row.split(factor=0.1, align=True)
        if Buttons.MainButtonSeparateLeft(row, self) :
            self.MainCollectionSeparate -= 1;
        row = row.split(factor=0.1, align=True)
        if Buttons.MainButtonSeparateRight(row, self) :
            if len(e) > self.MainCollectionSeparate : 
                self.MainCollectionSeparate += 1;
        self.Presets[self.MainButtonNumber-1][0][1] = self.MainCollectionSeparate;
        if self.MainCollectionSeparate == -1 :
            row.label(text = "No Separate Object")
        if self.MainCollectionSeparate == -0 :
            row.label(text = "Separate All Material")
        if self.MainCollectionSeparate > 0 :
            if len(e) > self.MainCollectionSeparate-1 : 
                row.label(text = "Only "+e[self.MainCollectionSeparate-1].name)
        
        row = (layout.box()).row()
        row = row.split(factor=0.5, align=True)
        row.prop(self, "Count")
        self.Presets[self.MainButtonNumber-1][1][0] = self.Count;
        row.prop(self, "Ditale")
        self.Presets[self.MainButtonNumber-1][1][1] = self.Ditale;
        
        row = layout.row()
        row.prop(self, "Smooth", text="Use")
        self.Presets[self.MainButtonNumber-1][6] = self.Smooth;
        
        row = layout.row()
        row.prop(self, "MainActive", text="Use")
        self.Presets[self.MainButtonNumber-1][5] = self.MainActive;
        
        row = layout.row()
        row = (layout.box()).row()
        row = row.split(factor=0.5, align=True)
        row.prop(self, "NoiseUv")
        self.Presets[self.MainButtonNumber-1][2][0] = self.NoiseUv;
        row.prop(self, "SizeUv", translate=True)
        self.Presets[self.MainButtonNumber-1][2][1] = self.SizeUv;
        
        row = layout.row()
        row = (layout.box()).row()
        row = row.split(factor=0.333, align=True)
        row.prop(self, "LenghtMax")
        self.Presets[self.MainButtonNumber-1][3][0] = self.LenghtMax;
        row.prop(self, "LenghtMin")
        self.Presets[self.MainButtonNumber-1][3][1] = self.LenghtMin;
        row.prop(self, "LenghtPow")
        self.Presets[self.MainButtonNumber-1][3][2] = self.LenghtPow;
        
        row = layout.row()
        
        row.label(text="Hair noise collection: ")
        row = (layout.box()).row()
        
        row = row.split(factor=0.1, align=True)
        if Buttons.NoiseButtonAdd(row, self) :
            AddDeformPreset(self.Presets[self.MainButtonNumber-1]);
            ReSetControlNoise(self);
            self.NoiseButtonNumber = self.NoiseButtonCount;
        
        row = row.split(factor=0.1, align=True)
        if Buttons.NoiseButtonDel(row, self) :
            if self.NoiseButtonCount > 0 :
                self.NoiseButtonNumber -= 1;
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
            row = row.split(factor=0.5, align=True)
            row.prop(self, "NoiseCollectionType")
            row = layout.row()
            row = row.split(factor=0.5, align=True)
            row.prop(self, "NoiseCollectionCoord")
            row = layout.row()
            row = row.split(factor=0.5, align=True)
            row.prop(self, "NoiseHight")
            row = layout.row()
            row = row.split(factor=0.5, align=True)
            row.prop(self, "NoisePower")
            row = layout.row()
            row = row.split(factor=0.5, align=True)
            row.prop(self, "HoiseSize")
            row = layout.row()
            row.prop(self, "NoiseActive", text="Use")
            
            
            self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][5] = self.NoiseActive;
            self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][4] = self.NoiseCollectionCoord;
            self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][1] = self.NoiseHight;
            self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][2] = self.NoisePower;
            self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][3] = self.HoiseSize;
            self.Presets[self.MainButtonNumber-1][4][self.NoiseButtonNumber-1][0] = self.NoiseCollectionType;
            
            for i in range( len( self.Presets[self.MainButtonNumber-1][4] ) -self.NoiseButtonNumber) :
                row = (layout.box()).row()
                row.label(text = "Number "+str(i+self.NoiseButtonNumber+1)+", Type "+ self.Presets[self.MainButtonNumber-1][4][i+self.NoiseButtonNumber][0]+", Size "+str(math.floor( self.Presets[self.MainButtonNumber-1][4][i+self.NoiseButtonNumber][1]*10)/10))
        
    def ttt(self) :
        print("test")
    def invoke(self, context, event):
        self.Presets = [ [ ["vertex",0], [10, 4], [1.,1.1], [1.,0.7,1.7], [  ],1,0.,0.01  ] ];
        self.MainButtonCount = 0;
        self.MainButtonNumber = 0;
        self.NoiseButtonCount = 0;
        self.NoiseButtonNumber = 0;
        ReSetControlPresets(self);
        self.lines = [];
        self.vertexMap = [];
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