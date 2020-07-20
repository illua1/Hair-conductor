


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
import mathutils


OperatorText = [];

OperatorText.append("Hair base group ");
OperatorText.append("Yor neded made vertex groun on hair floor polygones!");
OperatorText.append("Need add material to object");
OperatorText.append("Hair collection: ");
OperatorText.append("Delet thes or add new (count ");
OperatorText.append("Hair preset number ");
OperatorText.append("This collection hair main setings: ");
OperatorText.append("No Separate Object");
OperatorText.append("Separate All Material");
OperatorText.append("Only ");
OperatorText.append("No bone");
OperatorText.append("Bone number ");
OperatorText.append("All hair");
OperatorText.append("Use");
OperatorText.append("Prewiev hair setingt");
OperatorText.append("View full object");
OperatorText.append("Hair deform collection: ");
OperatorText.append("Delet thes or add new (count ");
OperatorText.append("Deformer number ");
OperatorText.append("Number ");
OperatorText.append("Final hair setingt");
OperatorText.append("Bone list");
OperatorText.append("Delet thes or add new (count ");
OperatorText.append("Bone preset number ");
OperatorText.append("Only ");
OperatorText.append("All hair");


ConsoleText = [];

ConsoleText.append("-Separate object to hair elements");
ConsoleText.append("-Separate object to hair elements ");
ConsoleText.append("-Start generate hair");
ConsoleText.append("-Solving object part");

ConsoleText.append("-Generate vertex for haer element ");
ConsoleText.append("-Generate vertex for haer element ");
ConsoleText.append("-Set vertex grop");
ConsoleText.append("-Generate vertex for haer element ");
ConsoleText.append("-Made spline hair ");


DeformNames = []

DeformNames.append(["Gradient noise","Gradient noise deform by hair data"])
DeformNames.append(["XYZ Noise","Gradient noise deform by hair cord"])
DeformNames.append(["Voronoise","Voronoise noise use"])
DeformNames.append(["Round","Not worcking!"])
DeformNames.append(["Resize","Use for reset size uv xy"])
DeformNames.append(["Rotate","Use for rotate hair"])


########################################

def MainButtonLeft(row, self) :
    row.prop(self, "MainButtonLeft",icon="TRIA_LEFT")
    if self.MainButtonLeft == 1 :
        self.MainButtonLeft = 0;
        return 1;
    
def MainButtonRight(row, self) :
    row.prop(self, "MainButtonRight",icon="TRIA_RIGHT")
    if self.MainButtonRight == 1 :
        self.MainButtonRight = 0;
        return 1;
def MainButtonDel(row, self) :
    row.prop(self, "MainButtonDel",icon="X")
    if self.MainButtonDel == 1 :
        self.MainButtonDel = 0;
        return 1;
def MainButtonAdd(row, self) :
    row.prop(self, "MainButtonAdd",icon="ADD")
    if self.MainButtonAdd == 1 :
        self.MainButtonAdd = 0;
        return 1;



def NoiseButtonTop(row, self) :
    row.prop(self, "NoiseButtonTop",icon="TRIA_UP")
    if self.NoiseButtonTop == 1 :
        self.NoiseButtonTop = 0;
        return 1;
    
def NoiseButtonDown(row, self) :
    row.prop(self, "NoiseButtonDown",icon="TRIA_DOWN")
    if self.NoiseButtonDown == 1 :
        self.NoiseButtonDown = 0;
        return 1;
def NoiseButtonDel(row, self) :
    row.prop(self, "NoiseButtonDel",icon="X")
    if self.NoiseButtonDel == 1 :
        self.NoiseButtonDel = 0;
        return 1;
def NoiseButtonAdd(row, self) :
    row.prop(self, "NoiseButtonAdd",icon="ADD")
    if self.NoiseButtonAdd == 1 :
        self.NoiseButtonAdd = 0;
        return 1;

def NoiseButtonSetTop(row, self) :
    row.prop(self, "NoiseButtonSetTop",icon="SORT_DESC")
    if self.NoiseButtonSetTop == 1 :
        self.NoiseButtonSetTop = 0;
        return 1;
def NoiseButtonSetDown(row, self) :
    row.prop(self, "NoiseButtonSetDown",icon="SORT_ASC")
    if self.NoiseButtonSetDown == 1 :
        self.NoiseButtonSetDown = 0;
        return 1;

def MainButtonSeparateLeft(row, self) :
    row.prop(self, "MainButtonSeparateLeft",icon="TRIA_LEFT")
    if self.MainButtonSeparateLeft == 1 :
        self.MainButtonSeparateLeft = 0;
        return 1;
    
def MainButtonSeparateRight(row, self) :
    row.prop(self, "MainButtonSeparateRight",icon="TRIA_RIGHT")
    if self.MainButtonSeparateRight == 1 :
        self.MainButtonSeparateRight = 0;
        return 1;

  
def DomenButtonBuild(row, self) :
    row.prop(self, "DomenButtonBuild",icon="IMPORT")
    if self.DomenButtonBuild == 1 :
        #self.DomenButtonBuild = 0;
        return 1;

