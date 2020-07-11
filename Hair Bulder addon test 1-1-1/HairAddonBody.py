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
    

def GetObjectPart(poly, mod) :
    Group = [];
    worckPart = [];
    print("-Separate object to hair elements");
    n = 0;
    while 1 :
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
        print("-Separate object to hair elements ",n);
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
    materials = bpy.data.materials[ obj.data.materials[ obj.data.polygons[floorPoly].material_index ].name ].name
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

def SetHairVertexCord(vertex, oldLine, dol, size, Smooth) :
    d = dol * oldLine[1][1] * size;
    id = GetIdOnDistList(d, oldLine[1][2]);
    
    if not id[1] < len(oldLine[0]) :
        id[1] -= 1;
    #print("-", id)
    #print("-", oldLine[0])
    #print("-", len(oldLine[0]))
    #print("-", len(oldLine[1]))
    
    bezId = GetIdOnBezList(id, oldLine[0])
    
    cord = lerp( oldLine[0][id[0]], oldLine[0][id[1]], id[2] );
    cord = lerp(cord, bezId, Smooth)
    vertex.x = cord[0];
    vertex.y = cord[1];
    vertex.z = cord[2];

def VertexSetPose(map, obj, lines, vertMap, uvSize, HairLenRange, noise, noiseGroup, Smooth,mod) :
    for v in vertMap :
        vert = obj.data.vertices[v[0]].co
        
        uvs = GetHairUvS( v[2], lines[ v[1] ][2], HairLenRange, uvSize, noise );
        
        if len(noiseGroup) == 0:
            oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], uvs[0:2]);
            #VertexNoise(vert, vert, v, [ defoalt[1], defoalt[2], defoalt[3] ] );
            SetHairVertexCord(vert, oldLine, v[3], uvs[2], Smooth);
        for noise in noiseGroup :
            
            oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], uvs[0:2]);
            
            SetHairVertexCord(vert, oldLine, v[3], uvs[2], Smooth);
            
            if noise[0] == "noise" :
                if noise[4] == "xyz" :
                    VertexNoise(vert, vert, v, [ noise[1], noise[2], noise[3] ] );
                if noise[4] == "id" :
                    VertexNoise(vert, mathutils.Vector((v[3], v[2][0], v[1])), v, [ noise[1], noise[2], noise[3] ] );
    
    bpy.ops.object.select_all(action='DESELECT')
    obj.select_set(True)
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.object.mode_set(mode=mod)

def CurvePose(map, obj, lines, vertMap, uvSize, HairLenRange, UvRange, noiseGroup, mod) :
    a = [];
    for v in vertMap :
        vert = mathutils.Vector((1.0, 2.0, 3.0))
        
        uvs = GetHairUvS( v[2], lines[ v[1] ][2], HairLenRange, uvSize, UvRange );
        
        oldLine = GetLineVertexOfUv(map, lines[ v[1] ][0], uvs[0:2]);
        
        SetHairVertexCord(vert, oldLine, v[3], uvs[2]);
        
        #VertexNoise(vert, v, ecletSetings);
        
        a.append((vert.x, vert.y, vert.z, 1,v[3], v[4]))
    
    return a;
 
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

def GenerateHairVertexMap(HairObject, GetLineObject, Line, HairProp, mod) :
    a = [];
    
    for HairGroup in range(len(Line)) :
        
        count = int(HairProp[0] * Line[HairGroup][2][1])
        for IdEveryHair in range(count) :
            
            for IdVertexOfHair in range(HairProp[1]) :
                
                HairObject.data.vertices.add(1);
                a.append([ len(HairObject.data.vertices)-1, HairGroup, [IdEveryHair,(count)], IdVertexOfHair/(HairProp[1]-1) ]);
                
                if not IdVertexOfHair == 0:
                    HairObject.data.edges.add(1);
                    HairObject.data.edges[len(HairObject.data.edges)-1].vertices = [len(HairObject.data.vertices)-1, len(HairObject.data.vertices)-2]
    
    return a;

