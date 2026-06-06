<h1>신뢰할 수 있는 인공지능 Assignemnt4</h1>
Fashion mnist와 간단한 DNN을 𝛼, 𝛽-Crown에 넣어 Formal Verification을 증명하는 프로그램


<h2>구성 요소</h2>

test.py: 모델을 불러와서 Fashion mnist에 대한 foram verification을 증명

custum.yaml: custom_model.yaml을 바탕으로 만든 yaml 파일 (모델을 fashion_mnist_dnn_light.onnx로 dataset을 fashion_mnist로 수정 및 batch_size 1021, epsilon = 0.05로 변경)

<h2>실행 방법</h2>
#새로운 가상환경 생성
conda env create -f complete_verifier/environment.yaml --name alpha-beta-crown

#가상환경 활성화
conda activate alpha-beta-crown

#test.py 실행
python test.py

<h2>예상 결과</h2>
총 검증 소요 시간

검증 정확도

반례 발견

검증 완료

타임아웃

등과 같은 정보.

<h2>alpha-beta-CROWN 폴더에서의 변경사항</h2>
1. /home/egus05/assignment4/alpha-beta-CROWN/complete_verifier/models/my_model 경로에 my_model을 추가로 생성하여 onnx 모델을 추가.

2. Fashion-MNIST데이터에 대한 검증을 위해 complete_verifier/custom/custom_model_data.py 에서 Fashion-MNIST 커스텀 데이터 로더를 추가 (31 ~ 61 line, fashion_mnist())

4. NotImplementedError해결을 위해 /home/egus05/assignment4/alpha-beta-CROWN/complete_verifier/loading.py 에서 fashion_mnist 분기를 최상단에 배치 (45~85 line)
