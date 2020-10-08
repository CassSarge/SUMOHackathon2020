# SUMOHackathon2020

Using OpenCV and NN to provide real time feedback on sign language education.

SUMO Hackathon Project for team Vault Dwellers




## Neural Network
The neural network can be loaded from a variety of pretrained models, including:
- VGG16
- ResNet50
- MobileNet

The script then grabs a frame from the computers default webcam and highlights a region of interest. This region will be passed to the classifier and our model will predict the most likely ASL fingerspelt alphabet. 

## References

Neural Network was trained by: https://github.com/BelalC/sign2text

Most of the code for computer vision and NN was used from or largely based on this source.

Sources for pitch and initial research: 

Stats on deafness: https://www.who.int/news-room/facts-in-pictures/detail/deafness

[English literacy as a barrier to health care information for deaf people who use Auslan ](https://d1wqtxts1xzle7.cloudfront.net/33719433/2013_Napier_AFP.pdf?1400291642=&response-content-disposition=inline%3B+filename%3DEnglish_literacy_as_a_barrier_to_healthc.pdf&Expires=1602034757&Signature=gxXI1R2vpLPYJaCXijUwYP-TU6jopZcdlc2Qf74nXk3eK4jhKZD3ePB~4OabDV-Vl11kvI2qbW62q~DrGBgrQXKC-9cwasCBgUpaGTaYMNRCLCbtLEGc259by~OT2iGSpR4BNJhMgcnD6wSqqK4rhFJMyBonBKUboTPXyps7c92Vjb30koR1uJB51QU1zJMLGkUnnS0nNyd-9Hsd7y6ydq6QsZB6GJIZK5kCb2cLkOfEFREXv8nHq-4jSg-dus2H9wFn5Cnb9Clez4z0y0fJmDFjjYgMQ3qcW~7OVuSgygzXREqS4a5zM5-i51v~ivyRKLiTLa~UI2LS9jR2pRjqLw__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

Healthcare info: https://theconversation.com/accessing-healthcare-is-challenging-for-deaf-people-but-the-best-solution-isnt-one-size-fits-all-127734

Interpreter Shortage: https://mable.com.au/newsroom/auslan-national-shortage/

Qualification: https://smartandskilled.nsw.gov.au/sands/qualification/PSP51018

Initial source pg 6-7: https://issuu.com/srcpubs/docs/honi_soit_2018__semester_02__week_0_4e6d77f51585ac
