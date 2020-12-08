import numpy as np

def landmark_to_np(face_landmark):
    coords = np.zeros((face_landmark.num_parts, 2),dtype='int')
    for i in range(0, face_landmark.num_parts):
        coords[i] = (face_landmark.part(i).x, face_landmark.part(i).y)
    return coords