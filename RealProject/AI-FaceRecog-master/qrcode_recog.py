import cv2
import numpy as np
import sys
import time
from pyzbar import pyzbar

def readQRCode(img_data):
    barcodes = pyzbar.decode(img_data)
    # Sort to get bigest one
    if len(barcodes) > 0:
        max_rect_area = 0
        top = 0
        left = 0
        width = 0
        height = 0
        data = ''
        for barcode in barcodes:
            (x, y, w, h) = barcode.rect
            if w*h > max_rect_area:
                top = y
                left = x
                width = w
                height = h
                data = barcode.data.decode("utf-8")
        
        return (top, left, width, height, data)
    return None
