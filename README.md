# LiCa-Insight

카메라 영상에서부터 추적 대상의 공간상의 위치를 계산하고 수집한 동선 데이터를 웹사이트를 통해 시각화하여 제공합니다.

# Acknowledgement
- 활용된 MOT(Multiple Object Tracking) 모델은 [noahcao/OC_SORT](https://github.com/noahcao/OC_SORT) 레포지토리에서 제공하는 pretrained 모델입니다.
- 프로젝트 요구사항에 맞춰 OC_SORT의 demo_track.py 스크립트를 커스텀 하였습니다.
- ocsort_custom/tools 디렉토리에서 커스텀된 스크립트를 확인할 수 있습니다. 

# Demo
삼성청년SW아카데미 서울캠퍼스 휴게실을 지나드는 교육생들의 동선 데이터를 수집하고 시각화한 데모입니다.


## Location Dots
![location_dots](https://github.com/KevRiver/LiCa-Insight/assets/25262306/c9d95760-3a08-4423-b479-eaf87c7b1472)

## Heatmap
![heatmap](https://github.com/KevRiver/LiCa-Insight/assets/25262306/5f611062-46bc-42c4-a962-5492d0488150)

## Tracking
### 1
![2023-05-18-10-05-00-_-10-05-30 (1)](https://github.com/KevRiver/LiCa-Insight/assets/25262306/5d63bc90-6e2c-4dfc-98b7-dca5d24d3ddb)
![2023-05-18_10-05-00___10-05-30_-_Trace (1)](https://github.com/KevRiver/LiCa-Insight/assets/25262306/c99cb705-38ee-410f-9b4e-4f2275843990)

# System Architecture
![A208 System Architecture v0 4](https://github.com/KevRiver/LiCa-Insight/assets/25262306/381251db-dc8f-4bd5-80c3-daa05999f5a5)
![30 (1)](https://github.com/KevRiver/LiCa-Insight/assets/25262306/aad1374d-78d1-4787-b9ea-6178a8538e22)

# Built With
## Frontend
---
<div>
    <img src="https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white">
    <img src="https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=white">
    <img src="https://img.shields.io/badge/axios-5A29E4?style=for-the-badge&logo=axios&logoColor=white">
    <img src="https://img.shields.io/badge/recoil-3578e5?style=for-the-badge">
</div>

## Backend
<div>
    <img src="https://img.shields.io/badge/spring_boot-2.7.11-6DB33F?style=for-the-badge&logo=springboot&logoColor=white">
    <img src="https://img.shields.io/badge/spring_security-6DB33F?style=for-the-badge&logo=springsecurity&logoColor=white">
    <img src="https://img.shields.io/badge/jwt-0.9.1-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white">
    <img src="https://img.shields.io/badge/spring_amqp-6DB33F?style=for-the-badge&logo=spring&logoColor=white">
    <img src="https://img.shields.io/badge/spring_data_jpa-6DB33F?style=for-the-badge&logo=spring&logoColor=white">
    <img src="https://img.shields.io/badge/sendinblue-6.0.0-0092FF?style=for-the-badge&logo=sendinblue&logoColor=white">
    <img src="https://img.shields.io/badge/swagger-3.0.0-85EA2D?style=for-the-badge&logo=swagger&logoColor=white">
    <img src="https://img.shields.io/badge/gradle-7.6.1-02303A?style=for-the-badge&logo=gradle&logoColor=white">
    <br>
    <img src="https://img.shields.io/badge/python-3.9.13-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/pika-1.3.1-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/opencv-4.7.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
</div>

## Embedded
<div>
    <img src="https://img.shields.io/badge/raspberrypi_4-CD2355?style=for-the-badge">
    <img src="https://img.shields.io/badge/python-3.9.13-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/pika-1.3.1-3776AB?style=for-the-badge&logo=python&logoColor=white">
    <img src="https://img.shields.io/badge/opencv-4.7.0-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white">
</div>

## Infra
<img src="https://img.shields.io/badge/aws_ec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white">
<img src="https://img.shields.io/badge/ubuntu-20.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white">
<img src="https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white">
<img src="https://img.shields.io/badge/jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white">
<img src="https://img.shields.io/badge/rabbitmq-3--management-FF6600?style=for-the-badge&logo=rabbitmq&logoColor=white">
<img src="https://img.shields.io/badge/nginx-009639?style=for-the-badge&logo=nginx&logoColor=white">
