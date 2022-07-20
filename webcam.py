# import the opencv library
import cv2
## create object
vid_o = cv2.VideoCapture(0)
i=0

while(True):
	
	#capture
	ret, frame = vid_o.read()

	# Display the resulting frame
	cv2.imshow('frame', frame)
	
	# the 'x' button is quit
	if cv2.waitKey(1) & 0xFF == ord('x'):
		break
cv2.imwrite('Frame'+str(i)+'.jpg', frame)
i += 1

# After the loop release the cap object
vid_o.release()
# Destroy all the windows
cv2.destroyAllWindows()
