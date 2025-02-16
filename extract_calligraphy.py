# Author: 김재민 (Jaemin Kim)
# Date: 2025-02-11
# Group: 연세서우회 (Yonsei SeowooHoe)

import cv2
import os
import glob
import numpy as np

def extract_calligraphy_black_on_white(input_path, output_path, threshold_value=200):
    # 이미지 로드
    image = cv2.imread(input_path)
    if image is None:
        print("이미지를 불러올 수 없습니다.")
        return
    
    # 그레이스케일 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 이진화 (배경을 흰색, 글씨를 검은색으로)
    # threshold_value보다 어두운 픽셀은 0(검은색), 밝은 픽셀은 255(흰색)이 됩니다.
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
        
    # 결과 이미지 저장
    cv2.imwrite(output_path, binary)
    print(f"글자는 검은색, 배경은 흰색으로 추출된 이미지를 {output_path}에 저장했습니다.")

if __name__ == '__main__':
    path_to_inputs = os.path.join('input', '*.jpg')
    inputs_files = glob.glob(path_to_inputs)

    for input_image_path in inputs_files:
        output_image_path = os.path.join('output', os.path.basename(input_image_path))
        extract_calligraphy_black_on_white(input_image_path, output_image_path, threshold_value=130)