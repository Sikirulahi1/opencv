import cv2 as cv

class App:
    def __init__(self):
        img = cv.imread('Photos\group.jpg')
        Window('image', img)
        
    def run(self):
        """Run the main event loop"""
        k=0
        while k != ord('q'):
            k = cv.waitKey(0)
            print(k, chr(k))
            
        cv.destroyAllWindows()
    

class Window:
    """Create window with an image"""
    def __init__(self, win, img):
        self.win = win
        self.img = img
        cv.imshow(win, img)
        
if __name__ == '__main__':
    App().run()