def DomenButtonBuildLeft(row, self) :
    row.prop(self, "DomenButtonBuildLeft",icon="TRIA_LEFT")
    if self.DomenButtonBuildLeft == 1 :
        self.DomenButtonBuildLeft = 0;
        return 1;

def DomenButtonBuildRight(row, self) :
    row.prop(self, "DomenButtonBuildRight",icon="TRIA_RIGHT")
    if self.DomenButtonBuildRight == 1 :
        self.DomenButtonBuildRight = 0;
        return 1;



def DomenButtonViews(row, self) :
    g = self.DomenButtonViews
    
    if self.DomenButtonViews == 1 :
        row.prop(self, "DomenButtonViews",icon="HIDE_ON")
    
    else :
        row.prop(self, "DomenButtonViews",icon="HIDE_ON")
    
    if not g == self.DomenButtonViews :
        return 1;





    
def BoneButtonLeft(row, self) :
    row.prop(self, "BoneButtonLeft",icon="TRIA_LEFT")
    if self.BoneButtonLeft == 1 :
        self.BoneButtonLeft = 0;
        return 1;

  
def BoneButtonRight(row, self) :
    row.prop(self, "BoneButtonRight",icon="TRIA_RIGHT")
    if self.BoneButtonRight == 1 :
        self.BoneButtonRight = 0;
        return 1;

def BoneButtonAdd(row, self) :
    row.prop(self, "BoneButtonAdd",icon="ADD")
    if self.BoneButtonAdd == 1 :
        self.BoneButtonAdd = 0;
        return 1;

def BoneButtonDel(row, self) :
    row.prop(self, "BoneButtonDel",icon="X")
    if self.BoneButtonDel == 1 :
        self.BoneButtonDel = 0;
        return 1;
# BoneButtonCount BoneButtonNumber
# BoneButtonUseDinamick BoneButtonDitale BoneButtonSepaateMaterials

# [ -1, 0, 5 ]



    
def BoneButtonSepaateLeft(row, self) :
    row.prop(self, "BoneButtonSepaateLeft",icon="TRIA_LEFT")
    if self.BoneButtonSepaateLeft == 1 :
        self.BoneButtonSepaateLeft = 0;
        return 1;

  
def BoneButtonSepaateRight(row, self) :
    row.prop(self, "BoneButtonSepaateRight",icon="TRIA_RIGHT")
    if self.BoneButtonSepaateRight == 1 :
        self.BoneButtonSepaateRight = 0;
        return 1;

    
def MainButtonBoneLeft(row, self) :
    row.prop(self, "MainButtonBoneLeft",icon="TRIA_LEFT")
    if self.MainButtonBoneLeft == 1 :
        self.MainButtonBoneLeft = 0;
        return 1;

  
def MainButtonBoneRight(row, self) :
    row.prop(self, "MainButtonBoneRight",icon="TRIA_RIGHT")
    if self.MainButtonBoneRight == 1 :
        self.MainButtonBoneRight = 0;
        return 1;



#########################################################################

def lerp(a, b, x) :
    e = [0,0,0];
    for i in range(len(a))  :
        e[i] = a[i] + ((b[i] - a[i]) * x );
    return e;
def unlerp(a,b,x) :
    return (x-a) / (b-a)
def fract(x) :
    return x-math.floor(x)

def lenght(a, b) :
    return math.pow( math.pow( a[0] - b[0], 2 )+math.pow( a[1] - b[1], 2 )+math.pow( a[2] - b[2], 2 ), 0.5);

def GetRandomX(uvs) :
    vec = mathutils.Vector((uvs[0],uvs[1],uvs[2]));
    return mathutils.noise.fractal(vec,0,0.1,1)+0.5;

def GetAllActive(e) :
    a = [];
    for i in e :
        if i.select :
            a.append(i.index);
    return a;

def allSelect(poly, i) :
    for p in poly :
        for e in i :
            if p.index == e :
                p.select = 1; 
def noCopiList(l) :
    a = [];
    for line in l :
        yes = 1;
        for e in a :
            if line[3] == e :
                yes = 0;
        if yes :
            a.append(line[3])
    return a;

def GetMinDest(l) :
    a = [];
    
    for i in range(4) :
        a.append( [ l[0][i-1], l[1][i] ] )
    f = 0;
    id = 0;
    for g in range(len(a)) :
        if a[g][0] < f :
            f == a[g][0]
            id = g
    return a[id];

def SeparateLineToMaterial(lines, indexe) :
    a = []
    for e in indexe :
        a.append([]);
    for line in lines :
        a[ indexInArr(line[3],indexe) ].append(line);
    return a;

def indexInArr(e, list) :
    g = 0;
    for i in range(len(list)) :
        if list[i] == e :
            g = i
    return g;

def indexInArrTho(e, list, r) :
   # g = 0;
    for i in range(len(list)) :
        if list[i][r] == e :
            return i;
            break;
        

