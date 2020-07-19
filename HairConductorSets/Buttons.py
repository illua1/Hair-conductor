


#Code editing license.
#-You can change the code for personal use.
#-You can transfer modified code when mentioning the fact of editing, the user of the editor and the author of the add-on.
#-You cannot sell a modified addon.
#-You cannot use parts of the addon code for commercial purposes.




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
