import cv2

class Read:

    def __init__(self, img):
        self.img = cv2.imread(img)


        cv2.destroyAllWindows()

    def preprocess(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        median = cv2.medianBlur(gray, 9)
        self.img = median

    def grid_detection(self):
        pass

    def display(self):
        cv2.namedWindow('image', cv2.WINDOW_KEEPRATIO)
        cv2.resizeWindow('image', (600,800))
        cv2.imshow("image", self.img)
        cv2.waitKey(0) & 0xFF

if __name__ == "__main__":
    img = Read("img\image_1.jpg")
    img.preprocess()
    img.display()