def GetObjectPart(poly, mod) :
    Group = [];
    worckPart = [];
    print(ConsoleText[0]);
    n = 0;
    for rrrr in poly :
        n += 1;
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode=mod)
        if len(worckPart) == 0 :
            poly[0].select = 1;
        else :
            poly[worckPart[0]].select = 1;
        worckPart = [];
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_linked(delimit={'SEAM'})
        bpy.ops.object.mode_set(mode=mod)
        Group.append( GetAllActive(poly) );
        for t in Group :
            allSelect(poly, t );
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='INVERT')
        bpy.ops.object.mode_set(mode=mod)
        worckPart = GetAllActive(poly);
        if len(worckPart) == 0 :
            break;
        
        print(ConsoleText[1],n);
    return Group;

def conectedVertexe(obj, l, v) :
    for e in obj.data.edges :
        for i in [0, 1] :
            if e.vertices[i] == l :
                if e.vertices[1-i] == v :
                    return 1;
    return 0;

def sortLineToEdgs(obj, id, line) :
    a = [-1, id]; 
    b = -1;
    for l in range(len(line)) :
        if line[l] == id :
            b = l
    if not b == -1 :
        del line[b];
    end = line[:];
    yes = 1;
    for eee in obj.data.vertices :
        y = -1;
        for i in range(len(end)) :
            if not end[i] == a[len(a)-2] :
                if conectedVertexe(obj, end[i], a[len(a)-1]):
                    y = i;
        if not y == -1 :
            a.append(end[y]);
            del end[y];
        if len(end) == 0 :
            yes = 0;
            break;
    del a[0];
    return a;

def GetPolyProp(poly, VertList) : # ----------------
    a = 10;
    xy = [ [[0,1],[2,3]], [[1,2],[3,0]] ]
    f = []
    for e in xy : 
        g = [];
        for i in e : 
            s = [];
            for t in i : 
                p = [];
                p.append(poly.vertices[ VertList[t] ].co.x)
                p.append(poly.vertices[ VertList[t] ].co.y)
                p.append(poly.vertices[ VertList[t] ].co.z)
                s.append(p)
            g.append(lenght(s[0],s[1]));
        f.append(g[0] + g[1]);
    a = f[0] / f[1]
    size = f[0] + f[1]
    #print(a);
    return [a,size];

def GetLine(obj, poly, id, mod) :
    a = [];
    floorPoly = 0;
    floor = [];
    for p in poly :
        end = 0
        for v in obj.data.polygons[p].vertices :
            for g in obj.data.vertices[v].groups :
                if id == g.group :
                    end += 1;
        if end == 4 :
            for v in obj.data.polygons[p].vertices :
                floor.append( v );
            floorPoly = p;
    
    floor = sortLineToEdgs(obj, floor[0], floor[:])[:];
    ban = [];
    for f in floor :
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.mode_set(mode=mod)
        loop = -1;
        for e in obj.data.edges :
            yes = 1;
            for bb in ban :
                if bb == e.index :
                    yes = 0;
            if yes :
                
                for i in [0,1] :
                    if e.vertices[i] == f :
                        for ff in floor :
                            if e.vertices[1-i] == ff :
                                yes = 0
                        if yes :
                            loop = e.index;
        if not loop == -1:
            ban.append(loop);
            obj.data.edges[loop].select = 1;
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.loop_multi_select(ring=False)
            bpy.ops.object.mode_set(mode=mod)
            line = GetAllActive(obj.data.vertices);
            line = sortLineToEdgs(obj, f, line);
            a.append(line);
    #inf(obj.data.materials[ obj.data.polygons[floorPoly].material_index ])
    
    #if len (obj.data.materials) > 0 :
    materials = bpy.data.materials[ obj.data.materials[ obj.data.polygons[floorPoly].material_index ].name ].name
    #else :
    #    materials = -1
    #inf(materials)
    prop = GetPolyProp(obj.data, floor);
    
    return [a,floorPoly,prop, materials];

def GetIdOnDistList(d, o) :
    v = o[:];
    g = o[:]
    v.append(d);
    g.append(-1);
    v.sort();
    c = 0;
    
    for i in range(len(g)) :
        if not v[i] == g[i] :
            c = i;
            break
    x = ( d - g[c-1] ) / ( g[c] - g[c-1] )
    return [c-1, c, x];

def GetIdOnBezList(id, oldLine) :
    bezId = [];
    
    dist = [];
    g = 0;
    
    if id[2] < 0.5 :
        d = id[0]
        l = id[2]+0.5
        
    else :
        d = id[1]
        l = id[2]-0.5
    
    if d == 0 :
        elem = [d,d,d+1];
    else :
        if d == len(oldLine)-1 :
            elem = [d-1,d,d];
        else :
            elem = [d-1,d,d+1];
    
    l1 = lerp(oldLine[elem[0]], oldLine[elem[1]], 0.5)
    l2 = lerp(oldLine[elem[1]], oldLine[elem[2]], 0.5)
    
    p1 = lerp(l1, oldLine[elem[1]], l)
    p2 = lerp(oldLine[elem[1]], l2, l)
    
    bezId = lerp(p1, p2, l);
    
    return bezId;

