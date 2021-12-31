
class ObjData(object):

    def __init__(self) -> None:
        super().__init__()
        self.vertices = None
        self.normals = None
        self.texCoords = None
        self.tangents = None
        self.indices = None


class ObjLoader(object):

    @staticmethod
    def loadFromFile(fileName):
        with open(fileName, "r") as file:
            lines = file.readlines()
            temp_vertices = []
            temp_normals = []
            temp_texCoords = []
            vertex_indices = []
            normal_indices = []
            texCoord_indices = []
            for line in lines:
                line = line.strip()
                if line.startswith("#"):
                    continue
                if line == "":
                    continue
                if line.startswith("v "):
                    temp = line.replace("v ", "")
                    temp = temp.split(" ")
                    temp_vertices += [float(temp[0]),
                                      float(temp[1]), float(temp[2])]

                if line.startswith("vn "):
                    temp = line.replace("vn ", "")
                    temp = temp.split(" ")
                    temp_normals += [float(temp[0]),
                                     float(temp[1]), float(temp[2])]
                if line.startswith("vt "):
                    temp = line.replace("vt ", "")
                    temp = temp.split(" ")
                    temp_texCoords += [float(temp[0]), float(temp[1])]
                if line.startswith("f "):
                    temp = line.replace("f ", "")
                    tris = temp.split(" ")
                    for tri in tris:
                        tri = tri.split("/")
                        vertex_indices += [int(tri[0]) - 1]
                        texCoord_indices += [int(tri[1]) - 1]
                        normal_indices += [int(tri[2]) - 1]

            print("done loading")

            # vertices = []
            # normals = []
            # texCoords = []

            # for i in vertex_indices:
            #     vertices += [temp_vertices[i * 3]]
            # for i in normal_indices:
            #     normals += [temp_normals[i * 3]]
            # for i in texCoord_indices:
            #     texCoords += [temp_texCoords[i * 2]]

            objData = ObjData()
            objData.vertices = temp_vertices
            objData.normals = temp_normals
            objData.texCoords = temp_texCoords
            objData.indices = vertex_indices

            print(objData.indices[0], objData.indices[1], objData.indices[2])
            print(objData.vertices[0],
                  objData.vertices[1], objData.vertices[2])
            print(objData.vertices[3],
                  objData.vertices[4], objData.vertices[5])
            print(objData.vertices[6],
                  objData.vertices[7], objData.vertices[8])

            return objData
