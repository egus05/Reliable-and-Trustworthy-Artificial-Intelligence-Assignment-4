import subprocess
import time
import os

#verifier와 yaml 파일 경로
verifier_dir = os.path.join(os.path.dirname(__file__), "alpha-beta-CROWN", "complete_verifier")
yaml_path = os.path.join(os.path.dirname(__file__), "custum.yaml")

command = ["python", "abcrown.py", "--config", yaml_path]
return_code = None

#시작 시간
start_time = time.time()

try:
    #프로그램 실행
    process = subprocess.run(command, cwd=verifier_dir, check=True)
    return_code = process.returncode
except subprocess.CalledProcessError as e:
    print(f"오류가 발생했습니다: {e}")

#종료시간
end_time = time.time()
elapsed_time = end_time - start_time

#정상실행 되었을 경우
if return_code is not None:
    print(f"종료 상태 코드: {return_code}")
    print(f"총 검증 소요 시간: {elapsed_time:.2f} 초")