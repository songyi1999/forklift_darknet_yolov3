import  os
import  glob

    # 1. Get all the images
def  getimageallpath( dirpath,savefile):
    imagepathlist= glob.glob( dirpath +  '/*' )
    
    with  open(savefile,  'w' ) as  f:
        for  imagepath in  imagepathlist:
            f.write(imagepath +  '\n' )
    print( 'Done' )

getimageallpath( '/home/songyi/worker/123/forklift/forklift/train/images' ,'train.txt' )

getimageallpath( '/home/songyi/worker/123/forklift/forklift/test/images' ,'test.txt' )