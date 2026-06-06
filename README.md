<h1>신뢰할 수 있는 인공지능 Assignemnt4</h1>
Fashion mnist와 간단한 DNN을 𝛼, 𝛽-Crown에 넣어 Formal Verification을 증명하는 프로그램

<h2>Exploration report</h2>
<b>A summary of the 𝛼, 𝛽-Crown models directory: what models, configurations, and verification setups are available. If applicable, briefly compare the organization with Marabou’s
resources.</b>

𝛼, 𝛽-Crown은 fc model이나 VGG16, ResNet 과 같은 전통적인 모델이서 cora같은 GNN, safenlp같은 자연어 처리모델, 커스템 모델까지도 지원이 가능하다. 또한
mnistfc, cifar10, cifar100, collins 등의 검증 대상 데이터 셋을 지원하며, eran, oval, marabou등의 타 검증 도구 또한 연동하여 사용이 가능하다.

Marabou는 SMT 솔버의 특성상 소규모의 MLP 모델이나 ACAS Xu같은 정적 제어 시스템에 그 검증 도메인이 제한되어 있지만 𝛼, 𝛽-Crown은 수학적으로 미분가능하기 때문에 GPU를 지원하여 
대형 모델에서도 사용이 가능하다. 또한 Marabou와는 달리 yaml파일로 표준화하여 관리하기 때문에 테스트와 리소스 관리가 체계적이라는 장점이 있다.


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
1. assignment4/alpha-beta-CROWN/complete_verifier/models/my_model 경로에 my_model을 추가로 생성하여 onnx 모델을 추가.

2. Fashion-MNIST데이터에 대한 검증을 위해 complete_verifier/custom/custom_model_data.py 에서 Fashion-MNIST 커스텀 데이터 로더를 추가 (31 ~ 61 line, fashion_mnist())

4. NotImplementedError해결을 위해 assignment4/alpha-beta-CROWN/complete_verifier/loading.py 에서 fashion_mnist 분기를 최상단에 배치 (45~85 line)