def SetHairVertexCord(oldLine, dol, size, Smooth) :
    vert = mathutils.Vector((1.0, 2.0, 3.0))
    
    d = dol * oldLine[1][1] * size;
    id = GetIdOnDistList(d, oldLine[1][2]);
    
    if not id[1] < len(oldLine[0]) :
        id[1] -= 1;
    
    bezId = GetIdOnBezList(id, oldLine[0])
    
    cord = lerp( oldLine[0][id[0]], oldLine[0][id[1]], id[2] );
    cord = lerp(cord, bezId, Smooth)
    
    vert.x = cord[0];
    vert.y = cord[1];
    vert.z = cord[2];
    
    return vert;
    
def VertexNoise(cord, inf, setings, p) :
    vertex = mathutils.Vector((0, 0, 0))
    if inf > setings[0] :
        d = unlerp(setings[0], 1, inf)
        d = math.pow(d, p)
        s = lerp([0], [setings[1]], d)[0];
        #print(1)
        vertex = mathutils.noise.noise_vector(cord*20 * setings[2]) * s   ;
    return vertex;

def rotateXY(pos, r) :#(gort, ruv[2], ruv[2], NoiseHight, NoisePower, NoiseGrowth);
    a = [0,0]
    a[0] = pos[0]*math.cos(r) + pos[1]*math.sin(r)
    a[1] = pos[1]*math.cos(r) - pos[0]*math.sin(r)
    return a;

def VertexSetPose(map, obj, lines, vertMap, uvSize, HairLenRange, noise, noiseGroup, Smooth,TestingActive,mod, type, GenUse) :
    a= [];
    
    for v in vertMap :
        if type == "curve" :
            vert = mathutils.Vector((1.0, 2.0, 3.0))
        else :
            vert = obj.data.vertices[v[0]].co
        uvs = GetHairUvS( v[2], lines[ v[1] ][2], HairLenRange, uvSize, noise );
        if not type == "curve" :
            a.append(uvs[2] * v[3])
        if not v[4] == 0 :
            ruv = [uvs[0], uvs[1], v[3], v[1]/v[4], uvs[2]]
        else :
            ruv = [uvs[0], uvs[1], v[3], 1, uvs[2]]
        cord = mathutils.Vector((0, 0, 0))
        if len(noiseGroup) == 0:
            oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], ruv[0:2]);
            cord.xyz = SetHairVertexCord(oldLine, v[3], ruv[4], Smooth).xyz;
        else :
            oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], ruv[0:2]);
            cord.xyz = SetHairVertexCord(oldLine, v[3], ruv[4], Smooth).xyz;
        for ieni in range(len(noiseGroup)) :
            noiseParametr = noiseGroup[ieni];
            yes = 1;
            if (TestingActive[0]==ieni)*TestingActive[1]  :
                NoiseHight = TestingActive[2].NoiseHight
                NoisePower = TestingActive[2].NoisePower
                NoiseSize = TestingActive[2].NoiseSize
                NoiseGrowth = TestingActive[2].NoiseGrowth
                NoiseSpace = [TestingActive[2].NoiseSpace[0],TestingActive[2].NoiseSpace[1],TestingActive[2].NoiseSpace[2]]
                NoiseCollectionType = TestingActive[2].NoiseCollectionType
                NoiseActive = TestingActive[2].NoiseActive
                yes = 0;
            else :
                NoiseHight = noiseParametr[1]
                NoisePower = noiseParametr[2]
                NoiseSize = noiseParametr[3]
                NoiseGrowth = noiseParametr[6]
                NoiseSpace = [noiseParametr[5][0],noiseParametr[5][1],noiseParametr[5][2]]
                NoiseCollectionType = noiseParametr[0]
                NoiseActive = noiseParametr[4]
            if NoiseActive :
                
                if NoiseHight <= ruv[2] :
                    
                    oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], ruv[0:2]);
                    newA = SetHairVertexCord(oldLine, v[3], ruv[4], Smooth).xyz;
                    
                    vv = unlerp(NoiseHight, 1, ruv[2])
                    s = math.pow(vv, NoiseGrowth)*NoisePower
                    gort = [ruv[0],ruv[1],ruv[2]][:]
                    gortV = mathutils.Vector((gort[0],gort[1],gort[2]));
                    
                    if NoiseCollectionType == "noiseXYZ" :
                        ds = mathutils.Vector(( cord.x,cord.y,cord.z)[:]);
                        vector = VertexNoise(ds, ruv[2], [NoiseHight, NoisePower, NoiseSize], NoiseGrowth);
                        gort[0] += vector.x
                        gort[1] += vector.y
                        gort[2] += vector.z
                    if NoiseCollectionType == "noiseUV" :
                        vector = VertexNoise(gortV, ruv[2], [NoiseHight, NoisePower, NoiseSize], NoiseGrowth);
                        gort[0] += vector.x
                        gort[1] += vector.y
                        gort[2] += vector.z
                    if NoiseCollectionType == "rotate" :
                        r = math.pow(vv, NoiseGrowth)*NoiseSize
                        gort[0] -= 0.5;
                        gort[1] -= 0.5;
                        gort = rotateXY(gort[0:2], ruv[2]*NoiseSize);
                        gort[0] += 0.5;
                        gort[1] += 0.5;
                    if NoiseCollectionType == "size" :
                        for i in [0,1] :
                            gort[i] -= 0.5;
                            gort[i] *= NoiseSpace[i]
                            gort[i] += 0.5;
                    if NoiseCollectionType == "round" :
                        for g in [0,1] :
                            gort[g] -= 0.5;
                        angle = gort[0] / gort[1]
                        angle = math.atan(angle);
                        x = 0;
                        if gort[1] < 0 :
                            x == 1;
                        angle += x;
                        angle /= 1;
                        angle += 0.5;
                        angle *= 0.5;
                        angle *= 1;#-----
                        angle = fract(angle)
                        angle -= 0.5;
                        angle = abs(angle);
                        angle *= 2;
                        angle -= 1;
                        angle = math.cos(angle);
                        angle *= 0.44;
                        angle += 0.5;
                        angle = 1-angle;
                        angle *= 1.9;
                        angle += 1.0;
                        
                        for g in [0,1] :
                            gort[g] *= angle;
                            gort[g] += 0.5;
                    if NoiseCollectionType == "voron" :
                        ds = mathutils.Vector(( gort[0], gort[1], 0)[:])*NoiseSize;
                        newe = GetMinDest( mathutils.noise.voronoi( ds ) )[1]/NoiseSize
                        gort[0] = newe.x
                        gort[1] = newe.y
                        
                    oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], gort);
                    newB = SetHairVertexCord(oldLine, v[3], ruv[4], Smooth).xyz;
                    cord += (newB-newA) * s
                
        vert.xyz = cord.xyz;
        
        if type == "curve" :
            a.append((vert.x, vert.y, vert.z, 1, v[3], v[4]))
    #if type == "curve" : 
    return a;
        
    
   # bpy.ops.object.select_all(action='DESELECT')
   ## obj.select_set(True)
   # bpy.ops.object.mode_set(mode='EDIT')
   # bpy.ops.object.mode_set(mode=mod)

