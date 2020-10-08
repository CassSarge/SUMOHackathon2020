#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LIVE DEMO
This script loads a pre-trained model (for best results use pre-trained weights for classification block)
and classifies American Sign Language finger spelling frame-by-frame in real-time
"""

import string as string_module
import cv2
import time
from processing import square_pad, preprocess_for_vgg
from model import create_model
import argparse
import numpy as np


def testing_mode(my_predict, frame, width, height, label_dict):
    ''' Will display the top three predictions for the ASL symbol in the ROI'''

    # Predict letter
    top_prd = np.argmax(my_predict)

    # Only display predictions with probabilities greater than 0.5
    if np.max(my_predict) >= 0.50:

        prediction_result = label_dict[top_prd]

        # sorts list in asceding order - therefore to get the 2nd and 3rd most likely option, we pick index -2 and -3
        preds_list = np.argsort(my_predict)[0]
        pred_2 = label_dict[preds_list[-2]]
        pred_3 = label_dict[preds_list[-3]]

        # Annotate image with most probable prediction
        cv2.putText(frame, text=prediction_result,
                    org=(width // 2, height // 2),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=17, color=(213,152,20),
                    thickness=15, lineType=cv2.LINE_AA)
        # Annotate image with second most probable prediction (displayed on bottom left)
        cv2.putText(frame, text=pred_2,
                    org=(width // 2 + width // 5, (360 + 240)),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=6, color=(97, 140, 94),
                    thickness=6, lineType=cv2.LINE_AA)
        # Annotate image with third probable prediction (displayed on bottom right)
        cv2.putText(frame, text=pred_3,
                    org=(width // 2 + width // 3 + 5, (360 + 240)),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=6, color=(97,140,94),
                    thickness=6, lineType=cv2.LINE_AA)



def demo_mode(target, my_predict, frame, width, height, label_dict):

    ''' Will display the target letter and respond with a tick, 
    self closes when the target letter is detected for a time period'''

    cv2.putText(frame, text=target,
                org=(width // 2, height // 2),
                fontFace=cv2.FONT_HERSHEY_COMPLEX,
                fontScale=17, color=(213,152,20),
                thickness=15, lineType=cv2.LINE_AA)

        # Predict letter
    top_prd = np.argmax(my_predict)
    prediction_result = label_dict[top_prd]

    # Confident we at least have a hand
    if np.max(my_predict) >= 0.50:
        # Annotate image in bottom left
        cv2.putText(frame, text=prediction_result,
                    org=(width // 2 + width // 5, (360 + 240)),
                    fontFace=cv2.FONT_HERSHEY_DUPLEX,
                    fontScale=6, color=(97, 140, 94),
                    thickness=6, lineType=cv2.LINE_AA)

        preds_list = np.argsort(my_predict)[0]
        pred_2 = label_dict[preds_list[-2]]
        pred_3 = label_dict[preds_list[-3]]

        # Display success only if target is in top 3 prediction results
        if target in (prediction_result, pred_2, pred_3):

            # Annotate image with success message
            cv2.putText(frame, text="Success!!",
                org=(width // 2 + width // 3 + 5, (360 + 240)),
                fontFace=cv2.FONT_HERSHEY_DUPLEX,
                fontScale=6, color=(97, 140, 94),
                thickness=6, lineType=cv2.LINE_AA)

    

def main():
    ap = argparse.ArgumentParser()
    required_ap = ap.add_argument_group('required arguments')
    required_ap.add_argument("-m", "--model",
                            type=str, default="mobilenet", required=True,
                            help="name of pre-trained network to use")
    ap.add_argument("-t", "--target", default = "-", help = "Target letter for demo mode")
    args = vars(ap.parse_args())

    mydict = {"TESTING": 1, "DEMO": 0}

    if args['target'].upper() not in string_module.ascii_uppercase:
        mode = mydict["TESTING"]
    else:
        mode = mydict["DEMO"]
        targetLetter = args['target'].upper()



    # ====== Create model for real-time classification ======
    # =======================================================

    # Map model names to classes
    MODELS = ["resnet", "vgg16", "inception", "xception", "mobilenet"]

    if args["model"] not in MODELS:

        string = ""
        for x in MODELS:
            string += (x)
            string += (" ")
        raise AssertionError("Model given must be one of: resnet, vgg16, inception, xceptino, mobilnet")

    # Create pre-trained model + classification block, with or without pre-trained weights
    my_model = create_model(model=args["model"], model_weights_path=None)

    # Dictionary to convert numerical classes to alphabet
    label_dict = {pos: letter
                for pos, letter in enumerate(string_module.ascii_uppercase)}


    # ====================== Live loop ======================
    # =======================================================

    # Get a frame from the default video source (the webcam in most cases) 
    video_capture = cv2.VideoCapture(0)

    fps = 0
    start = time.time()

    width = int(video_capture.get(3) + 0.5)
    height = int(video_capture.get(4) + 0.5)


    while True:
        # Capture frame-by-frame
        _, frame = video_capture.read()

        # add a frame to the fps counter
        fps += 1

        # Draw rectangle around face
        x = 313
        y = 82
        w = 451
        h = 568
        cv2.rectangle(frame, (x, y), (x + w, y + h), (213,152,20), 3)

        # Crop + process captured frame
        hand = frame[83:650, 314:764]
        hand = square_pad(hand)
        hand = preprocess_for_vgg(hand)

        # Make prediction
        my_predict = my_model.predict(hand,
                                    batch_size=1,
                                    verbose=0)

        if (mode):
            testing_mode(my_predict, frame, width, height, label_dict)
        else:
            demo_mode(targetLetter, my_predict, frame, width, height, label_dict)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Press 'q' to exit live loop
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Calculate frames per second
    end = time.time()
    FPS = fps/(end-start)
    print("[INFO] approx. FPS: {:.2f}".format(FPS))

    # Release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
