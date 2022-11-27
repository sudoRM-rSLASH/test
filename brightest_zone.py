# Run with sample image:
## python brightest_zone.py --type darkest or brightest --image sample_image.jpg
## Optional add --radius (radius of Gaussian blur) can improve detection accuracy

import argparse
import cv2

# Add arguments
args = argparse.ArgumentParser()
args.add_argument("-t", "--type", help="find brightest or darkest zone")
args.add_argument("-i", "--image", help="path to the image file")
args.add_argument("-r", "--radius", type=int, help="radius of Gaussian blur; must be odd")
args = vars(args.parse_args())

# Read image and apply grayscale
image = cv2.imread(args.get("image"))
orig = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Set radius of Gb
radius = args.get("radius") if args.get("radius") else 41

# Apply Gaussian blur and find the brightest point
gray = cv2.GaussianBlur(gray, (radius, radius), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)

# Set type
zone = minLoc if args.get("type") == "darkest" else maxLoc

# Draw square around the brightest point
image = orig.copy()
cv2.rectangle(
    image,
    (zone[0] + 50, zone[1] + 50),
    (zone[0] - 50, zone[1] - 50),
    (255, 0, 0),
    2,
)

# Display result
cv2.imshow("Result", image)
cv2.waitKey(0)