def GetLineVertexOfUv(lineObject, Lines, uv) :
    line = [];
    corLine = [];
    for li in Lines :
        lin = [];
        for l in li :
            lin.append(lineObject.data.vertices[l].co.xyz);
        line.append(lin)
    for v in range(len(line[0])) :
        corLine.append( lerp( lerp( line[0][v], line[1][v], uv[0] ), lerp( line[3][v], line[2][v], uv[0] ), uv[1] ));
    
    dist = [];
    d = 0;
    e = [0];
    
    for i in range(len(corLine)) :
        if i < len(corLine)-1 :
            f = lenght( corLine[i], corLine[i+1] );
            dist.append( f );
            d += f;
            e.append( d );
    return [corLine, [dist,d,e] ];

def GenerateHairVertexMap(HairObject, GetLineObject, Line, HairProp, DinamickDitale, HairLenRange, uvSize, noise, mod, UsFinishPreset) :
    a = [];
    
    for HairGroup in range(len(Line)) :
        if UsFinishPreset:
            print(ConsoleText[4]+str( HairGroup ) )
        count = int(HairProp[0] * Line[HairGroup][2][1])
        for IdEveryHair in range(count) :
            if DinamickDitale :
                map = [ len(HairObject.data.vertices)-1, HairGroup, [1,1], 0, len(Line) ]
                
                uv = GetHairUvS( [IdEveryHair,count], Line[ HairGroup ][2], HairLenRange, uvSize, noise)#lines[ v[1] ][2], HairLenRange, uvSize, noise );
                
                lengehtLineHair = GetLineVertexOfUv(GetLineObject, Line[ HairGroup ][0], uv[0:2]);
                lengehtHair= lengehtLineHair[1][1] * uv[2]
                
                couneVertex = int(HairProp[1] * lengehtHair);
                if couneVertex == 1 :
                    couneVertex = 2;
            else :
                couneVertex = HairProp[1];
            for IdVertexOfHair in range(couneVertex) :
                
                HairObject.data.vertices.add(1);
                
                a.append([ len(HairObject.data.vertices)-1, HairGroup, [IdEveryHair,(count)], IdVertexOfHair/(couneVertex-1), len(Line), Line[HairGroup][1] ]);
                
                if not IdVertexOfHair == 0:
                    HairObject.data.edges.add(1);
                    HairObject.data.edges[len(HairObject.data.edges)-1].vertices = [len(HairObject.data.vertices)-1, len(HairObject.data.vertices)-2]
    
    return a;

