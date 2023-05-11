import bpy
import numpy as np

# function to create photon
def create_photon(n):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.05, location=(0, 0, 0))
    # create red material
    mat = bpy.data.materials.new(name="red")
    mat.diffuse_color = (1, 0, 0, 1)
    # assign material to photon
    bpy.context.object.data.materials.append(mat)
    # set shading to smooth
    bpy.context.object.data.use_auto_smooth = True
    # set name of photon
    bpy.context.object.name = "photon" + str(n)
    return bpy.context.object

def make_plane_black(object):
    # create grey material
    mat = bpy.data.materials.new(name="black")
    mat.diffuse_color = (0.5, 0.5, 0.5, 1)
    # assign material to plane
    object.data.materials.append(mat)
    return bpy.context.object


Nx = 10
Ny = 10
N = Nx * Ny

L_x = 10 # length of plane in x direction
L_z = 10 # length of plane in z direction
focal_distance = 7.5 # distance from plane to origin

# create Nx x Ny array of planes context.object
context_arr = np.empty((Nx + 1, Ny + 1), dtype=object)

for i in np.arange(0, 1 + 1/Nx, 1/Nx):
    for j in np.arange(0, 1 + 1/Ny, 1/Ny):
        bpy.ops.mesh.primitive_plane_add(size=1, location=(-5 + j * L_x, focal_distance, 5 - i * L_z))
        bpy.context.object.dimensions = (L_x/Nx, 1, L_z/Ny)
        bpy.context.object.rotation_euler = (np.pi/2, 0, 0)
        bpy.context.object.name = "plane" + str(i) + str(j)
        context_arr[int(i*Nx), int(j*Ny)] = bpy.context.object




rate_create_photon = 8 # create photon every 10 frames

# set end frame
bpy.context.scene.frame_end = rate_create_photon * N

n=0
for i in np.arange(0, 1 + 1/Nx, 1/Nx):
    for j in np.arange(0, 1 + 1/Ny, 1/Ny):
        # create photon at time stamp rate_create_photon * n
        bpy.context.scene.frame_set(rate_create_photon * n)
        photon = create_photon(n)
        # set keyframe for location
        photon.keyframe_insert(data_path="location", frame=rate_create_photon * n)
        # move photon to position on plane and set keyframe
        photon.location = (-5 + j * L_x, focal_distance + 0.1, 5 - i * L_z)
        plane = make_plane_black(context_arr[int(i*Nx), int(j*Ny)])
        print(plane.name)
        plane.keyframe_insert(data_path="data.materials[0].diffuse_color", frame=rate_create_photon * n)
        photon.keyframe_insert(data_path="location", frame=rate_create_photon * n + rate_create_photon)
        n += 1






