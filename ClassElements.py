import os

class Directory:

    def __init__(self, path= os.getcwd(), deep = 0, *content):
        
        '''
        self.name -> Name of directory
        self.path -> Path or URL of directory
        self.subdirectory/files -> List of directories/files what are in self.path
        self.size -> Total size of that directoty
        self.deep -> Distance what are to root folder
        '''
        self.name = path.split('/')[-1] 
        self.path = path
        self.sub_directories = []
        self.files = []
        self.size = None
        self.deep = deep
        
        if (not len(content) & len(os.listdir())>0): content= os.listdir()

        for element in content:
            assert type(element) is str

            os.chdir(self.path)
            
            tempDir = {
                'newPath': self.path + '/' + element,
                'newDeep': self.deep + 1,
            }

            if not('.' in element): 
 
                
                os.chdir(tempDir['newPath'])
    
                try:
                    self.sub_directories.append(Directory(tempDir['newPath'], tempDir['newDeep'], *os.listdir()))

                except NotADirectoryError:
                    self.files.append(File(tempDir['newPath'], tempDir['newDeep']))

            else: 
                self.files.append(File(tempDir['newPath'], tempDir['newDeep']))

    def __str__(self):
        
        TAB = '\t'
        SPACE = '\n'
        toPrint = self.deep * TAB + self.name + SPACE

        for folder in self.sub_directories:
            toPrint += Directory.__str__(folder)
        
        for file in self.files:
            toPrint += File.__str__(file)

        return toPrint

class File:
    
    def __init__(self, path, deep=0):
        
        self.name = path.split('/')[-1]   
        self.path = path
        self.size = None
        self.deep = deep

    def __str__(self):

        return self.deep*'\t'+ self.name + '\n'