def GenerateHairVertex111(HairObject, GetLineObject, Line, HairProp, mod, UsFinishPreset) :
    
    for HairGroup in range(len(Line)) :
        if UsFinishPreset:
            print(ConsoleText[5]+str( HairGroup ) )
        count = int(HairProp[0] * Line[HairGroup][2][1])
        for IdEveryHair in range(count) :
            
            for IdVertexOfHair in range(HairProp[1]) :
                
                HairObject.data.vertices.add(1);
                
                if not IdVertexOfHair == 0:
                    HairObject.data.edges.add(1);
                    HairObject.data.edges[len(HairObject.data.edges)-1].vertices = [len(HairObject.data.vertices)-1, len(HairObject.data.vertices)-2]

def VertexGroupSet(obj, vertMap, boneMap, VeteLenMap, UsFinishPreset) :
    
   # print(boneMap)
   # print("-----__")
   # print(vertMap)
    
    if not len(boneMap) == 0 :
    #if 0 :
        for v in range(len(vertMap)) :
            
            for l in range(len(boneMap)) :
                
                vertId = vertMap[v][0]
                vertDol = VeteLenMap[v]
                if vertMap[v][5] == boneMap[l][1] : 
                    #print( vertMap[v][5] )
                    #print( boneMap[l][1] )
                    
                    
                    
                    
                    boneCount = len( boneMap[l][0] )-1
                    
                    for c in range( boneCount ) :
                        if ((c/boneCount) <= vertDol) * (((1+c)/boneCount) >= vertDol) :
                            if UsFinishPreset:
                                print(ConsoleText[6]+str(v/vertMap))
                            g1 = obj.vertex_groups.find(boneMap[l][0][c])
                            g2 = obj.vertex_groups.find(boneMap[l][0][c+1])
                            
                            d = ( ( vertDol - (c/boneCount) ) / ( ((1+c)/boneCount) - (c/boneCount) ) )
                            
                            v1 = obj.vertex_groups[g1]
                            v2 = obj.vertex_groups[g2]
                            
                            v1.add([vertId], 1-d, "ADD")
                            v2.add([vertId],   d, "ADD")

def GenerateHairCurveMap(HairObject, GetLineObject, Line, HairProp, DinamickDitale, HairLenRange, uvSize, noise, mod, UsFinishPreset) :
    d = []
    for HairGroup in range(len(Line)) :
        if UsFinishPreset:
            print(ConsoleText[7]+str( HairGroup ) )
        if len(HairObject.data.materials) > 0 :
            materialIndex = HairObject.data.materials.find( Line[HairGroup][3] )
        else :
            materialIndex = 0;
        
        count = int(HairProp[0] * Line[HairGroup][2][1])
        for IdEveryHair in range(count) :
            a = [];
            id = 0;
            if DinamickDitale :
                map = [ id, HairGroup, [1,1], 0, len(Line) ]
                uv = GetHairUvS( [IdEveryHair,count], Line[ HairGroup ][2], HairLenRange, uvSize, noise)#lines[ v[1] ][2], HairLenRange, uvSize, noise );
                lengehtLineHair = GetLineVertexOfUv(GetLineObject, Line[ HairGroup ][0], uv[0:2]);
                lengehtHair= lengehtLineHair[1][1] * uv[2]
                couneVertex = int(HairProp[1] * lengehtHair);
                if couneVertex == 1 :
                    couneVertex = 2;
            else :
                couneVertex = int( HairProp[1] );
            for IdVertexOfHair in range(couneVertex) :
                id =+ 1;
                
                a.append([ id, HairGroup, [IdEveryHair,(count)], IdVertexOfHair/(couneVertex-1), materialIndex ]);
                
            d.append(a)
    
    
    
    
    #makeSpline(HairObject.data, "NURBS", c )
    
    return d;

def GetHairUvS(idHair, prop, HairLenRange, uvSize, noise) :
    a = [0.5,0.5,1]
    c = idHair[0] / idHair[1]
    p = math.pow(idHair[1], 0.5) * prop[0]
    a[0] = math.floor(c * p) / p
    a[1] = fract(c * p)
    f = [p, idHair[1] / p ];
    for i in [0,1] :
        a[i] *= 1+prop[0]/idHair[1];
        a[i] -= ( GetRandomX( [ idHair[0] * 0.5,i,0] )-0.5 ) * noise / f[i]
        a[i] -= 0.5;
        a[i] *= uvSize;
        a[i] += 0.5;
    r = GetRandomX( [c*100,5,0] )-0.5;
    if r > 0.001 :
        r = math.pow(r, HairLenRange[2] );
 ##   if a[2] >= 0 :
 #       a[2] = 0.1;
 #   if a[2] <= 1 :
 #       a[2] = 0.9999;
    
    a[2] = lerp([HairLenRange[0]], [HairLenRange[1]], r )[0]
 #   if a[2] >= 0 :
 #       a[2] = 0.1;
 #   if a[2] <= 1 :
#        a[2] = 0.9999;
    
    return a;

