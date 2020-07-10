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

    