def GenerateHairVertex(HairObject, GetLineObject, Line, HairProp, mod) :
    
    for HairGroup in range(len(Line)) :
        
        count = int(HairProp[0] * Line[HairGroup][2][1])
        for IdEveryHair in range(count) :
            
            for IdVertexOfHair in range(HairProp[1]) :
                
                HairObject.data.vertices.add(1);
                
                if not IdVertexOfHair == 0:
                    HairObject.data.edges.add(1);
                    HairObject.data.edges[len(HairObject.data.edges)-1].vertices = [len(HairObject.data.vertices)-1, len(HairObject.data.vertices)-2]
    

def GenerateHairCurveMap(HairObject, GetLineObject, Line, HairProp, mod) :
    d = []
    for HairGroup in range(len(Line)) :
        materialIndex = HairObject.data.materials.find( Line[HairGroup][3] )
        count = int(HairProp[0] * Line[HairGroup][2][1])
        for IdEveryHair in range(count) :
            a = [];
            id = 0;
            for IdVertexOfHair in range(HairProp[1]) :
                
                id =+ 1;
                #inf(HairObject.data.materials[ Line[HairGroup][3] ])
                #inf(HairObject.data.materials.keys)
                #materialIndex = HairObject.data.materials.find( Line[HairGroup][3] )
                
                a.append([ id, HairGroup, [IdEveryHair,(count)], IdVertexOfHair/(HairProp[1]-1), materialIndex ]);
                
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
    a[2] = lerp([HairLenRange[0]], [HairLenRange[1]], r )[0]
    return a;

def VertexNoise(vertex, cord, inf, setings) :
    
    if inf[3] > setings[0] :
        d = unlerp(setings[0], 1, inf[3])
        s = lerp([0], [setings[1]], d)[0];
        #print(1)
        vertex += mathutils.noise.noise_vector(cord*20 * setings[2]) * s  ;
    
def makeSpline(cu, typ, points, size):
    spline = cu.splines.new(typ)
    npoints = len(points)
    
    if typ == 'BEZIER':
        spline.bezier_points.add(npoints-1)
        for (n,pt) in enumerate(points):
            bez = spline.bezier_points[n]
            #inf(bez)
            bez.handle_left_type = 'AUTO'
            bez.handle_right_type = 'AUTO'
            bez.co.x = pt[0]
            bez.co.y = pt[1]
            bez.co.z = pt[2]
            bez.radius = (1-pt[4])*size
            #print(bez.radius)
        spline.material_index = pt[5]
        #inf(spline)
            
            #bez.weight_softbody = 1;
    else:
        spline.points.add(npoints-1)    # One point already exists?
        for (n,pt) in enumerate(points):
            spline.points[n].co = pt
        
    return

def HairLines(input_object, intutStart_name, mod) :
    bpy.ops.wm.console_toggle()
    print("-Start generate hair");
    
    #floorGroupIndex = input_object.vertex_groups[intutStart_name].index;
    floorGroupIndex = intutStart_name
    
    
    VertexLine = [];
    bpy.ops.object.select_all(action='DESELECT')
    input_object.select_set(True)
    
    ObjectPart = GetObjectPart(input_object.data.polygons, mod);
    
    for part in range(len(ObjectPart)) :
        print("Solving object part", str(part/len(ObjectPart)));
        VertexLine.append( GetLine(input_object, ObjectPart[part], floorGroupIndex, mod) );
    bpy.ops.wm.console_toggle()
    return VertexLine;


#inf(bpy.context.collection)

#inf(bpy.context.scene.collection)

#inf(bpy.context.scene.objects["maps"].data)
#bpy.context.active_object.name = "1"
#inf(bpy.context.active_object.name)

#t = 0;
#while t < 90000 :
#    t += 1;
#    print(GetRandomX([t,0,0])*0.25+0.5);