def makeSpline(cu, typ, points, size, vertexMap, aperentBone, VeteLenMap, UsFinishPreset):
    spline = cu.data.splines.new(typ)
    npoints = len(points)
    if typ == 'BEZIER':
        spline.bezier_points.add(npoints-1)
        for (n,pt) in enumerate(points):
            
            if UsFinishPreset:
                print(ConsoleText[8]+str(n/len(points)))
            bez = spline.bezier_points[n]
            #inf(bez)
            bez.handle_left_type = 'AUTO'
            bez.handle_right_type = 'AUTO'
            bez.co.x = pt[0]
            bez.co.y = pt[1]
            bez.co.z = pt[2]
            bez.radius = (1-pt[4])*size
            #inf(bez)
        if len(points) > 0 :
            if len(cu.data.materials) > 0 :
                spline.material_index = pt[5]
            
    else:
        spline.points.add(npoints-1)    # One point already exists?
        for (n,pt) in enumerate(points):
            spline.points[n].co = pt
        
    return

def GenerateBoneHairs(maps, Armature, ditale, dinamic, materisl, uslesMaterial, Line, mod) :
    a = []
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = Armature
    id = 0;
    for HairGroup in range(len(Line)) :
        if (materisl == 0) or ( (not materisl == 0) and (Line[HairGroup][3] == uslesMaterial[materisl-1]) ) :
            
            lengehtLineHair = GetLineVertexOfUv(maps, Line[ HairGroup ][0], [0.5,0.5]);
            count = ditale
            if count < 1 :
                count = 1;
            if dinamic :
                count *= lengehtLineHair[1][1];
            count = int(count)
            
            b = []
            for IdVertexOfHair in range(count) :
                
                cord1 = SetHairVertexCord( lengehtLineHair, IdVertexOfHair/count, 1, 0).xyz;
                cord2 = SetHairVertexCord( lengehtLineHair, (IdVertexOfHair+1)/count, 1, 0).xyz;
                
                bpy.ops.object.mode_set(mode='EDIT')
                bone = Armature.data.edit_bones.new("bone")
                
                bone.head = (cord1.x, cord1.y, cord1.z)
                
                bone.tail = (cord2.x, cord2.y, cord2.z)
                
                bone.name = "Bone  "+str(IdVertexOfHair)+" "+str(HairGroup)
                
                if IdVertexOfHair > 0:
                    bone.parent = Armature.data.edit_bones[ id-1 ];
                id += 1;
                b.append( bone.name )
            a.append( [ lengehtLineHair[1][1], Line[HairGroup][3], b, Line[HairGroup][1] ] )
    bpy.ops.object.mode_set(mode=mod)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = maps
    
    return [Armature.name, a];

def HairLines(input_object, intutStart_name, mod) :
    bpy.ops.wm.console_toggle()
    print(ConsoleText[2]);
    
    #floorGroupIndex = input_object.vertex_groups[intutStart_name].index;
    floorGroupIndex = intutStart_name
    
    
    VertexLine = [];
    bpy.ops.object.select_all(action='DESELECT')
    input_object.select_set(True)
    
    ObjectPart = GetObjectPart(input_object.data.polygons, mod);
    
    for part in range(len(ObjectPart)) :
        print(ConsoleText[3], str(part/len(ObjectPart)));
        VertexLine.append( GetLine(input_object, ObjectPart[part], floorGroupIndex, mod) );
    bpy.ops.wm.console_toggle()
    return VertexLine;

def GetBoneUsles(pres, id) :
    a = []
    for i in range(len(pres)) :
        if pres[i][0] == id or pres[i][0] == 0 : 
            a.append( [i, pres[i][0]] )
    return a;

