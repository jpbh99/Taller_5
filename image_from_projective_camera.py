import cv2
import json
from camera_model import *

if __name__ == '__main__':

    # intrinsics parameters
    leer = json.loads(open(r'C:\Users\juanp\Desktop\Prueba_cell\calibration_2_cell.json').read())
    fx = 1000
    fy = 1000
    width = 1280
    height = 720
    cx = width / 2
    cy = height / 2
    K = leer["K"]

    h = leer["h"]
    d = leer["d"]
    R = set_rotation(leer["tilt"], leer["pan"], 0)
    t = np.array([0, -d, h])
    
    # create camera
    camera = projective_camera(K, width, height, R, t)

    
    square_3D1 = np.array([[0, 0, 0], [1, 0, 0], [1, -1, 0], [0, -1, 0]])
    square_3D2 = np.array([[0, 0, 1], [1, 0, 1], [1, -1, 1], [0, -1, 1]])

    square_2D = projective_camera_project(square_3D1, camera)
    square_2D2 = projective_camera_project(square_3D2, camera)

    image_projective = 255 * np.ones(shape=[camera.height, camera.width, 3], dtype=np.uint8)

    cv2.line(image_projective, (square_2D[0][0], square_2D[0][1]), (square_2D[1][0], square_2D[1][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[1][0], square_2D[1][1]), (square_2D[2][0], square_2D[2][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[2][0], square_2D[2][1]), (square_2D[3][0], square_2D[3][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[3][0], square_2D[3][1]), (square_2D[0][0], square_2D[0][1]), (200, 1, 255), 3)

    cv2.line(image_projective, (square_2D2[0][0], square_2D2[0][1]), (square_2D2[1][0], square_2D2[1][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D2[1][0], square_2D2[1][1]), (square_2D2[2][0], square_2D2[2][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D2[2][0], square_2D2[2][1]), (square_2D2[3][0], square_2D2[3][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D2[3][0], square_2D2[3][1]), (square_2D2[0][0], square_2D2[0][1]), (200, 1, 255), 3)

    cv2.line(image_projective, (square_2D[0][0], square_2D[0][1]), (square_2D2[0][0], square_2D2[0][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[1][0], square_2D[1][1]), (square_2D2[1][0], square_2D2[1][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[2][0], square_2D[2][1]), (square_2D2[2][0], square_2D2[2][1]), (200, 1, 255), 3)
    cv2.line(image_projective, (square_2D[3][0], square_2D[3][1]), (square_2D2[3][0], square_2D2[3][1]), (200, 1, 255), 3)



    cv2.imshow("Image", image_projective)
    cv2.waitKey(0)
