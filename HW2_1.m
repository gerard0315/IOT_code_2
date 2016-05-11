%Ben Zhu
%bjz2107
%PS2 problem 1 edge detection
clf
%given script parts a + b
I = imread('parkingphoto.png');
h = [0 1 0; 1 -4 1; 0 1 0];
I2 = imfilter(I,h);
imshow(I), title('Original Image');
figure(2)
imshow(I2), title('Filtered Image a')


%The filter removes everything but edges ... as it suggests. It detects
%these edges using a method of looking at certain dark edges with 
%light pixels surrounding it. (off center/ onsurround)
%It is necessary for it to equal zero because it is a filter of the image
%and if it did not equal zero, it wouldn't equally alter parts of the photo
%so it'd be not stable as a filter. 



%part C 4x4 on center off surround
h2 = [0 -1 -1 0; -1 2 2 -1; -1 2 2 -1; 0 -1 -1 0];
  
I3 = imfilter(I,h2);

figure(3)
imshow(I3), title('Filtered Image c');

%So this is on center, off surround 4x4. It takes in the areas where it is
%brighter than surrounding, and enhances those areas, effectively
%brightening the bright centers/edges. 
%This picture appears to be more clear than the first filter, perhaps this
%is due to the 4x4 matrix causing a larger block to be compared, which
%results in better filtering?

% part D

h3=[-1 -1 -1; 2 2 2; -1 -1 -1];
I4 = imfilter(I,h3);

figure(4)
imshow(I4), title('Filtered Image mystery');

%Well, it looks like it is taking all the horizontal lines or edges, where
%everything above and below are dark and everything to left or right is
%bright, and enhances those. So vertical dark, horizontal bright


%Transposed
I5 = imfilter(I, h3.');
figure(5)
imshow(I5), title('Filtered Image transposed');


%The transpose of that matrix now enhances vertically. That is to say, for
%edges where they are horizontally surrounded by dark pixels, and
%vertically by bright pixels, those get enhanced, as evidenced by the
%vertical lines popping out.



% Can you synthesize an image that converts to all black and is reproduced 
% for either of these previous filters? Try using Inkscape or Illustrator 
% if you do not have a favorite drawing program.

%for horiz and vert edge detection- stripes of the opposite of each should 
% result in an all black image
horizontalstripes = imread('horizontalstripes.jpg');
verticalstripes = imrotate(horizontalstripes,90); 

figure(6)
imshow(horizontalstripes), title('Horizontal Stripes');

figure(7)
imshow(verticalstripes), title('Vertical Stripes');



horizontalfilter = imfilter(verticalstripes, h3);
figure(9)
imshow(horizontalfilter), title('Filtered Vertical Stripes');

verticalfilter = imfilter(horizontalstripes, h3.');
figure(8)
imshow(verticalfilter), title('Filtered Horizontal Stripes');