#################################################################
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
        vertexMap =  GenerateHairVertexMap(vert, maps, aDe, [count, ditale], DinamickDitale, [LenghtMin, LenghtMax, LenghtPow ], SizeUv, RangeUv, mod, self.UsFinishPreset )
        VeteLenMap =  VertexSetPose(        maps, vert, aDe, vertexMap, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth, [self.NoiseButtonNumber-1,noiseYes, self], mod, "", self.UsFinishPreset);
        VertexGroupSet(vert, vertexMap, aperentBone, VeteLenMap, self.UsFinishPreset)
    else :
        vertexMap =  GenerateHairCurveMap(vert, maps, aDe, [count, ditale], DinamickDitale, [LenghtMin, LenghtMax, LenghtPow ], SizeUv, RangeUv, mod, self.UsFinishPreset)
        c = [];
        for a in vertexMap :
            c = VertexSetPose(maps, vert, aDe, a, SizeUv, [LenghtMin, LenghtMax, LenghtPow ], RangeUv, self.Presets[Hairs][4], Smooth, [self.NoiseButtonNumber-1,noiseYes, self], mod, "curve", self.UsFinishPreset);
            makeSpline(vert, "BEZIER", c , size, vertexMap, aperentBone, VeteLenMap, self.UsFinishPreset)
            
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
        
        bonesList.append(  GenerateBoneHairs(maps, Armature, ditale, dinamic, materisl, self.uslesMaterial, self.lines, mod) ) ;
        
    
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
                LinesByMatreial =  SeparateLineToMaterial(self.lines, self.uslesMaterial);
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
                self.lines =  HairLines(maps, self.DomenButtonBuildNumber, mod);
                self.BonePreset = [];
                self.BoneButtonNumber = 0;
                self.BoneButtonCount = 0;
                
            self.uslesMaterial =  noCopiList(self.lines)
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
                if  DomenButtonBuildLeft(row, self) :
                    self.DomenButtonBuildNumber -= 1;
                row = row.split(factor=0.1, align=True)
                if  DomenButtonBuildRight(row, self) :
                    if le-1 > self.DomenButtonBuildNumber :
                        self.DomenButtonBuildNumber += 1;
                row = row.split(factor=0.8, align=True)
                if not len(maps.vertex_groups) == 0 :
                    row.label(text=OperatorText[0]+maps.vertex_groups[self.DomenButtonBuildNumber].name)
                else :
                    row.label(text=OperatorText[1])
                row = row.split(factor=1, align=True)
                DomenButtonBuild(row,self)
            else :
                row.label(text=OperatorText[2], icon="SHADING_TEXTURE")
            
        else :
            
            row.prop(self, "DomenButtonViews",text="View domain ");
            #row.label(text="View domain ")
            
            row = layout.row()
            
            row.label(text=OperatorText[3], icon="HAIR_DATA")
            row = (layout.box()).row()
            
            row = row.split(factor=0.1, align=True)
            if  MainButtonAdd(row, self) :
                self.MainButtonCount += 1;
                self.MainButtonNumber = self.MainButtonCount;
                AddHairPreset(self.Presets);
                ReSetControlPresets(self);
            
            row = row.split(factor=0.1, align=True)
            if  MainButtonDel(row, self) :
                if self.MainButtonCount > 1 :
                    DelHairPreset(self.Presets, self.MainButtonNumber-1);
                    self.MainButtonCount -= 1;
                    self.MainButtonNumber -= 1;
                    ReSetControlPresets(self);
            
            row.label(text = OperatorText[4]+str(self.MainButtonCount)+")" )
        
            if self.MainButtonCount > 1:
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if  MainButtonLeft(row, self) :
                    self.MainButtonNumber -= 1;
                    ReSetControlPresets(self);
                
                row = row.split(factor=0.1, align=True)
                if  MainButtonRight(row, self) :
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
            MainButtonSeparateLeft(row, self)
            row = row.split(factor=0.1, align=True)
            MainButtonSeparateRight(row, self)
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
                MainButtonBoneLeft(row, self)
                row = row.split(factor=0.1, align=True)
                MainButtonBoneRight(row, self)
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
            if  NoiseButtonAdd(row, self) :
                AddDeformPreset(self.Presets[self.MainButtonNumber-1]);
                self.NoiseButtonCount += 1;
                self.NoiseButtonNumber = self.NoiseButtonCount;
                ReSetControlNoise(self);
            
            row = row.split(factor=0.1, align=True)
            if  NoiseButtonDel(row, self) :
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
                
                if  NoiseButtonTop(row, self) :
                    if self.NoiseButtonNumber > 1 :
                        self.NoiseButtonNumber -= 1;
                        ReSetControlNoise(self);
                row = row.split(factor=0.1, align=True)
                if  NoiseButtonDown(row, self) :
                    if self.NoiseButtonNumber < self.NoiseButtonCount :
                        self.NoiseButtonNumber += 1;
                        ReSetControlNoise(self);
                row = row.split(factor=0.6, align=True)
                row.label(text = OperatorText[16]+str(self.NoiseButtonNumber))
                
                row = row.split(factor=0.3, align=True)
                if  NoiseButtonSetTop(row, self) :
                    self.Presets[self.MainButtonNumber-1][4] = resetIdNoise(self.Presets[self.MainButtonNumber-1][4], self.NoiseButtonNumber-1, -1)
                    ReSetControlNoise(self)
                row = row.split(factor=0.4, align=True)
                if  NoiseButtonSetDown(row, self) :
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
            if  BoneButtonAdd(row, self) :
                self.BoneButtonCount += 1;
                self.BoneButtonNumber = self.BoneButtonCount
                AddBonePreset(self.BonePreset);
                ReSetControlPresets(self);
            
            row = row.split(factor=0.1, align=True)
            if  BoneButtonDel(row, self) :
                if self.BoneButtonNumber > 0 :
                    DelBonePreset(self.BonePreset, self.BoneButtonNumber-1, self.Presets);
                    self.BoneButtonCount -= 1;
                    self.BoneButtonNumber -= 1;
                    ReSetControlPresets(self);
            
            row.label(text = OperatorText[22]+str(self.BoneButtonCount)+")" )
        
            if self.BoneButtonCount > 1:
                row = (layout.box()).row()
                row = row.split(factor=0.1, align=True)
                if  BoneButtonLeft(row, self) :
                    self.BoneButtonNumber -= 1;
                    ReSetControlPresets(self);
                
                row = row.split(factor=0.1, align=True)
                if  BoneButtonRight(row, self) :
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
                if  BoneButtonSepaateLeft(row, self) :
                    self.BoneButtonSepaateMaterials -= 1;
                row = row.split(factor=0.1, align=True)
                if  BoneButtonSepaateRight(row, self) :
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