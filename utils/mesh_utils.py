##############################################
# Tools to deal with meshes

def center_mesh3d(M,x0,y0,z0):
    xlen = sum(M.hx)
    ylen = sum(M.hy)
    zlen = sum(M.hz)
    return [-xlen/2+x0, -ylen/2+y0, -zlen/2+z0]
