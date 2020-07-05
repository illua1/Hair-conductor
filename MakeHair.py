import bpy;
import math
import mathutils


def inf(f):
    print();
    print(f);
    print();
    print(dir(f));
    print();
    print(type(f));
    print();

######

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

def GetObjectPart(poly, mod) :
    Group = [];
    worckPart = [];
    while 1 :
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
    while yes:
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
    del a[0];
    return a;

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
    return [a,p,floor];

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

def SetHairVertexCord(vertex, oldLine, dol, size) :
    d = dol[0] / dol[1] * oldLine[1][1] * size;
    id = GetIdOnDistList(d, oldLine[1][2]);
    
    if not id[1] < len(oldLine[0]) :
        id[1] -= 1;
    cord = lerp( oldLine[0][id[0]], oldLine[0][id[1]], id[2] );
    vertex.x = cord[0];
    vertex.y = cord[1];
    vertex.z = cord[2];
            
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

def GenerateHairVertexObject(HairObject, GetLineObject, Line, HairProp, HairLenRange, noise, uvSize, ecletSetings, mod) :
    
    for HairGroup in Line :
        floorProp = GetPolyProp(GetLineObject.data, HairGroup[2] );
        
        count = int(HairProp[0] * floorProp[1])
        for IdEveryHair in range(count) :
            uvs = GetHairUvS( [ IdEveryHair,count ], floorProp[0], HairLenRange, uvSize, noise );
            oldLine = GetLineVertexOfUv(GetLineObject, HairGroup[0], uvs[0:2]);
            #print(oldLine);
            
            for IdVertexOfHair in range(HairProp[1]) :
                HairObject.data.vertices.add(1);
                
                SetHairVertexCord(HairObject.data.vertices[-1].co, oldLine, [ IdVertexOfHair,HairProp[1]-1 ], uvs[2]);
                
                SetVertexNoise(HairObject.data.vertices[-1].co, IdVertexOfHair/HairProp[1], ecletSetings);
                
                if not IdVertexOfHair == 0:
                    HairObject.data.edges.add(1);
                    HairObject.data.edges[len(HairObject.data.edges)-1].vertices = [len(HairObject.data.vertices)-1, len(HairObject.data.vertices)-2]
    bpy.ops.object.select_all(action='DESELECT')
    HairObject.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode=mod)

def GetHairUvS(idHair, prop, HairLenRange, uvSize, noise) :
    a = [0.5,0.5,1]
    c = idHair[0]/idHair[1]
    p = math.pow(idHair[1], 0.5) * prop
    a[0] = math.floor(c * p) / p
    a[1] = fract(c * p)
    f = [p, idHair[1] / p ];
    for i in [0,1] :
        a[i] *= 1+prop/idHair[1];
        a[i] -= ( GetRandomX( [ idHair[0] * 0.5,i,0] )-0.5 ) * noise / f[i]
        a[i] -= 0.5;
        a[i] *= uvSize;
        a[i] += 0.5;
    r = GetRandomX( [c*100,5,0] )-0.5;
    if r > 0.001 :
        r = math.pow(r, HairLenRange[2] );
    a[2] = lerp([HairLenRange[0]], [HairLenRange[1]], r )[0]
    return a;

def SetVertexNoise(vertex, inf, setings) :
    
    if inf > setings[0] :
        d = unlerp(setings[0], 1, inf)
        s = lerp([0], [setings[1]], d)[0];
        #print(1)
        vertex += mathutils.noise.noise_vector(vertex*20 * setings[2]) * s  ;
    

#####

def GenerateHair(input_name, intutStart_name, output_name, HairCount, HairDitail, HairLenRange, noise, uvSize, ecletSetings) :
    print("-Start generate hair");
    obj = bpy.context.scene.objects;
    map = obj[input_name];
    floorGroupIndex = map.vertex_groups[intutStart_name].index;
    hair = obj[output_name];
    mod = bpy.context.mode;
    
    VertexLine = [];
    bpy.ops.object.select_all(action='DESELECT')
    map.select_set(True)
    
    ObjectPart = GetObjectPart(map.data.polygons, mod);
    
    for part in ObjectPart :
        VertexLine.append( GetLine(map, part, floorGroupIndex, mod) );
        #print(GetLine(map, part, floorGroupIndex, mod));
        ##print();
    
    GenerateHairVertexObject(hair, map, VertexLine, [HairCount, HairDitail], HairLenRange, noise, uvSize, ecletSetings, mod);

#GenerateHair("hair map", "floor", "hair", 200, 4, [0.7,1,0.25], 1, 1.2, [0.7, 0.5, 2] );
#GenerateHair("hair map", "floor", "hair", 100, 6, [0.2,1,0.4], 1, 1.6, [0.2, 0.3, 0.1] );
#GenerateHair("hair_map", "floor", "hair", 1, 10);

GenerateHair("maps", "f", "vert", 100, 5, [0.9,1,0.25], 1, 0.5, [0.9, 0.0, 2] );
GenerateHair("maps", "f", "vert", 170, 5, [0.6,1,0.4], 1, 1.6, [0.9, 0.2, 0.1] );
GenerateHair("maps", "f", "vert", 80, 8, [0.9,1,1.4], 1, 1.6, [0.2, 0.3, 0.1] );

GenerateHair("maps w", "f", "vert w", 80, 5, [0.9,1,0.25], 1, 0.5, [0.9, 0.0, 2] );
GenerateHair("maps w", "f", "vert w", 120, 5, [0.6,1,0.4], 1, 1.6, [0.9, 0.2, 0.1] );
GenerateHair("maps w", "f", "vert w", 60, 8, [0.9,1,1.4], 1, 1.6, [0.2, 0.3, 0.1] );


#t = 0;
#while t < 90000 :
#    t += 1;
#    print(GetRandomX([t,0,0])*0.25+0.5);