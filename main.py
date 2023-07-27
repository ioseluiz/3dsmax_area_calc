from pymxs import runtime as rt

def main():
  
  for obj in rt.objects:
    print(obj.name)
    rt.convertToPoly(obj)
    #rt.polyop.setFaceSelection(obj, rt.name('all'))
    rt.subObjectLevel = 4
    face_data = rt.getPolygonCount(obj)
    faces = face_data[0]
    vertices = face_data[1]
    for x in range(1,faces+1):
        rt.polyop.setFaceSelection(obj,x)
        vertices = rt.polyop.getFaceVerts(obj,x)
        print(rt.polyop.getFaceVerts(obj, x))
        for v in vertices:
            print(rt.polyop.getVert(obj, v))
        
    print("(Faces, Vertices): " + str(rt.getPolygonCount(obj)))
	
	  


if __name__ == '__main__':
  main()
  #res=pymxs.runtime.stringStream('')
  #pymxs.runtime.apropos('face',to=res)
  #print(res)