import subprocess
import time
import os
import re

#verifier와 yaml 파일 경로
verifier_dir = os.path.join(os.path.dirname(__file__), "alpha-beta-CROWN", "complete_verifier")
yaml_path = os.path.join(os.path.dirname(__file__), "custum.yaml")

command = ["python", "abcrown.py", "--config", yaml_path]
return_code = None

#시작 시간
start_time = time.time()

try:
    #프로그램 실행
    process = subprocess.run(
        command, 
        cwd=verifier_dir, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.STDOUT, 
        text=True,
        encoding='utf-8',
        errors='ignore',
        check=True
    )
    return_code = process.returncode
    full_output = process.stdout
    
except subprocess.CalledProcessError as e:
    return_code = e.returncode
    full_output = e.output
    print(f"오류가 발생했습니다: {e}")

#종료시간
end_time = time.time()
elapsed_time = end_time - start_time
print(full_output)

#정상실행 되었을 경우
if return_code is not None:
    #전체 로그에서 필요한 최종 통계 정보 추출
    verified_acc = "N/A"
    safe_count = 0
    unsafe_count = 0
    timeout_count = 0

    # 정규표현식으로 요약 패턴 탐색
    acc_match = re.search(r"Final verified acc:\s*([\d.]+)%", full_output)
    if acc_match:
        verified_acc = acc_match.group(1)

    summary_match = re.search(r"total verified \(safe/unsat\):\s*(\d+)\s*,\s*total falsified \(unsafe/sat\):\s*(\d+)\s*,\s*timeout:\s*(\d+)", full_output)
    if summary_match:
        safe_count = int(summary_match.group(1))
        unsafe_count = int(summary_match.group(2))
        timeout_count = int(summary_match.group(3))
        
    print(f"종료 상태 코드: {return_code}")
    print(f"총 검증 소요 시간: {elapsed_time:.2f} 초")
    print(f"검증 정확도: {verified_acc}%")
    print(f"반례 발견 : {unsafe_count} 개")
    print(f"검증 완료 : {safe_count} 개")
    print(f"타임아웃 : {timeout_count} 개")