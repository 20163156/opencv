2018 ComputerVision Final Project

주제:동전(coin) 영상에서 서로 다른 동전들의 개수와 위치를 파악.
고려사항 : 이미지가 무슨 노이즈가 있는지 입력으로 주면 안되고 알아서 판별해야 한다.

먼저  salt & pepper noise는 median filter로 
gaussian noise는 gaussian filter후 sharping을 적용하기 위해 salt&pepper noise를 먼저 골라낸다.
salt & pepper는 이미지 전체에 흰점 검은점이 골고루 퍼져있으므로 이미지를 히스토그램으로 나타냈을때 0값과 255값이 
평균보다 많을 것이다. 따라서 이미지의 0값과 255값이 평균 전체 픽셀수 / 256 값보다 크면 미디언필터를 적용한다.
조건을 벗어나면 가우시안 필터를 적용한후 샤프닝 처리를 하는것으로 구현한다.
