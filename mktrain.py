import  os
import  glob

    # 1. Get all the images
def  getimageallpath( dirpath,savefile):
    imagepathlist= glob.glob( dirpath +  '/*' )
    
    with  open(savefile,  'w' ) as  f:
        for  imagepath in  imagepathlist:
            f.write(imagepath +  '\n' )
    print( 'Done' )

getimageallpath( 'train/images' ,'train.txt' )

getimageallpath( 'test/images' ,'test.txt' )
